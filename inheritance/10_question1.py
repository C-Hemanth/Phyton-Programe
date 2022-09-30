class c2vector:
    def __init__(self,i,j):
        self.i=i
        self.j=j

    # def __str__(self):
        # return f"{self.i}i+{self.j}j"


    def getdetails(self):
        print(f"{self.i}i+{self.j}j")
        

class c3vector(c2vector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k

    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"

c1=c2vector(1,2)
c2=c3vector(3,4,5)
# c1.getdetails()
print(c1)
print(c2)