# h=7
# product=1
# for i in range(1,h+1):
#     product=product*i
# print(product)


# BY USING DEF

def fact_iter(h):
    product =1
    for i in range(h):
        product = product*(i+1)
    return (product)


f=(fact_iter(5))
print(f)



def factorial_recursive(h):
    if h==0 or h==1:
        return 1
    # if h==2:
        # return 2
    # else:                                                     # we can write else or leave writing else
    return h*factorial_recursive(h-1)
print(factorial_recursive(5))
           
    




