"""
🦖 Rex Programming Language
Runner
Version: 0.1 "Hatchling"
"""

from lexer.lexer import Lexer
from parser.parser import Parser


def main():
    code = 'let name = "Osant"'

    lexer = Lexer(code)
    tokens = lexer.tokenize()

    print("=== TOKENS ===")
    for token in tokens:
        print(token)

    parser = Parser(tokens)
    ast = parser.parse()

    print("\n=== AST ===")
    print(ast)


if __name__ == "__main__":
    main()