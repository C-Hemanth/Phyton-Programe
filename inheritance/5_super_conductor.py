class grandpa:
    country='india'

    def __init__(self):
        print('i become old')

    def retire(self):
        # super().retire()
        print("his age is 60 years")

class father(grandpa):
    company='smuggles'

    def __init__(self):
        super().__init__()
        print('i will retire soon')


    # def retire(self,age):                 # we can write like this
    def retire(self):
        super().retire()
        # self.age=age
        print(f"i nwill retire after 50")

class son(father):
    business='pirates'

    def __init__(self):
        super().__init__()                          # in constructor method we usew this init with super
        print("i am entering")

    def retire(self):
        super().retire()                            # this also gives the same output as constructor method
        print(f"my aim to become a world famous")

# g=grandpa()
# print(g.retire())
# f=father()
# f.age='88'
# f.retire('90')
# f.retire()
s=son()
# print(s.country)  # son has no instance called counttry it atykes from grandpa class
# g.retire()
# f.retire()
s.retire()                    # if we use constructor method then we dont need to be use this statements
