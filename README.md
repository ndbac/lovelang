# 💝 LoveLang

LoveLang is a cute and expressive programming language designed to make coding more lovable! It features a friendly syntax that makes programming feel like writing love letters to your computer.

## 🌟 Features

### Lovely Syntax
- Variables are declared with `love`
- Print with `heart`
- Conditionals use `feel`-`kiss`-`hug`
- While loops use `forever`
- For loops use `cuddle`
- Comments start with `xoxo`

### Example
```lovelang
xoxo This is a lovely program!

love message = "Hello, lovely world!";
heart message;

xoxo If statement example
love number = 42;
feel number > 20 kiss {
    heart "That's a big lovely number!";
} hug {
    heart "That's a cute small number!";
}

xoxo While loop example
love counter = 0;
forever counter < 5 {
    heart "Counting with love:";
    heart counter;
    love counter = counter + 1;
}

xoxo For loop example
love sum = 0;
cuddle i in 0 to 5 {
    love sum = sum + i;
    heart "Current sum is:";
    heart sum;
}
```

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/ndbac/lovelang.git
cd lovelang
```

2. Set up Python environment (Python 3.7+ required):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 💫 Usage

Run a LoveLang program:
```bash
PYTHONPATH=. python src/main.py examples/hello_world.love
```

## 📖 Language Reference

### Keywords
- `love` - Variable declaration
- `heart` - Print statement
- `feel` - If condition
- `kiss` - Then block
- `hug` - Else block
- `forever` - While loop
- `cuddle` - For loop
- `in` - Used in for loops
- `to` - Range specifier in for loops
- `xoxo` - Comments

### Operators
- Arithmetic: `+`, `-`, `*`, `/`
- Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Assignment: `=`

### Data Types
- Numbers (integers and floats)
- Strings (enclosed in double quotes)
- Boolean expressions (comparison results)

## 📁 Project Structure

```
lovelang/
├── src/
│   ├── main.py
│   ├── lexer/
│   │   ├── lexer.py
│   │   └── tokens.py
│   ├── parser/
│   │   ├── parser.py
│   │   └── ast.py
│   └── interpreter/
│       └── interpreter.py
├── tests/
│   ├── test_lexer.py
│   ├── test_parser.py
│   └── test_interpreter.py
├── examples/
│   └── hello_world.love
├── requirements.txt
└── README.md
```

## 🧪 Testing

Run the test suite:
```bash
PYTHONPATH=. pytest tests/
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 💕 Acknowledgments

- Inspired by the desire to make programming more approachable and fun
- Thanks to all contributors who help make LoveLang more lovely

## 🐛 Bug Reports

Found a bug? Please open an issue with:
- Description of the problem
- Code sample that reproduces the issue
- Expected vs actual behavior

Let's make programming lovely together! 💝