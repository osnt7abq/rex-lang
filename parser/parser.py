"""
🦖 Rex Programming Language
Parser
Version: 0.1 "Hatchling"
"""

from token_types import TokenType
from ast import Program, VariableDeclaration, IntegerLiteral, StringLiteral, Identifier


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def current(self):
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return None