from models.DocumentStatus import DocumentStatus
from models.Document import Document
from models.DocumentProcessorResult import DocumentProcessorResult
from models.WordCountPair import WordCountPair
from errors.DocumentProcessorError import DocumentProcessorError
import asyncio, time, datetime

async def process_document_async(doc: Document, delay: float = 0.2) -> DocumentProcessorResult:
    try:
        print("Started processing", doc.id,"at:",datetime.datetime.time(datetime.datetime.now()))
        await asyncio.sleep(delay)
        result = process_document(doc)
        return result
    except Exception as e:  
        print(f'Exception for doc with id: \"{doc.id}\". Exception:',e)
        return DocumentProcessorResult(doc, error_code='500', error_message='Internal Exception')

def process_document(doc: Document) -> DocumentProcessorResult:
    try:
        doc_status = get_document_status(doc)
        normalized_text = normalize_text(doc.text)
        symbol_count = find_symbol_count(normalized_text)
        words = find_words(normalized_text)
        word_count = len(words)
        unique_word_count = find_unique_word_count(words)
        max_frequent_words = find_max_frequent_words(words)
        return DocumentProcessorResult(doc, symbol_count, word_count, unique_word_count, normalized_text, max_frequent_words,doc_status)
    except DocumentProcessorError as e:
        return DocumentProcessorResult(doc, error_code=e.error_code, error_message=e.error_message)
    
def find_symbol_count(text: str) -> int:
    return len(text)
    
def find_word_count(text: str) -> int:
    words = find_words(text)
        
    return len(words)
    
def find_words(text:str) -> list[str]:
    return text.split()
    
def find_unique_words(words: list[str]) -> set[str]:
    lowercase_words :set[str] = set()
    for word in words:
        lowercase_word = word.lower()
        lowercase_words.add(lowercase_word)
                
    return lowercase_words
    
def find_unique_word_count(words: list[str]) -> int:
    return len(find_unique_words(words))

    
def normalize_text(text: str) -> str:
    return " ".join(text.split())
    
    
def find_max_frequent_words(words: list[str], max_count:int = 5) -> list[WordCountPair]:
    result_dict : dict[str,int] = {}
    for searchable in words:    
        lower = searchable.lower()
        count = result_dict.get(lower, 0)      
        count += 1
        result_dict.update({lower: count}) 
                
    pairs :list[WordCountPair] = []
    for word, count in result_dict.items():
        pair = WordCountPair(word,count)
        pairs.append(pair)
        
    sorted_dict = sorted(pairs, key=(lambda par : par.count), reverse=True)
        
    return sorted_dict[:max_count]
                
    
def get_document_status(doc: Document) -> DocumentStatus:
    if doc.id == '' or doc.text == '':
        raise DocumentProcessorError(doc, "404", "Failed Document Parsing")
    
    for symbol in doc.text:
        if symbol.isspace() is False:
            return DocumentStatus.SUCCESS
                
    raise DocumentProcessorError(doc, "400", "Document is empty")