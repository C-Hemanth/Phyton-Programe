#  formula== (a+bi)(c+di) = (ac-bd) + (ad+bc)i

class complex:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i

    def __add__(self,c):
        return complex(self.real + c.real,self.imaginary + c.imaginary)
    
    
    def __mul__(self,c):
        mulreal = self.real*c.real-self.imaginary*c.imaginary
        mulimaginary = self.real*c.real+self.imaginary*c.imaginary
        return complex(mulreal,mulimaginary)


    def __str__(self): 
        if self.imaginary<0:
            return f"{self.real}-{self.imaginary}i"
        else:                                                                       # else can be written or not written it sour choice
            return f"{self.real}+{self.imaginary}i"
        

c1=complex(1,2)
c2=complex(3,4)
print(c1+c2)
print(c1*c2)