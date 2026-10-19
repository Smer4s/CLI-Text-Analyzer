from models.Document import Document

class DocumentProcessorError(Exception):        
    doc: Document
    error_code: str 
    error_message: str 
    
    def __init__(self, doc: Document, error_code: str, error_message: str):
        super(DocumentProcessorError).__init__()
        self.doc = doc
        self.error_code = error_code
        self.error_message = error_message