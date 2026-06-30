"""
🦖 Rex Programming Language
Lexer
Version: 0.1 "Hatchling"
"""

from keywords import KEYWORDS
from token import Token
from token_types import TokenType


class Lexer:
    def __init__(self, source):
        self.words = source.split()

    def tokenize(self):
        tokens = []

        for word in self.words:
            if word in KEYWORDS:
                tokens.append(Token(TokenType.KEYWORD, word))
            elif word == "=":
                tokens.append(Token(TokenType.ASSIGN, word))
            elif word == "+":
                tokens.append(Token(TokenType.PLUS, word))
            elif word == "-":
                tokens.append(Token(TokenType.MINUS, word))
            elif word == "*":
                tokens.append(Token(TokenType.MULTIPLY, word))
            elif word == "/":
                tokens.append(Token(TokenType.DIVIDE, word))
            elif word == "%":
                tokens.append(Token(TokenType.MODULO, word))
elif word == "==":
    tokens.append(Token(TokenType.EQUAL, word))
elif word == "!=":
    tokens.append(Token(TokenType.NOT_EQUAL, word))
elif word == ">":
    tokens.append(Token(TokenType.GREATER, word))
elif word == "<":
    tokens.append(Token(TokenType.LESS, word))
elif word == ">=":
    tokens.append(Token(TokenType.GREATER_EQUAL, word))
elif word == "<=":
    tokens.append(Token(TokenType.LESS_EQUAL, word))
            elif word.startswith('"') and word.endswith('"'):
                tokens.append(Token(TokenType.STRING, word[1:-1]))
            elif word.isdigit():
                tokens.append(Token(TokenType.INTEGER, word))
            else:
                tokens.append(Token(TokenType.IDENTIFIER, word))

        return tokens