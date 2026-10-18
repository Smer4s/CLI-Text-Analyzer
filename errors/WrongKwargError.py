class WrongKwargError(Exception):
    kwarg_name: str
    def __init__(self, kwarg_name):
        super().__init__(kwarg_name)
        self.kwarg_name = kwarg_name