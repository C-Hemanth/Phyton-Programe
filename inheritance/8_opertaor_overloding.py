class number:
    def __init__(self,num):                             # we are adding this number 1 into
        self.num=num

    def __add__(self,num2):                             # this num2 so it makes to calculate 
        print("lets add")
        # return (300)
        return self.num+num2.num
        # return self.num+self.num2

                        #  for multiplacation
    def __mul__(self,num2):
        print('lets multiply')
        return self.num*num2.num

n1=number(7)
n2=number(8)
sum=n1+n2
mul=n1*n2
print(sum)
print(mul)
