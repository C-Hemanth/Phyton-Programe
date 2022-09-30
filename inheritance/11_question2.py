class animals:
    def shout(self):
        pass


class pets(animals):
    pass


class dog(pets):
    def __init__(self,sound):
        self.sound=sound
    
    def shout(self):
        print(f"the sound of dog is {self.sound}")


a=animals()
a.shout()
p=pets()
d=dog('bark')
d.shout()