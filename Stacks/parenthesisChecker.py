
from Stacks import Stack1

def par_checker(paren_list):
    s=Stack1()

    balanced=True
    index=0

    while index<len(paren_list) and balanced:
        symbol=paren_list[index]
        if symbol=='(':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced=False
            else:
                s.pop()
        index=index+1

    if balanced and s.is_empty():
        return True
    else:
        return False
    


print(par_checker('((()))'))