sub1=int(input("enter your first sub  marks \n"))
sub2=int(input("enter your second sub marks \n"))
sub3=int(input("enter your third sub marks \n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("you have failed because you got less than 33 percent in each subject")    
elif(sub1+sub2+sub3)/3<40:
    print("you have beeen failed because you got less pecentage of total")   
else:                                                                          #OR          #elif(sub1>33 or sub2>33 or sub3>33):
    print("congrats,you have been passed")                                              # we can use else or elif