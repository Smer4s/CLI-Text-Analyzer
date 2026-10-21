# CLI Text Analyzer Project

## Helps you to analyze text documents in **input.json** and gives you result in **output.json**

### Usage:

> `` uv run main.py -i input.json -o output.json -c 50 -d 0.2 ``

## Example:

### input.json:

<details>
<summary> JSON file </summary>

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

</details>

### Console Output:

<details>
<summary> Console Output </summary>

    Exception!!! Expected to have a field: 'id'
    Started processing  at: 11:45:01.318324
    Started processing doc-2 at: 11:45:01.521035
    Started processing doc-3 at: 11:45:01.722528
    Error!!! (Document(id='', text=''), 'Failed Document Parsing', '404')
    Error!!! (Document(id='doc-3', text='   '), 'Document is empty', '400')
    Successfully wrote 1 documents. 2 were failed! 1 tasks ran concurrently with 0.2 seconds. Total execution time was: 0.61

</details>

### output.json:

<details>
<summary> JSON file </summary>

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

</details>

### Benchmark results

<details>
<summary> Results Table </summary>

| Concurrency  | Execution time |
| -----------  | -----------    |
| 50           | 0.43           |
| 40           | 0.42           |
| 30           | 0.41           |
| 25           | 0.61           |
| 15           | 0.82           |
| 13           | 1.02           |
| 10           | 1.22           |
| 5            | 2.44           |
| 1            | 12.18          |

</details>

> Even with `` concurrency = 50 `` **Execution Time** is not `` 0s `` because of *I/O operations*, *delay* and *CPU-bound operations* 