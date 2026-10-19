from models.DocumentProcessorResult import DocumentProcessorResult
import json
import dataclasses

class JsonWriter(object):
    def write_json(self, docs: list[DocumentProcessorResult], path: str) -> None:
        with open(path, mode='w') as f:
            result_list = [dataclasses.asdict(doc) for doc in docs]
            serialized = json.dumps(result_list, default=str)
            f.write(serialized)