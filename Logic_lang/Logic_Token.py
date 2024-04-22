from enum import Enum, auto
from typing import Optional

class Tokens_type(Enum) :
    AND = auto()
    OR = auto()
    XOR = auto()
    NAND = auto()
    NOR = auto()
    NOT = auto()
    
    VALUE = auto()
    
    R_SHIFT = auto()
    L_SHIFT = auto()
    
    ASSIGN_EQUAL = auto()
    CALCUL_EQUAL = auto()
    
    IDENTIFIER = auto()
    
    EOF = auto()

class Token:
    def __init__(self, token_type: Tokens_type):
        self.type = token_type
        