from dataclasses import dataclass
from models.Document import Document
from models.DocumentStatus import DocumentStatus
from models.WordCountPair import WordCountPair
import json

@dataclass
class DocumentProcessorResult(object):
    document: Document
    symbol_count: int
    word_count: int
    unique_word_count: int
    normalized_text: int
    max_frequent_words: list[WordCountPair]
    document_status: DocumentStatus