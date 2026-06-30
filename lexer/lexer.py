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
        elif word.isdigit():
            tokens.append(Token(TokenType.INTEGER, word))
        else:
            tokens.append(Token(TokenType.IDENTIFIER, word))

    return tokens