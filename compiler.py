



class Token():
    def __init__(self):
        pass



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