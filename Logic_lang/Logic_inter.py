import Logic_lang.Logic_lang
import Logic_lang.Logic_Token as LT

def interpreter(tokes_get : list) :

    result_ = tokes_get

    for token_analyze in result_ :
        if token_analyze == LT.Tokens_type.AND :
            temp_addr = result_.index(LT.Tokens_type.AND)
            result_[temp_addr] = result_[temp_addr - 1] and result_[temp_addr + 1]
            del result_[temp_addr - 1]
            del result_[temp_addr + 1]
            continue

    return result_
            
