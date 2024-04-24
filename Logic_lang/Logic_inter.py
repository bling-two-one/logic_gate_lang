import Logic_lang.Logic_lang
import Logic_lang.Logic_Token as LT

Var_list = dict()

def AND_calc(token_analyze, result : list)  -> list:
        result_ = result
        if token_analyze == LT.Tokens_type.AND :
            temp_calc = ''
            temp_addr = result_.index(LT.Tokens_type.AND)
            for binary_ in range(len(result_[temp_addr + 1][1])) :
                 temp_calc += str(int((int(result_[temp_addr + 1][1][binary_]) and int(result_[temp_addr - 1][1][binary_]))))
            result_[temp_addr] = temp_calc
            del result_[temp_addr + 1]
            del result_[temp_addr - 1]

        return result_

def NAND_calc(token_analyze, result : list)  -> list:
        result_ = result
        if token_analyze == LT.Tokens_type.NAND :
            temp_addr = result_.index(LT.Tokens_type.AND)
            for binary_ in range(len(result_[temp_addr + 1][1])) :
                 temp_calc += str(int(not (int(result_[temp_addr + 1][1][binary_]) and int(result_[temp_addr - 1][1][binary_]))))
            result_[temp_addr] = temp_calc
            del result_[temp_addr + 1]
            del result_[temp_addr - 1]

        return result_

def OR_calc(token_analyze, result : list)  -> list:
        result_ = result
        if token_analyze == LT.Tokens_type.OR :
            temp_calc = ''
            temp_addr = result_.index(LT.Tokens_type.OR)
            for binary_ in range(len(result_[temp_addr + 1][1])) :
                 temp_calc += str(int((int(result_[temp_addr + 1][1][binary_]) or int(result_[temp_addr - 1][1][binary_]))))
            result_[temp_addr] = temp_calc
            del result_[temp_addr + 1]
            del result_[temp_addr - 1]

        return result_

def AND_calc(token_analyze, result : list)  -> list:
        result_ = result
        if token_analyze == LT.Tokens_type.AND :
            temp_calc = ''
            temp_addr = result_.index(LT.Tokens_type.AND)
            for binary_ in range(len(result_[temp_addr + 1][1])) :
                 temp_calc += str(int(not (int(result_[temp_addr + 1][1][binary_]) or int(result_[temp_addr - 1][1][binary_]))))
            result_[temp_addr] = temp_calc
            del result_[temp_addr + 1]
            del result_[temp_addr - 1]

        return result_

def interpreter(tokens_get : list) :

    result_ = tokens_get

    for token_analyze in result_ :
            if token_analyze == LT.Tokens_type.AND :
                 result_ = AND_calc(token_analyze, result_)
            if token_analyze == LT.Tokens_type.OR :
                result_ = OR_calc(token_analyze, result_)

    return result_
            
