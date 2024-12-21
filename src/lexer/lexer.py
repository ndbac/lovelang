from .tokens import Token, TokenType

class Lexer:
    def __init__(self, source: str):
        self.source = source
        self.pos = 0
        self.line = 1
        self.current_char = self.source[0] if source else None

    def advance(self):
        self.pos += 1
        if self.pos >= len(self.source):
            self.current_char = None
        else:
            if self.current_char == '\n':
                self.line += 1
            self.current_char = self.source[self.pos]

    def skip_whitespace(self):
        while self.current_char and self.current_char.isspace():
            self.advance()

    def skip_comment(self):
        while self.current_char and self.current_char != '\n':
            self.advance()

    def get_token(self):
        while self.current_char:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char == 'x' and self.peek() == 'o':
                self.advance()
                self.advance()
                self.skip_comment()
                continue

            # Map characters to token types
            simple_tokens = {
                '+': TokenType.PLUS,
                '-': TokenType.MINUS,
                '*': TokenType.MULTIPLY,
                '/': TokenType.DIVIDE,
                '(': TokenType.LPAREN,
                ')': TokenType.RPAREN,
                '{': TokenType.LBRACE,
                '}': TokenType.RBRACE,
                ';': TokenType.SEMICOLON
            }

            if self.current_char.isdigit():
                return self.number()
            if self.current_char.isalpha():
                return self.identifier()
            if self.current_char == '"':
                return self.string()
            if self.current_char in ['=', '!', '<', '>']:
                return self.comparison_operator()
            if self.current_char in simple_tokens:
                token = Token(simple_tokens[self.current_char], self.current_char, self.line)
                self.advance()
                return token

            raise SyntaxError(f"Invalid character '{self.current_char}' at line {self.line}")

        return Token(TokenType.EOF, None, self.line)

    def peek(self):
        peek_pos = self.pos + 1
        if peek_pos >= len(self.source):
            return None
        return self.source[peek_pos]

    def number(self):
        result = ''
        while self.current_char and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        
        if self.current_char == '.':
            result += self.current_char
            self.advance()
            while self.current_char and self.current_char.isdigit():
                result += self.current_char
                self.advance()
        
        return Token(TokenType.NUMBER, result, self.line)

    def identifier(self):
        result = ''
        while self.current_char and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        
        # Check for keywords
        token_type = TokenType(result) if result in [t.value for t in TokenType] else TokenType.IDENTIFIER
        return Token(token_type, result, self.line)

    def string(self):
        self.advance()  # Skip opening quote
        result = ''
        while self.current_char and self.current_char != '"':
            result += self.current_char
            self.advance()
        
        if self.current_char != '"':
            raise SyntaxError(f"Unterminated string at line {self.line}")
        
        self.advance()  # Skip closing quote
        return Token(TokenType.STRING, result, self.line)

    def comparison_operator(self):
        current = self.current_char
        next_char = self.peek()
        
        if current == '=' and next_char == '=':
            self.advance()
            self.advance()
            return Token(TokenType.EQ, '==', self.line)
        elif current == '!' and next_char == '=':
            self.advance()
            self.advance()
            return Token(TokenType.NEQ, '!=', self.line)
        elif current == '<' and next_char == '=':
            self.advance()
            self.advance()
            return Token(TokenType.LTE, '<=', self.line)
        elif current == '>' and next_char == '=':
            self.advance()
            self.advance()
            return Token(TokenType.GTE, '>=', self.line)
        elif current == '<':
            self.advance()
            return Token(TokenType.LT, '<', self.line)
        elif current == '>':
            self.advance()
            return Token(TokenType.GT, '>', self.line)
        elif current == '=':
            self.advance()
            return Token(TokenType.ASSIGN, '=', self.line)
