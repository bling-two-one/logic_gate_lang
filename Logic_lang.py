from enum import Enum, auto
import Logic_token_type


class Lexer:
    def __init__(self, source : str) -> None:
        self.source = source #소스 코드
        self.token = []      #파싱된 토큰
        self.start = 0       #시작
        self.current = 0     #끝
        self.line = 1        #라인
    
    def add_Token(self, set_token) :
        self.token.append(set_token)
    
    def scan_token(self) -> None:
        ch = self.advance()
        
        if ch == Logic_token_type.AND :
            self.add_Token(Logic_token_type.AND)
        
        
        