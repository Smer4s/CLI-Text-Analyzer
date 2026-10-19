from dataclasses import dataclass, field
from models.Document import Document
from models.DocumentStatus import DocumentStatus
from models.WordCountPair import WordCountPair
import json

@dataclass
class DocumentProcessorResult(object):
    document: Document = field(default_factory=Document)
    symbol_count: int = 0
    word_count: int = 0
    unique_word_count: int = 0
    normalized_text: str = ''
    max_frequent_words: list[WordCountPair] = field(default_factory=list)
    document_status: DocumentStatus = DocumentStatus.FAILED