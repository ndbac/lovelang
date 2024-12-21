import pytest
from src.lexer.lexer import Lexer
from src.parser.parser import Parser
from src.interpreter.interpreter import Interpreter

def test_arithmetic():
    source = '''
    love x = 5;
    love y = 3;
    love z = x + y * 2;
    '''
    lexer = Lexer(source)
    parser = Parser(lexer)
    interpreter = Interpreter()
    
    ast = parser.parse()
    interpreter.visit(ast)
    
    assert interpreter.variables['z'] == 11

def test_comparison():
    source = '''
    love x = 5;
    love result = x > 3;
    '''
    lexer = Lexer(source)
    parser = Parser(lexer)
    interpreter = Interpreter()
    
    ast = parser.parse()
    interpreter.visit(ast)
    
    assert interpreter.variables['result'] == True

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
