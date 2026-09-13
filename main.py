
import sys

# reference: https://en.wikipedia.org/wiki/Tiny_BASIC

def raise_invalid_path(): 
    raise Exception("INVALID SOURCE CODE PATH" + str(sys.argv))

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

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Compiler().parse(sys.argv[1])
    else:
        raise_invalid_path()