c={1,3,5,8,9}
# print(type(c))
# print(c)
c.add(7)
print(c)

#for an empty set
# d=set()
# d.add(4)
# d.add(6)
# d.add((3,4,6))                                      #we can add touples but we can't develop lists and dicts in this model
# # d.add({4:3})                                      #not useful for dicts
# print(type(d))
# print(d)

# print(len(c))                                           # n.o of numbers in the string
# c.remove(5)
# print(c)                                                   #removes the number what we have given
# print(c.pop())           # in set the pop does not take any value it takes randomly but in lists we give on;y one value for pop
# print(c)
# c.clear()                                       # clear the total set
# print(c)
print(c.union({2,4,3,5,6}))                             #add the new values to the given first set
print(c.intersection({5,6}))                        #print the values common in both the sets
