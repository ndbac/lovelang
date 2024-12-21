import pytest
from src.lexer.lexer import Lexer
from src.parser.parser import Parser
from src.parser.ast import *

def test_variable_declaration():
    source = 'love x = 42;'
    lexer = Lexer(source)
    parser = Parser(lexer)
    ast = parser.parse()

    assert isinstance(ast, BlockNode)
    assert len(ast.statements) == 1
    assert isinstance(ast.statements[0], AssignNode)
    assert ast.statements[0].name == 'x'

def test_print_statement():
    source = 'heart "Hello, World!";'
    lexer = Lexer(source)
    parser = Parser(lexer)
    ast = parser.parse()

    assert isinstance(ast.statements[0], PrintNode)
    assert isinstance(ast.statements[0].expr, StringNode)

def test_if_statement():
    source = '''
    feel x > 5 kiss {
        heart "Greater";
    } hug {
        heart "Lesser";
    }
    '''
    lexer = Lexer(source)
    parser = Parser(lexer)
    ast = parser.parse()

    assert isinstance(ast.statements[0], IfNode)
    assert ast.statements[0].hug_block is not None

def test_while_loop():
    source = '''
    forever x < 5 {
        heart x;
        love x = x + 1;
    }
    '''
    lexer = Lexer(source)
    parser = Parser(lexer)
    ast = parser.parse()

    assert isinstance(ast.statements[0], WhileNode)
