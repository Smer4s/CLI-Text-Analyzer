import json
from models.Document import Document
from errors.DocumentProcessorError import DocumentProcessorError

class JsonReader(object):
    def read_json(self, path:str) -> list[Document]:

        with open(path) as f:
            file_content = f.read()
            docs: list[Document] = []
            for doc in json.loads(file_content):
                try:
                    id = doc["id"]
                    text = doc["text"]
                    
                    if type(id) != str or type(text) != str:
                        raise DocumentProcessorError(Document(), "402", "Expected to have text value in field \'id\' or \'text\'")
                    docs.append(Document(id, text))
                except KeyError as e:
                    print("Exception!!! Expected to have a field:", e)
                    docs.append(Document())
                except DocumentProcessorError as e:
                    print("Exception!!!", e)
                    docs.append(Document())
            return docs