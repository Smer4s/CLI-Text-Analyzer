# CLI Text Analyzer Project

## Helps you to analyze text documents in **input.json** and gives you result in **output.json**

### Usage:

> `` uv run main.py -i input.json -o output.json ``

## Example:
### input.json:
    [
        {
            "id2": "doc-1",
            "text": "   Hello hello Python    World   "
        },
        {
            "id": "doc-2",
            "text": "Async programming programming is awesome Async programming programming is rap rap apple apple apple apple awesome Async programming programming is awesome Async programming programming is awesome Async programming programming is awesome"
        },
        {
            "id": "doc-3",
            "text": "   "
        }
    ]

### Console Output:

    Exception!!! Expected to have a field: 'id'
    Error!!! (Document(id='', text=''), 'Failed Document Parsing', '404')
    Error!!! (Document(id='doc-3', text='   '), 'Document is empty', '400')
    Successfully wrote 1 documents. 2 were failed!

### output.json:
    [
        {
            "document": {
                "id": "",
                "text": ""
            },
            "symbol_count": 0,
            "word_count": 0,
            "unique_word_count": 0,
            "normalized_text": "",
            "max_frequent_words": [],
            "document_status": "Failed",
            "error_code": "404",
            "error_message": "Failed Document Parsing"
        },
        {
            "document": {
                "id": "doc-2",
                "text": "Async programming programming is awesome Async programming programming is rap rap apple apple apple apple awesome Async programming programming is awesome Async programming programming is awesome Async programming programming is awesome"
            },
            "symbol_count": 236,
            "word_count": 31,
            "unique_word_count": 6,
            "normalized_text": "Async programming programming is awesome Async programming programming is rap rap apple apple apple apple awesome Async programming programming is awesome Async programming programming is awesome Async programming programming is awesome",
            "max_frequent_words": [
                {
                    "word": "programming",
                    "count": 10
                },
                {
                    "word": "async",
                    "count": 5
                },
                {
                    "word": "is",
                    "count": 5
                },
                {
                    "word": "awesome",
                    "count": 5
                },
                {
                    "word": "apple",
                    "count": 4
                }
            ],
            "document_status": "Success",
            "error_code": "",
            "error_message": ""
        },
        {
            "document": {
                "id": "doc-3",
                "text": "   "
            },
            "symbol_count": 0,
            "word_count": 0,
            "unique_word_count": 0,
            "normalized_text": "",
            "max_frequent_words": [],
            "document_status": "Failed",
            "error_code": "400",
            "error_message": "Document is empty"
        }
    ]