from random import *
from eval import calc


def generate_quiz():
    x = randint(1,10)
    y = randint(1,10)

    op = choice(['+','-','*','/'])

    res = calc(x, y, op)

    error = choice([-1 , 1])

    display_res = res + error

    return[x,y,op,display_res]

    # Hint: Return [x, y, op, display_res]
    
def check_answer(x, y, op, display_res, user_choice):
    true_res = calc(x,y,op )
    if true_res == display_res:
        return user_choice
        # if user_choice: #== True: 
        #     return True
        # else:
        #     return False
    else:
        return not user_choice
        # if user_choice: #== True:
        #     return False
        # else:
        #     return True
