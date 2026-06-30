"""
🦖 Rex Programming Language
Lexer
Version: 0.1 "Hatchling"
"""

from lexer.keywords import KEYWORDS
from lexer.token import Token
from lexer.token_types import TokenType


class Lexer:
    def __init__(self, source):
        self.source = source

    def tokenize(self):
        tokens = []

        i = 0
        while i < len(self.source):

            if self.source[i].isspace():
                i += 1
                continue

            # Read string
            if self.source[i] == '"':
                i += 1
                string = ""

                while i < len(self.source) and self.source[i] != '"':
                    string += self.source[i]
                    i += 1

                i += 1
                tokens.append(Token(TokenType.STRING, string))
                continue

            # Read normal word
            word = ""

            while i < len(self.source):
                if self.source[i].isspace() or self.source[i] == '"':
                    break

                word += self.source[i]
                i += 1

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

            elif word.isdigit():
                tokens.append(Token(TokenType.INTEGER, word))

            elif word:
                tokens.append(Token(TokenType.IDENTIFIER, word))

        return tokens
