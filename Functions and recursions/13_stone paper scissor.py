import random

def game(comp,me):
    if comp==me:
        return None
    elif comp=='s':
        if me=='p':
            return True
        elif me=='c':
            return False

    elif comp == 'p':
        if me == 's':
            return False
        elif me=='c':
            return True
    elif comp == 'c':
        if me == 's':
            return True
        elif me == 'p':
            return False               

print("comp turn: stone(s),paper(p),scissor(c)")
randno=random.randint(1,3)                                              # it prints randomly number

if randno==1:
    comp = 's'
elif randno == 2:
    comp = 'p'
elif randno == 3:
    comp = 'c'
    
me=input("your turn : stone(s),paper(p),scissor(c)?")
a= game(comp,me) 
print(f"computer chose  {comp}")
print(f"me chose{me}")

if a == None:
    print("the game is tie!")
elif a:
    print("you win!")
else:
    print("you lose !")        


