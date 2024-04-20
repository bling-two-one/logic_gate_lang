from Logic_lang import Logic_Lexer

lexer = Logic_Lexer('OR')

tokens = lexer.lex()

print('\n'.join(map(str, tokens)))