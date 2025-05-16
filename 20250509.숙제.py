import random
com = random.randint(1,100)
while (True) :
    user = int(input())
    if (com == user) :
        print("Correct!")
        break
    elif (com>user) :
        print("Up")
    else :
        print("Down")
