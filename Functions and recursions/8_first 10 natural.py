def recursive_sum(h):
    if h<=1:
        return h
    else:
        return h + recursive_sum(h-1)
print(recursive_sum(5))
            
num=5
if num<0:
    print("enter a positive number")
else:
    print("the sum is",recursive_sum(num))
