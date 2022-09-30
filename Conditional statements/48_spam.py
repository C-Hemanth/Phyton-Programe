text=input("enter the text\n")

if("you will get alot of money" in text):
    spam=True
elif("play this you get a lot" in text):
    spam=True    
elif("tell your bank account" in text):
    sapm=True
else:
    spam=False        


if(spam):
    print("this text is spam")    
else:
    print("this text is not spam")    