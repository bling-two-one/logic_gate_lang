import Logic_lang

if __name__ == '__main__' :
    lexer = Logic_lang.Lexer('AND')
    tokens = lexer.lex()
    
    print('\n'.join(map(str, tokens)))