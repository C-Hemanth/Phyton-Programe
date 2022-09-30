a=int(input("enter your number : "))
b=int(input("enter your number 1 : "))
c=int(input("enter your number 2 : "))
d=int(input("enter your number 3 : "))


if(a>b):
    h1=a
else:
    h1=b

if(c>d):
    h2=c
else:
    h2=d

if(h1>h2):
    print(str(h1) + " is large" )
    # print(h1)
else:
    print(str(h2) + "is large" )        
    # print(h2)