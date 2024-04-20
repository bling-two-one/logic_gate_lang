from Logic_Token import Token, Tokens_type
from typing import Optional, List

#코드를 토큰 단위로 스캔
class Logic_Lexer :
    def __init__(self, source : str) -> None:
        self.source = source    # 소스 코드
        self.tokens = []        # 파싱된 토큰
        self.start = 0			# 토큰의 시작
        self.current = 0		# 토큰의 끝
        self.line = 1			# 라인
    
    def lex(self) -> List[Token]:
        while not self.is_end():
            self.start = self.current
            self.scan_tokens()

        self.tokens.append(Token(Tokens_type.EOF, ''))

        return self.tokens
    
    def scan_tokens(self) :
        ch = self.advance()
        
        if ch == 'AND' :
            self.add_token(Tokens_type.AND)
        elif ch == 'OR' :
            self.add_token(Tokens_type.OR)
        elif ch == 'XOR' :
            self.add_token(Tokens_type.XOR)
        elif ch == 'NAND' :
            self.add_token(Tokens_type.NAND)
        elif ch == 'NOR' :
            self.add_token(Tokens_type.NOR)
        elif ch == 'NOT' :
            self.add_token(Tokens_type.NOT)
        
    def add_token(self) :
        self.tokens.append(Token(Tokens_type, self.source[self.start: self.current]))
    
    def is_end(self) -> bool:
        return self.current >= len(self.source)
    
    def advance(self) -> str :
        self.current += 1
        return self.source[self.current - 1]
    
    def run(code: str) -> None:
        lexer = Logic_Lexer(code)

        lexer.tokens = lexer.lex()
        print(lexer)

    @staticmethod
    def run_file(filename: str) -> None:
        with open(filename, 'r') as f:
                Logic_Lexer.run(f.read())
