
from Logic_lang.Logic_Token import Tokens_type
import re
import Logic_lang.Logic_inter as LT

is_shift = re.compile('>{2}|<{2}[0-8]')

class token_collect :
    def __init__(self, source : list) -> None:
        self.source = source
        self.tokens = []
        self.current = 0
        self.start = 0
        self.end = len(source)
    
    def add_token(self, token : Tokens_type) :
        self.tokens.append(token)
    
    def next_line(self) :
        self.current += 1

    def is_end(self) :
        if self.current == self.end :
            return True
        elif self.current < self.end :
            return False    
        
    def scan(self) :
        code = self.source[self.current]

        if code == 'AND' :
            self.add_token(Tokens_type.AND)
            self.next_line()
            
        elif code == 'OR' :
            self.add_token(Tokens_type.OR)
            self.next_line()
            
        elif code == 'XOR' :
            self.add_token(Tokens_type.XOR)
            self.next_line()
            
        elif code == 'NAND' :
            self.add_token(Tokens_type.NAND)
            self.next_line()
            
        elif code == 'NOR' :
            self.add_token(Tokens_type.NOR)
            self.next_line()
            
        elif code == 'NOT' :
            self.add_token(Tokens_type.NOT)
            self.next_line()
            
        elif bool(is_shift.match(code)) :
            if bool(re.match('<{2}[0-8]', code)) :
                self.add_token([Tokens_type.L_SHIFT, int(code[-1])])
                self.next_line()
                
            elif bool(re.match('>{2}[0-8]', code)) :
                self.add_token([Tokens_type.R_SHIFT,int(code[-1])])
                self.next_line()
                
        elif bool(re.match('[0-1]{1,8}', code)) :
            self.add_token([Tokens_type.VALUE, int(code)])
            self.next_line()
        
        elif bool(re.match('^=[a-zA-Z][0-9]*', code)) :
            self.add_token([Tokens_type.CALCUL_EQUAL, code[1:]])
            self.next_line()
            
        elif bool(re.match('^[^0-9][a-zA-Z0-9]*=[0-1]{1,8}$', code)) :
            self.add_token([Tokens_type.ASSIGN_EQUAL, code.split('=')[0], code.split('=')[1]])
            self.next_line()
        

def run(source_file : str) -> list :
    file = open(source_file, 'r')
    
    codes = file.readlines()
    codes = [v.strip() for v in codes if v.strip()]

    code_analyze = token_collect(codes)
    
    for i in codes :
            code_analyze.scan()

    return LT.interpreter(code_analyze.tokens)
    
