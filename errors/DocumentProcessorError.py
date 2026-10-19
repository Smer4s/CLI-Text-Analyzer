from models.Document import Document

class DocumentProcessorError(Exception):
    def __init__(self, doc: Document):
        super(DocumentProcessorError).__init__()
        self.doc = doc
    doc: Document

    