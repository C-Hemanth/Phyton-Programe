#  1st  question
c={"18",18,18.2}                        #python takes as three different values
print(c)

#   2and question
s=set()
s.add(20)
s.add(20.1)
s.add(20.0)
s.add("20")
print(len(s))       #the values total are 4 but it shos 3 because 20 and 20.0 are same so it shows only 1 value for both of this
print(s)


#  3rd question
favlang={}
a=input("enter your favorite language hemanth\n")
b=input("enter your favorite language johnnydepp\n")
c=input("enter your favorite language galgadot\n")
d=input("enter your favorite language tomcruise\n")

favlang['hemanth']=a
favlang['johnnydepp']=b
favlang['galgadot']=c
favlang['tomcruise']=d
print(favlang)