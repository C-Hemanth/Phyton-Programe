class grandpa:
    country='india'

    def __init__(self):
        print("hello")
    def retire(self):
        print("his age is 60 years")
    def age(self):
        print("his age is 60 years")

class father(grandpa):
    company='smuggles'
    # def retire(self,age):                 # we can write like this
    def retire(self):
        # self.age=age
        print(f"i nwill retire after{self.age}")

class son(father):
    business='pirates'

    def retire(self):
        print("my aim to become a world famous")

# g=grandpa()
# print(g.retire())
# f=father()
# f.age='88'
# f.retire()
# g.retire()
s=son()
s.retire()
s.age()
# print(s.country)  # son has no instance called counttry it atykes from grandpa class
