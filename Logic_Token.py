from enum import Enum, auto
from typing import Optional

class Tokens_type(Enum) :
    AND = auto()
    OR = auto()
    XOR = auto()
    NAND = auto()
    NOR = auto()
    NOT = auto()
    
    SHIFT = auto()
    
    IDENTIFIER = auto()
    EQUAL = auto()
    
    NUMBER = auto()
    
    EOF = auto()
    
    @classmethod
    def has_value(cls, value) :
        return any(value == item.value for item in cls)

class Token:
    def __init__(self, token_type: Tokens_type, lexeme: str):
        self.type = token_type
        self.lexeme = lexeme

    def __str__(self):
        return f'{self.type.name} {self.lexeme}'
        