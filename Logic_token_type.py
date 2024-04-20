from enum import Enum, auto

class Logic_TYPE(Enum) :
    EQUAL = auto() # =
    
    IDENTIFIER = auto() # var, func name, ([a-zA-Z][a-zA-Z0-9]*)
    NUMBER = auto() # binary num (0:1)
    
    EOF = auto() # End Of File
    
    #keyword
    FUN = 'func'
    VAR = 'value'
    
    AND = 'AND'
    OR = 'OR'
    XOR = 'XOR'    
    NAND = 'NAND'
    NOR = 'NOR'
    NOT = 'n'
    
    @classmethod
    def has_value(cls, value) :
        return any(value == item.value for item in cls)