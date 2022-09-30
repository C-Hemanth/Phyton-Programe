# SINGLE INHERITRNCE
# base class
class employee:
    company='google'

    def details(self):
        print("tis is mine")

# derived or child class
class programmer(employee):
    programmer='hemanth'
    company='youtube'                 # if we write this then the programmer company will be executed not the employee details 

    def getdetails(self):
        print(f"the programmer name is,{self.programmer}")

    def details(self):                             #  if we dont write this then the employee details will be executed
        print("this was not mine")              # if we write this it will be executed but not the employee details

e=employee()
e.details()
p=programmer()
p.getdetails()
p.details()                         # the output of the before employee detais will be executed in the programmer
print(p.company)