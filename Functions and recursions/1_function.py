def percent(marks):                                # For long lists we can use def function 
    # return((sum(marks)/400)*100)                    # return makes the below statements easy  (or)
    p=(sum(marks)/400)*100
    return p


marks=[33,44,55,66]
# percentage=(sum(marks)/400)*100                      # this is normal statement as we can use for if we haves ome statements
percentage=percent(marks)                             # by return this may be easy to print

marks3=[33,48,588,60]                                    # we can use ()  OR  []
# percentage3=(sum(marks)/400)*100
percentage3=percent(marks)

print(percentage,percentage3)



# def player(name):
    # a=input("enter user")