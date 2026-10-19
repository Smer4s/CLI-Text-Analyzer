import json
from models.Document import Document

class JsonReader(object):
    def read_json(self, path:str) -> list[Document]:

        with open(path) as f:
            file_content = f.read()
            docs: list[Document] = []
            for doc in json.loads(file_content):
                try:
                    docs.append(Document(doc["id"], doc["text"]))
                except KeyError as e:
                    print("Exception!!! Expected to have a field:", e)
                    docs.append(Document())
            return docs