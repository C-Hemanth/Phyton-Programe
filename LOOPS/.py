


lower=int(input('enter the lower number'))
higher=int(input('enter the higher number'))

for i in range(lower, higher + 1):
    if i > 1:
        for h in range(2, i):
            if (i % h) == 0:
                break
        else:
            print(i)
            
h=int(input('enter the number'))
for i in range (2,h):
    if i>=1:
        for j in range(2,i):
            if (i%j) == 0:
                break
        else:
                print(i)

a=int(input('enter the number'))
# a=1
while a>i :
    print(i)
    a=a+1
    



    
    
