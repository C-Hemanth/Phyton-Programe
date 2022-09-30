mydict={
  "johnny depp":'my inspiration',
 "gal gadot": "my smiley",
 'marks':[1,2,3],
  "tomcruise": "my fav",
  "anothername":{'hemu':'johnny'},
  5:63
}

print(mydict ["johnny depp"])
print(mydict['gal gadot'])

# mydict['marks']=[44.88]                              #if we want to change the marks the previous 
print(mydict ["marks"])
print(mydict['tomcruise'])
print(mydict["anothername"]['hemu'])        #amothername has two keys if we type the another key then the last key will be printed

print(mydict.keys())                                                             #prints the list of keys       OR
print(list(mydict.keys()))                               #we keep list to fet as lists it also used to print the list of keys
print(mydict.values())                                                         #the values of the given keywords will be printed
print(mydict.items())                                                         #prints the keywords with given values
updatedict={
  'leonardo':'dicaprio'

}
mydict.update(updatedict)                                                   # updates the list and add the new keyword with new value
print(mydict)

print(mydict.get("gal gadot"))                                              #give sthe same value for the keyword      OR
print(mydict["gal gadot"])                                # we camn write it as by removung get but it also prints same value
print(mydict.get("gal gadot2"))                                            # as gal gadot 2 name is not there it shows none      
print(mydict["gal gadot2"])                                                 # it shows an error so that the name id=s not there
