import sys, re
from models.IOPair import IOPair
from errors.WrongKwargError import WrongKwargError
from core.KwargParser import KwargParser
from core.JsonReader import JsonReader
from core.JsonWriter import JsonWriter
from core.DocumentProcessor import DocumentProcessor
from models.DocumentProcessorResult import DocumentProcessorResult

def main(args, kwargs):
    print("Hello from cli-text-analyzer!", "args: ", args, "kwargs: ", kwargs)
    
    try:
        parser = KwargParser()
        pair = parser.parse_input(kwargs)
        input = pair.input_path
        reader = JsonReader()
        docs = reader.read_json(input)
        print(docs)
        processor = DocumentProcessor()
        
        result_docs :list[DocumentProcessorResult]= []
        for doc in docs:
            result = processor.process_document(doc)
            result_docs.append(result)
            
        writer = JsonWriter()
        writer.write_json(result_docs, pair.output_path)
        
    except WrongKwargError as e:
        print("Exception!!! Expected positional argument: ", e.kwarg_name)
        pass
    
def analyze_text():
    pass

if __name__ == "__main__":
    sys_args = sys.argv
    pattern = "^([A-Za-z].*)=(.*$)"
    
    kwargs = dict[str,str]()
    args = list[str]()
    for arg in sys_args:
        if re.match(pattern, arg):
            groups = [g for g in re.split(pattern,arg) if g != '' ]
            key, value = groups[0], groups[1]
            kwargs.update({key:value})
        else:
            args.append(arg)
    
    main(args, kwargs)
