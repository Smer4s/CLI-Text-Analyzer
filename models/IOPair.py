from dataclasses import dataclass

@dataclass
class IOPair:
    input_path :str
    output_path :str
    
    def __init__(self, input_path, output_path):
        self.input_path=input_path
        self.output_path=output_path
