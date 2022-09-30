# a=2
# b=4
# c=3


def greatest(a,b,c):
    if(a>b):
        if (a>c):
            return c
        else:
            return a
    else:
        if(b>c):
            return b
        else:
            return c      
# m= greatest(a,b,c)
m= greatest(44,55,66.7)
print("the great value is " + str(m))



a=55
b=77
c=34
def max(a,b,c):
    if(a>b):
        return(a)
    elif(a<b):
        return(b)
    elif(a>c):
        return(a)
    elif(a<c):
        return(c)
    elif(b>c):
        return(b)
    else:
        return(c)
h=max(a,b,c)
print("the max is"  +  str(h))




