from random import randint
from random import choice
# from eval import calc
import eval
x = randint(1,10)
y = randint(1,10)

op = choice(['+','-','*','/'])

error = [-1 ,0 , 1]
err = choice(error)

playing = True
count = 5
while playing and 0<count <6 :
    count -= 1
    res = 0
    res = eval.calc(x, y, op)

    display_res = res + err

    print("{} {} {} = {}".format(x,op,y,display_res) )

    ans = input("(Y/N) ").upper()
    if res == display_res and ans == "Y":
        print("True")
        playing = False
    elif res == display_res and ans == "N":
        print("Lose")
        continue
    elif res != display_res and ans == "Y":
        print("Lose")
        continue
    elif res != display_res and ans == "N":
        print("True")
        playing = False
    
    if count == 0 :
        break

