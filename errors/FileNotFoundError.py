class FileNotFoundError(Exception):
    file_name: str
    def __init__(self, file_name):
        super().__init__(file_name)
        self.file_name = file_name