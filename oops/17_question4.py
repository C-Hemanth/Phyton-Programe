class calculator:
    number='positive'
    def __init__(self,num):
        self.number=num

    def square(self):
        print(f"the square of {self.number} is {self.number **2}")


    def squareroot(self):
        print(f"the square root of {self.number} is {self.number **0.5}")


    def cube(self):
        print(f"the cube of {self.number} is {self.number **3}")

    @staticmethod
    def greet():
        print('this is my calculatore')

cal=calculator(9)
cal.greet()
cal.square()
cal.squareroot()
cal.cube()
