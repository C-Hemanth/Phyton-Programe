def remove_and_split(string,word):                                  # we can use strip instaed of split
    newstring=string.replace(word, " ")
    return newstring.strip()
actor="     johnny depp is jack sparrow     "
print(remove_and_split(actor,"johnny depp"))                        # here we can use strip or split
print(actor)
print(actor.strip())                                                # strip make sthe statement to print without ang gap




