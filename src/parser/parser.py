from src.lexer.tokens import TokenType
from src.parser.ast import *

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_token()

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_token()
        else:
            raise SyntaxError(f"Expected {token_type}, got {self.current_token.type}")

    def parse(self):
        return self.statements()

    def statements(self):
        statements = []
        while self.current_token.type != TokenType.EOF:
            statements.append(self.statement())
        return BlockNode(statements)

    def statement(self):
        if self.current_token.type == TokenType.LOVE:
            return self.variable_declaration()
        elif self.current_token.type == TokenType.HEART:
            return self.print_statement()
        elif self.current_token.type == TokenType.FEEL:
            return self.if_statement()
        elif self.current_token.type == TokenType.FOREVER:
            return self.while_statement()
        elif self.current_token.type == TokenType.CUDDLE:
            return self.for_statement()
        else:
            return self.expr()

    def variable_declaration(self):
        self.eat(TokenType.LOVE)
        var_name = self.current_token.value
        self.eat(TokenType.IDENTIFIER)
        self.eat(TokenType.ASSIGN)
        value = self.expr()
        self.eat(TokenType.SEMICOLON)
        return AssignNode(var_name, value)

    def print_statement(self):
        self.eat(TokenType.HEART)
        expr = self.expr()
        self.eat(TokenType.SEMICOLON)
        return PrintNode(expr)

    def if_statement(self):
        self.eat(TokenType.FEEL)
        condition = self.expr()
        self.eat(TokenType.KISS)
        kiss_block = self.block()
        hug_block = None
        if self.current_token.type == TokenType.HUG:
            self.eat(TokenType.HUG)
            hug_block = self.block()
        return IfNode(condition, kiss_block, hug_block)

    def while_statement(self):
        self.eat(TokenType.FOREVER)
        condition = self.expr()
        block = self.block()
        return WhileNode(condition, block)

    def block(self):
        self.eat(TokenType.LBRACE)
        statements = []
        while self.current_token.type != TokenType.RBRACE:
            statements.append(self.statement())
        self.eat(TokenType.RBRACE)
        return BlockNode(statements)

    def expr(self):
        node = self.comparison()
        return node

    def comparison(self):
        node = self.arithmetic()
        
        while self.current_token.type in [TokenType.EQ, TokenType.NEQ, 
                                        TokenType.LT, TokenType.GT, 
                                        TokenType.LTE, TokenType.GTE]:
            op = self.current_token
            self.eat(self.current_token.type)
            node = BinOpNode(node, op, self.arithmetic())
        return node

    def arithmetic(self):
        node = self.term()
        while self.current_token.type in [TokenType.PLUS, TokenType.MINUS]:
            op = self.current_token
            self.eat(self.current_token.type)
            node = BinOpNode(node, op, self.term())
        return node

    def term(self):
        node = self.factor()
        while self.current_token.type in [TokenType.MULTIPLY, TokenType.DIVIDE]:
            op = self.current_token
            self.eat(self.current_token.type)
            node = BinOpNode(node, op, self.factor())
        return node

    def factor(self):
        token = self.current_token
        if token.type == TokenType.NUMBER:
            self.eat(TokenType.NUMBER)
            return NumberNode(float(token.value))
        elif token.type == TokenType.STRING:
            self.eat(TokenType.STRING)
            return StringNode(token.value)
        elif token.type == TokenType.IDENTIFIER:
            self.eat(TokenType.IDENTIFIER)
            return VariableNode(token.value)
        elif token.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            node = self.expr()
            self.eat(TokenType.RPAREN)
            return node

    def for_statement(self):
        self.eat(TokenType.CUDDLE)
        var_name = self.current_token.value
        self.eat(TokenType.IDENTIFIER)
        self.eat(TokenType.IN)
        start = self.expr()
        self.eat(TokenType.TO)
        end = self.expr()
        block = self.block()
        return ForNode(var_name, start, end, block)
