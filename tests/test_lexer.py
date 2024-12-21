import pytest
from src.lexer.lexer import Lexer
from src.lexer.tokens import TokenType, Token

def test_basic_tokens():
    source = 'love x = 42;'
    lexer = Lexer(source)
    
    tokens = []
    token = lexer.get_token()
    while token.type != TokenType.EOF:
        tokens.append(token)
        token = lexer.get_token()

    assert len(tokens) == 5
    assert tokens[0].type == TokenType.LOVE
    assert tokens[1].type == TokenType.IDENTIFIER
    assert tokens[2].type == TokenType.ASSIGN
    assert tokens[3].type == TokenType.NUMBER
    assert tokens[4].type == TokenType.SEMICOLON

def test_string_tokens():
    source = 'heart "Hello, Love!";'
    lexer = Lexer(source)
    
    tokens = []
    token = lexer.get_token()
    while token.type != TokenType.EOF:
        tokens.append(token)
        token = lexer.get_token()

    assert len(tokens) == 3
    assert tokens[0].type == TokenType.HEART
    assert tokens[1].type == TokenType.STRING
    assert tokens[1].value == "Hello, Love!"

def test_comparison_operators():
    source = 'feel x == 5 kiss { heart x; }'
    lexer = Lexer(source)
    
    tokens = []
    token = lexer.get_token()
    while token.type != TokenType.EOF:
        tokens.append(token)
        token = lexer.get_token()

    assert any(t.type == TokenType.EQ for t in tokens)
    assert any(t.type == TokenType.FEEL for t in tokens)
    assert any(t.type == TokenType.KISS for t in tokens)

def test_comments():
    source = 'xoxo this is a comment\nheart "Hello";'
    lexer = Lexer(source)
    
    tokens = []
    token = lexer.get_token()
    while token.type != TokenType.EOF:
        tokens.append(token)
        token = lexer.get_token()

    assert len(tokens) == 3  # heart, string, semicolon
    assert tokens[0].type == TokenType.HEART
