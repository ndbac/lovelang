import sys
from src.lexer.lexer import Lexer
from src.parser.parser import Parser
from src.interpreter.interpreter import Interpreter

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <filename>")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as file:
            source = file.read()

        print("💖 Welcome to LoveLang! 💖")
        print("Compiling with love...")

        lexer = Lexer(source)
        parser = Parser(lexer)
        interpreter = Interpreter()

        ast = parser.parse()
        result = interpreter.visit(ast)

        print("✨ Program finished with love! ✨")
        return result

    except FileNotFoundError:
        print(f"💔 Error: File '{sys.argv[1]}' not found")
    except Exception as e:
        print(f"💔 Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
