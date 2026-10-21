from core.DocumentProcessor import process_document_async
from models.Document import Document
from models.DocumentProcessorResult import DocumentProcessorResult
import asyncio

async def process_batch(documents: list[Document], max_concurrency: int, delay: float) -> list[DocumentProcessorResult]:
    validate_params(documents,max_concurrency,delay)
    
    semaphore = asyncio.Semaphore(max_concurrency)
    
    tasks = [asyncio.create_task(run_task_with_semaphore(semaphore, max_concurrency, process_document_async(doc, delay))) for doc in documents]
    
    return await asyncio.gather(*tasks)

async def run_task_with_semaphore(semaphore: asyncio.Semaphore, max_concurrency: int, task) -> DocumentProcessorResult:
    async with semaphore:
        return await task


def validate_params(documents: list[Document], max_concurrency: int, delay: float) -> None:
    doc_len = len(documents)
    if doc_len < 1 or doc_len > 50:
        raise ValueError("Expected documents count MUST be in range 1..50, but got", doc_len)
    if max_concurrency <= 0:
        raise ValueError("Expected concurrency to be greater than 0, but got", max_concurrency)
    if delay < 0:
        raise ValueError("Expected delay to be greater or equal than 0, but got", delay)
