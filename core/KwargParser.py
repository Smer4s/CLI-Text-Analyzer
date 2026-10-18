from models.IOPair import IOPair
from errors.WrongKwargError import WrongKwargError

class KwargParser(object):
    def __init__(self):
        super(KwargParser, self).__init__()
        
    def parse_input(self, kwargs: dict[str, str]) -> IOPair:
        input_path = self. parse_kwarg(kwargs,'i')
        output_path = self.parse_kwarg(kwargs,'o')
        return IOPair(input_path,output_path)

    def parse_kwarg(self, kwargs: dict[str, str], key: str) -> str:
        kwarg = kwargs.get(key)
        if kwarg is None:
            raise WrongKwargError(key)
        return kwarg    