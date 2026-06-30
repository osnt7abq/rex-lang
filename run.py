"""
🦖 Rex Programming Language
Runner
Version: 0.1 "Hatchling"
"""

from lexer.lexer import Lexer
from parser.parser import Parser
from interpreter.interpreter import Interpreter


def main():
    with open("examples/hello.rex", "r") as file:
        code = file.read()

    # Lexer
    lexer = Lexer(code)
    tokens = lexer.tokenize()

    print("=== TOKENS ===")
    for token in tokens:
        print(token)

    # Parser
    parser = Parser(tokens)
    program = parser.parse()

    print("\n=== AST ===")
    print(program)

    # Interpreter
    interpreter = Interpreter()
    interpreter.execute(program)

    print("\n=== VARIABLES ===")
    print(interpreter.variables)


if __name__ == "__main__":
    main() 