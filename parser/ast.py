"""
🦖 Rex Programming Language
AST Nodes
Version: 0.1 "Hatchling"
"""


class Program:
    def __init__(self):
        self.statements = []


class VariableDeclaration:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class IntegerLiteral:
    def __init__(self, value):
        self.value = value


class StringLiteral:
    def __init__(self, value):
        self.value = value


class Identifier:
    def __init__(self, name):
        self.name = name

class PrintStatement:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"PrintStatement({self.value})"