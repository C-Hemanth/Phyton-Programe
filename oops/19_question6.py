class example:
    # def __init__(self,name):
    def __init__(hemu,name):     # instead of self we canm use any type of parameter but it makes copnfukse when u give same parameter and same name
        hemu.name=name
        # self.name=name
ex=example("hemu")
print(ex.name)