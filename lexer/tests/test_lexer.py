"""
🦖 Rex Programming Language
Lexer Test
Version: 0.1 "Hatchling"
"""

from lexer.lexer import Lexer


def test_lexer():
    code = "let age 18"

    lexer = Lexer(code)
    tokens = lexer.tokenize()

    for token in tokens:
        print(token)


if __name__ == "__main__":
    test_lexer()