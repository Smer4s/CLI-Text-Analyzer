import argparse, sys
from errors.DocumentProcessorError import DocumentProcessorError
from core.JsonReader import JsonReader
from core.JsonWriter import JsonWriter
from core.DocumentProcessor import process_document
from models.DocumentProcessorResult import DocumentProcessorResult
from models.DocumentStatus import DocumentStatus

def main(parser: argparse.ArgumentParser) -> None:   
    try:
        cli_args : argparse.Namespace = parser.parse_args()
        (input_path, output_path) = (cli_args.i, cli_args.o)
        reader = JsonReader()
        docs = reader.read_json(input_path)
        (success, failed) = (0, 0)
        
        result_docs :list[DocumentProcessorResult]= []
        for doc in docs:
            try:
                result = process_document(doc)
                result_docs.append(result)
                if result.document_status == DocumentStatus.FAILED:
                    raise DocumentProcessorError(doc, result.error_message, result.error_code)
                else:
                    success += 1
            except Exception as e:
                print("Error!!!", e)
                failed +=1
            
        writer = JsonWriter()
        writer.write_json(result_docs, output_path)
        print("Successfully wrote", success, "documents.", failed, "were failed!")        
    except Exception as e:
        print("Unexpected Exception!!!", e)
        sys.exit(-1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='CLI Text Analyzer')
    parser.add_argument('-i', help='path to input file', required=True)
    parser.add_argument('-o', help='path to output file', required=True)
    
    main(parser)
