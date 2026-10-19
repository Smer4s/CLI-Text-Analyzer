from dataclasses import dataclass
from models.Document import Document
from models.DocumentStatus import DocumentStatus
from models.WordCountPair import WordCountPair
import json

@dataclass
class DocumentProcessorResult(object):
    document: Document = None
    symbol_count: int = 0
    word_count: int = 0
    unique_word_count: int = 0
    normalized_text: str = 0
    max_frequent_words: list[WordCountPair] = None
    document_status: DocumentStatus = DocumentStatus.FAILED