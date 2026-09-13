import enum

class Token(enum.Enum):
    PRINT = 1
    GOTO = 2
    INPUT = 3
    LET = 4
    GOSUB = 5
    RETURN = 6
    CLEAR = 7
    LIST = 8
    RUN = 9
    END = 10





class Lexer():
    def __init__(self):
        pass
    def to_tokens(self,contents):
        print(contents)
        return None



class Compiler():
    def __init__(self):
        self.lexer = Lexer()
        self.tokens = None
    def parse(self, path):
        contents = None
        with open(path) as f:
            contents = f.read()
        if contents:
            self.tokens = self.lexer.to_tokens(contents)