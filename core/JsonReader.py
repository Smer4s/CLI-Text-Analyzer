import json
from models.Document import Document

class JsonReader(object):
    def __init__(self):
        super(JsonReader, self).__init__()

    def read_json(self, path:str) -> list[Document]:
        try:
            with open(path) as f:
                file_content = f.read()
                docs: list[Document] = []
                for doc in json.loads(file_content):
                    try:
                        docs.append(Document(doc["id"], doc["text"]))
                    except KeyError as e:
                        print("Exception!!! Expected to have a field:", e)
                return docs
        except OSError:
            raise FileNotFoundError(path)
        
            
    