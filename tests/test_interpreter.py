import pytest
from src.lexer.lexer import Lexer
from src.parser.parser import Parser
from src.interpreter.interpreter import Interpreter

def test_arithmetic_and_comparison():
    source = '''
    love x = 5;
    love y = 3;
    love sum = x + y;
    love product = x * y;
    love is_greater = x > y;
    '''
    lexer = Lexer(source)
    parser = Parser(lexer)
    interpreter = Interpreter()
    
    ast = parser.parse()
    interpreter.visit(ast)

    assert interpreter.variables['sum'] == 8
    assert interpreter.variables['product'] == 15
    assert interpreter.variables['is_greater'] == True

def test_if_statement():
    source = '''
    love x = 10;
    feel x > 5 kiss {
        love result = "greater";
    } hug {
        love result = "lesser";
    }
    '''
    lexer = Lexer(source)
    parser = Parser(lexer)
    interpreter = Interpreter()
    
    ast = parser.parse()
    interpreter.visit(ast)
    
    assert interpreter.variables['result'] == "greater"

def test_while_loop():
    source = '''
    love counter = 0;
    love sum = 0;
    forever counter < 5 {
        love sum = sum + counter;
        love counter = counter + 1;
    }
    '''
    lexer = Lexer(source)
    parser = Parser(lexer)
    interpreter = Interpreter()
    
    ast = parser.parse()
    interpreter.visit(ast)
    
    assert interpreter.variables['sum'] == 10
    assert interpreter.variables['counter'] == 5

def test_string_concatenation():
    source = '''
    love greeting = "Hello";
    love name = "World";
    love message = greeting + " " + name;
    '''
    lexer = Lexer(source)
    parser = Parser(lexer)
    interpreter = Interpreter()
    
    ast = parser.parse()
    interpreter.visit(ast)
    
    assert interpreter.variables['message'] == "Hello World"

def test_for_loop():
    source = '''
    love sum = 0;
    cuddle i in 0 to 5 {
        love sum = sum + i;
    }
    '''
    lexer = Lexer(source)
    parser = Parser(lexer)
    interpreter = Interpreter()
    
    ast = parser.parse()
    interpreter.visit(ast)
    
    assert interpreter.variables['sum'] == 10  # 0 + 1 + 2 + 3 + 4
