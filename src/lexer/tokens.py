from enum import Enum

class TokenType(Enum):
    # Keywords
    LOVE = 'love'      # variable declaration
    HEART = 'heart'    # print
    FEEL = 'feel'      # if
    KISS = 'kiss'      # then
    HUG = 'hug'        # else
    FOREVER = 'forever' # while
    CUDDLE = 'cuddle'  # for
    IN = 'in'          # in (for loop)
    TO = 'to'          # range (for loop)
    
    # Operators
    PLUS = '+'
    MINUS = '-'
    MULTIPLY = '*'
    DIVIDE = '/'
    ASSIGN = '='
    
    # Comparison
    EQ = '=='
    NEQ = '!='
    LT = '<'
    GT = '>'
    LTE = '<='
    GTE = '>='
    
    # Delimiters
    LPAREN = '('
    RPAREN = ')'
    LBRACE = '{'
    RBRACE = '}'
    SEMICOLON = ';'
    
    # Other
    NUMBER = 'NUMBER'
    STRING = 'STRING'
    IDENTIFIER = 'IDENTIFIER'
    COMMENT = 'COMMENT'
    EOF = 'EOF'

class Token:
    def __init__(self, type: TokenType, value: str, line: int):
        self.type = type
        self.value = value
        self.line = line
