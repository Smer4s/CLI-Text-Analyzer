from models.DocumentStatus import DocumentStatus
from models.Document import Document
from models.DocumentProcessorResult import DocumentProcessorResult
from models.WordCountPair import WordCountPair

class DocumentProcessor(object):
    """docstring for DocumentProcessor."""
    def __init__(self):
        super(DocumentProcessor, self).__init__()
    
    @staticmethod
    def process_document(doc: Document) -> DocumentProcessorResult:
        symbol_count = DocumentProcessor.find_symbol_count(doc.text)
        word_count = DocumentProcessor.find_word_count(doc.text)
        unique_word_count = DocumentProcessor.find_unique_word_count(doc.text)
        normalized_text = DocumentProcessor.normalize_text(doc.text)
        max_frequent_words = DocumentProcessor.find_max_frequent_words(doc.text)
        doc_status = DocumentProcessor.get_document_status(doc.text)
        
        return DocumentProcessorResult(doc, symbol_count, word_count, unique_word_count, normalized_text, max_frequent_words,doc_status)
    
    @staticmethod
    def find_symbol_count(text: str) -> int:
        symbol_count = 0
        for symbol in text:
            if symbol != ' ':
                symbol_count += 1
                
        return symbol_count
    
    @staticmethod
    def find_word_count(text: str) -> int:
        words = DocumentProcessor.find_words(text)
        
        return len(words)
    
    @staticmethod
    def find_words(text:str) -> list[str]:
        words : list[str] = []
        prev_character_is_symbol = False
        word: str = ''
        for symbol in text:
            if symbol != ' ':
                prev_character_is_symbol = True
                word += symbol
            else:
                if prev_character_is_symbol:
                    words.append(word)
                    word = ''
                prev_character_is_symbol = False
        
        if prev_character_is_symbol:
            words.append(word)
                    
        return words
    
    @staticmethod
    def find_unique_word_count(text: str) -> int:
        words = DocumentProcessor.find_words(text)
        
        lowercase_words :set[str] = set()
        for word in words:
            lowercase_word = word.lower()
            lowercase_words.add(lowercase_word)
        
        return len(lowercase_words)

    @staticmethod
    def normalize_text(text: str) -> str:
        normalized_text: str = ''
        should_read = False
        should_add_space = False
        previous_character_is_space = False
        had_symbols = False
        
        for symbol in text:
            if symbol != ' ':
                should_read = True
                if previous_character_is_space and had_symbols:
                    should_add_space = True
                else:
                    should_add_space = False
                    
                had_symbols = True
                previous_character_is_space = False
            else:
                should_read = False
                should_add_space = False
                previous_character_is_space = True
                
            if should_add_space:
                normalized_text += ' '
            
            if should_read:
                normalized_text += symbol
                
        return normalized_text 
    
    @staticmethod
    def find_max_frequent_words(text: str, max_count:int = 5) -> list[WordCountPair]:
        words = DocumentProcessor.find_words(text)
        result_dict : dict[str,int] = {}
        for searchable in words:
            count = 0
            for word in words:
                if word == searchable:
                    count += 1
            
            result_dict.update({searchable: count}) 
                
        pairs :list[WordCountPair] = []
        for word, count in result_dict.items():
            pair = WordCountPair(word,count)
            pairs.append(pair)
        sorted_dict = sorted(pairs, key=(lambda par : par.count), reverse=True)
        
        return sorted_dict[:max_count]
                
    
    @staticmethod
    def get_document_status(text:str) -> DocumentStatus:
        for symbol in text:
            if symbol.isascii() is False:
                return DocumentStatus.FAILED
            
        return DocumentStatus.SUCCESS