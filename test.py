import Logic_lang

s = Logic_lang.token_collect(['AND','OR','XOR','NAND','NOR','NOT','1','101001','>>2','<<4','test=1010','=test2'])
while not s.is_end() :
    s.scan()
    
print(s.tokens)