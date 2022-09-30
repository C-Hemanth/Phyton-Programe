class Employ:
    company = 'pirates'
    salary='100'     
    #if we denote salary to the employees then it does not take it because it preferences class atribute than assignment atribute
hemanth=Employ()
freind=Employ()
#  Create instance attributes for both the objects
# if we comment out these two salries then the salary above will be printed


# hemanth.salary='563'
# freind.salary='546'

# If we give salary to only to one employee printed for that employee then the other employ sal will be taken as the above sal

hemanth.salary='005'
print(hemanth.salary)
print(freind.salary)
# print(hemanth.address)                # Throws an error because address is not aviolable