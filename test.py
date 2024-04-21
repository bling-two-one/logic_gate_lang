import Logic_lang

s = Logic_lang.token_collect(['A=101001',
                              'B=110101',
                              '101010',
                              'AND',
                              '10100'])
while not s.is_end() :
    s.scan()
    
print(s.tokens)