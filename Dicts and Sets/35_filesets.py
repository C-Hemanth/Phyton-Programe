c={1,3,5,8,9}
print(type(c))
print(c)
c.add(7)
print(c)

#for an empty set
d=set()
d.add(4)
d.add(6)
d.add((3,4,6))                                    #we can add touples but we can't develop lists and dicts in this model
# d.add({4:3})                                      #not useful for dicts
print(type(d))
print(d)