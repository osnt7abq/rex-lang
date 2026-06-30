"""
🦖 Rex Programming Language
Interpreter
Version: 0.1 "Hatchling"
"""

from parser.ast import (
    Program,
    VariableDeclaration,
    IntegerLiteral,
    StringLiteral,
    Identifier,
)


class Interpreter:
    def __init__(self):
        self.variables = {}

    def execute(self, program):
        for statement in program.statements:
            self.visit(statement)

    def visit(self, node):
        if isinstance(node, VariableDeclaration):
            self.visit_variable_declaration(node)

    def visit_variable_declaration(self, node):
        value = self.evaluate(node.value)
        self.variables[node.name] = value

    def evaluate(self, node):
        if isinstance(node, IntegerLiteral):
            return int(node.value)

        if isinstance(node, StringLiteral):
            return node.value

        if isinstance(node, Identifier):
            return self.variables.get(node.name)

        return None