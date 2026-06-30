"""
🦖 Rex Programming Language
Token Types
Version: 0.1 "Hatchling"
"""

class TokenType:
    # Keywords
    KEYWORD = "KEYWORD"

    # Identifiers
    IDENTIFIER = "IDENTIFIER"

    # Literals
    STRING = "STRING"
    INTEGER = "INTEGER"
    FLOAT = "FLOAT"

    # Operators
    ASSIGN = "="
    PLUS = "+"
    MINUS = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    MODULO = "%"

    # Comparison
    EQUAL = "=="
    NOT_EQUAL = "!="
    GREATER = ">"
    LESS = "<"
    GREATER_EQUAL = ">="
    LESS_EQUAL = "<="

    # Delimiters
    LPAREN = "("
    RPAREN = ")"
    LBRACE = "{"
    RBRACE = "}"
    LBRACKET = "["
    RBRACKET = "]"

    COMMA = ","
    DOT = "."
    COLON = ":"

    EOF = "EOF"