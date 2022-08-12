TYP_INT = "INT"
TYP_FLOAT = "FLOAT"
TYP_PLUS = "PLUS"
TYP_MINUS = "MINUS"
TYP_MUL = 'MUL'
TYP_DIV = "DIV"
TYP_LPAREN = "LPAREN"
TYP_RPAREN = "RPAREN"
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    def __repr__(self):
        if self.value: 
            return f'{self.type}:{self.value}'
        else:
            return f'{self.type}'
class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()
    def advance(self):
        self.pos += 1
        self.current_char = self.text[pos] if self.pos < len(self.text) else None
    def make_tokens(self):
        tokens = []
        while self.current_char != None:
            if self.current_char in '\t':
                pass
        return tokens
    
        
