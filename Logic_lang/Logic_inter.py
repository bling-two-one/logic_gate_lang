import Logic_lang.Logic_lang
import Logic_lang.Logic_Token as LT

Var_list = []

def AND_calc(result : list)  -> list:
        result_ = result
        temp_calc = ''
        temp_addr = result_.index(LT.Tokens_type.AND)
        for binary_ in range(len(result_[temp_addr + 1][1])) :
            temp_calc += str(int((int(result_[temp_addr + 1][1][binary_]) and int(result_[temp_addr - 1][1][binary_]))))
        result_[temp_addr] = [LT.Tokens_type.VALUE, temp_calc]
        del result_[temp_addr + 1]
        del result_[temp_addr - 1]

        return result_

def NAND_calc(result : list)  -> list:
        result_ = result
        temp_calc = ''
        temp_addr = result_.index(LT.Tokens_type.NAND)
        for binary_ in range(len(result_[temp_addr + 1][1])) :
            temp_calc += str(int(not (int(result_[temp_addr + 1][1][binary_]) and int(result_[temp_addr - 1][1][binary_]))))
        result_[temp_addr] = [LT.Tokens_type.VALUE, temp_calc]
        del result_[temp_addr + 1]
        del result_[temp_addr - 1]

        return result_

def OR_calc(result : list)  -> list:
        result_ = result
        temp_calc = ''
        temp_addr = result_.index(LT.Tokens_type.OR)
        for binary_ in range(len(result_[temp_addr + 1][1])) :
            temp_calc += str(int((int(result_[temp_addr + 1][1][binary_]) or int(result_[temp_addr - 1][1][binary_]))))
        result_[temp_addr] = [LT.Tokens_type.VALUE, temp_calc]
        del result_[temp_addr + 1]
        del result_[temp_addr - 1]

        return result_

def NOR_calc(result : list)  -> list:
        result_ = result
        temp_calc = ''
        temp_addr = result_.index(LT.Tokens_type.NOR)
        for binary_ in range(len(result_[temp_addr + 1][1])) :
            temp_calc += str(int(not (int(result_[temp_addr + 1][1][binary_]) or int(result_[temp_addr - 1][1][binary_]))))
        result_[temp_addr] = [LT.Tokens_type.VALUE, temp_calc]
        del result_[temp_addr + 1]
        del result_[temp_addr - 1]

        return result_

#def XOR_calc(result : list) -> list :
      

def interpreter(tokens_get : list) :

    result_ = tokens_get

    for token_analyze in result_ :
            if token_analyze == LT.Tokens_type.AND :
                result_ = AND_calc(result_)
                interpreter(result_)
                continue
            elif token_analyze == LT.Tokens_type.NAND :
                result_ = NAND_calc(result_)
                interpreter(result_)
                continue
            elif token_analyze == LT.Tokens_type.OR :
                result_ = OR_calc(result_)
                interpreter(result_)
                continue
            elif token_analyze == LT.Tokens_type.NOR :
                result_ = NOR_calc(result_)
                interpreter(result_)
                continue
    return result_
            
