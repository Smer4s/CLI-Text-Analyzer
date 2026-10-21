from core.DocumentProcessor import process_document_async
from models.Document import Document
from models.DocumentProcessorResult import DocumentProcessorResult
import asyncio

async def process_batch(documents: list[Document], max_concurrency: int, delay: float) -> list[DocumentProcessorResult]:
    semaphore = asyncio.Semaphore(max_concurrency)
    tasks = [asyncio.create_task(process_document_async(doc, semaphore, delay)) for doc in documents]
    
    await asyncio.gather(*tasks)
        
    results = [task.result() for task in tasks]
    return results
