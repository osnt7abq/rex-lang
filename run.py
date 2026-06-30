"""
🦖 Rex Programming Language
Runner
Version: 0.1 "Hatchling"
"""

from lexer.lexer import Lexer
from parser.parser import Parser


def main():
    with open("examples/hello.rex", "r") as file:
        code = file.read()

    lexer = Lexer(code)
    tokens = lexer.tokenize()

    print("=== TOKENS ===")
    for token in tokens:
        print(token)

    parser = Parser(tokens)
    program = parser.parse()

interpreter = Interpreter()
interpreter.execute(program)

print("\n=== VARIABLES ===")
print(interpreter.variables)

    print("\n=== AST ===")
    print(program)


if __name__ == "__main__":
    main()