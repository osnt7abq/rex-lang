"""
🦖 Rex Programming Language
Parser
Version: 0.1 "Hatchling"
"""

from lexer.token_types import TokenType
from parser.ast import (
    Program,
    VariableDeclaration,
    IntegerLiteral,
    StringLiteral,
    Identifier,
    PrintStatement,
)


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def current(self):
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return None

    def advance(self):
        self.position += 1
        return self.current()

    def match(self, token_type):
        token = self.current()

        if token and token.type == token_type:
            self.advance()
            return token

        return None

    def parse(self):
        program = Program()

        while self.current() is not None:
            statement = self.parse_statement()

            if statement:
                program.statements.append(statement)
            else:
                self.advance()

        return program

    def parse_statement(self):
        token = self.current()

        if token and token.type == TokenType.KEYWORD:
            if token.value == "let":
                return self.parse_variable_declaration()

        return None

    def parse_variable_declaration(self):
        self.advance()  # Skip 'let'

        name = self.match(TokenType.IDENTIFIER)

        self.match(TokenType.ASSIGN)

        value = self.current()

        if value.type == TokenType.INTEGER:
            value = IntegerLiteral(value.value)
        elif value.type == TokenType.STRING:
            value = StringLiteral(value.value)
        else:
            value = Identifier(value.value)

        self.advance()

        return VariableDeclaration(name.value, value)