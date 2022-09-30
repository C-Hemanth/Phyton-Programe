import random
randomnum = random.randint(1,54)
print(randomnum)
userguess = None
guesses = 0


while(userguess != randomnum):
    userguess = int(input("enter the number"))
    guesses +=1
    if (userguess == randomnum):
        print('u r right')
    else:
        if userguess>randomnum:
            print('please give a smaller number')
        else:
            print('please give a larger number')


print(f"the number of guesses are : {guesses}")