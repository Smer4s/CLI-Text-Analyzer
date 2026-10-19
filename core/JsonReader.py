import json
from models.Document import Document

class JsonReader(object):
    def __init__(self):
        super(JsonReader, self).__init__()

    def read_json(self, path:str) -> list[Document]:
        try:
            with open(path) as f:
                file_content = f.read()
                docs = [Document(doc["id"], doc["text"]) for doc in json.loads(file_content)]
                return docs
        except OSError:
            raise FileNotFoundError(path)   
    