"""
🦖 Rex Programming Language
Scanner
Version: 0.1 "Hatchling"
"""

class Scanner:
    def __init__(self, source):
        self.source = source
        self.position = 0

    def current_char(self):
        if self.position >= len(self.source):
            return None
        return self.source[self.position]

    def advance(self):
        self.position += 1