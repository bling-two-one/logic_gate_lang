from enum import Enum, auto
import Logic_token_type
import Logic_Token as L_token
from typing import Optional

class Lexer:
    def __init__(self, source : str) -> None:
        self.source = source #소스 코드
        self.tokens = []      #파싱된 토큰
        self.start = 0       #시작
        self.current = 0     #끝
        self.line = 1        #라인
    
    def scan_token(self) -> None:
        ch = self.advance()
        
        if ch == 'AND' :
            self.add_token(Logic_token_type.AND)
        elif ch == 'OR' :
            self.add_token(Logic_token_type.OR)
        elif ch == 'XOR' :
            self.add_token(Logic_token_type.XOR)
        elif ch == 'NAND' :
            self.add_token(Logic_token_type.NAND)
        elif ch == 'NOR' :
            self.add_token(Logic_token_type.NOR)
        elif ch == 'n' :
            self.add_token(Logic_token_type.NOT)
        elif Lexer.is_digit(ch):
            while Lexer.is_digit(self.peek()):
                self.advance()

            if self.peek() == '.':
                self.advance()

                while Lexer.is_digit(self.peek()):
                    self.advance()

            self.add_token(Logic_token_type.Logic_TYPE.NUMBER, float(self.source[self.start: self.current]))
        
        
        if self.is_end():
            raise InvalidSyntaxError('Unterminated string')

        
        
    def is_end(self) -> bool:
        return self.current >= len(self.source)

    def advance(self) -> str:
        self.current += 1
        return self.source[self.current - 1]

    def peek(self) -> str:
        return None if self.is_end() else self.source[self.current]

    def match(self, target: str) -> bool:
        if self.is_end():
            return False
        if self.source[self.current] != target:
            return False

        self.current += 1
        return True

    def add_token(self, token_type: Logic_token_type.Logic_TYPE, literal: Optional[object] = None) -> None:
        self.token.append(L_token.Token(token_type, self.source[self.start: self.current], literal))
        
    def lex(self):
        while not self.is_end():
            self.start = self.current
            self.scan_token()

            self.tokens.append(L_token.Token(Logic_token_type.Logic_TYPE.EOF, ''))

            return self.tokens
        