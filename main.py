import argparse, sys, asyncio
from errors.DocumentProcessorError import DocumentProcessorError
from core.JsonReader import JsonReader
from core.JsonWriter import JsonWriter
from core.DocumentProcessor import process_document
from models.DocumentProcessorResult import DocumentProcessorResult
from models.DocumentStatus import DocumentStatus
from core.AsyncBatchExecutor import process_batch
from time import perf_counter

async def main(parser: argparse.ArgumentParser) -> None:   
    
        cli_args : argparse.Namespace = parser.parse_args()
        (input_path, output_path, concurrency, delay) = (cli_args.i, cli_args.o, int(cli_args.c), float(cli_args.d))
        reader = JsonReader()
        docs = reader.read_json(input_path)
        (success, failed) = (0, 0)
        
        start_time = perf_counter()
        result_docs = await process_batch(docs, concurrency, delay)
        end_time = perf_counter()
        
        result_time = end_time - start_time
        
        for result in result_docs:
            try:
                if result.document_status == DocumentStatus.FAILED:
                    raise DocumentProcessorError(result.document, result.error_message, result.error_code)
                else:
                    success += 1
            except Exception as e:
                print("Error!!!", e)
                failed +=1
            
        writer = JsonWriter()
        writer.write_json(result_docs, output_path)
        print("Successfully wrote", success, "documents.", failed, "were failed!", concurrency, "tasks ran concurrently with", delay, "seconds. Total execution time was:", round(result_time,2))        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='CLI Text Analyzer')
    parser.add_argument('-i', help='path to input file', required=True)
    parser.add_argument('-o', help='path to output file', required=True)
    parser.add_argument('-c', help='max concurrency', required=True)
    parser.add_argument('-d', help='delay between tasks', required=True)
    
    asyncio.run(main(parser))
