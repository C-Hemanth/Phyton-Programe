class vector:
    def __init__(self, vec):
        self.vec=vec
         

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index +=1
        return str1[:-1]


    def __add__(self, vec2):
        newlist = []
        for i in range (len(self.vec)):
            newlist.append(self.vec[i] + vec2.vec[i])
        return vector(newlist)

    def __mul__(self, vec2):
        sum=0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum

    def __len__(self):
        return len(self.vec)




v1=vector([2,4,6,9])
v2=vector([3,5,7,8])
# v3=vector([0,1,7,9])


print(len(v2))
print(len(v1))