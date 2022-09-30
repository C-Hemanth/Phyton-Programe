class vector:
    def __init__(self, vec):
        self.vec=vec
         

    def __str__(self):
        return f"{self.vec[0]}i+{self.vec[1]}j+{self.vec[2]}k"


    



v1=vector([2,4,6])
v2=vector([3,5,7])
# v3=vector([0,1,7,9])

print(v1)
print(v2)