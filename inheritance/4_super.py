class grandpa:
    country='india'
    def retire(self):
        # super().retire()
        print("his age is 60 years")

class father(grandpa):
    company='smuggles'
    # def retire(self,age):                 # we can write like this
    def retire(self):
        super().retire()
        # self.age=age
        print(f"i nwill retire after 50")

class son(father):
    business='pirates'

    def retire(self):
        super().retire()
        print("my aim to become a world famous")

# g=grandpa()
# print(g.retire())
f=father()
# f.age='88'
# f.retire('90')
# f.retire()
s=son()
# print(s.country)  # son has no instance called counttry it atykes from grandpa class
# g.retire()
# f.retire()
s.retire()
