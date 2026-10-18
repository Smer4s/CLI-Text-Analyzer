from models.DocumentProcessorResult import DocumentProcessorResult
import json
import jsonpickle

class JsonWriter(object):
    """docstring for JsonWriter."""
    def __init__(self):
        super(JsonWriter, self).__init__()

    def write_json(self, docs: list[DocumentProcessorResult], path: str):
        f = open(path, mode='w')
        result = jsonpickle.encode(docs)
        f.write(result)