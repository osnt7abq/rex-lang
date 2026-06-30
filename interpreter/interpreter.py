"""
🦖 Rex Programming Language
Interpreter
Version: 0.1 "Hatchling"
"""

from parser.ast import (
    VariableDeclaration,
    IntegerLiteral,
    StringLiteral,
    Identifier,
    PrintStatement,
)


class Interpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, program):
        for statement in program.statements:
            self.execute(statement)

    def execute(self, node):
        if isinstance(node, VariableDeclaration):
            value = self.evaluate(node.value)
            self.variables[node.name] = value

        elif isinstance(node, PrintStatement):
            print(self.evaluate(node.value))

        else:
            raise Exception(f"Unknown statement: {type(node)}")

    def evaluate(self, node):
        if isinstance(node, IntegerLiteral):
            return int(node.value)

        elif isinstance(node, StringLiteral):
            return node.value

        elif isinstance(node, Identifier):
            if node.name in self.variables:
                return self.variables[node.name]

            raise Exception(f"Undefined variable '{node.name}'")

        return None