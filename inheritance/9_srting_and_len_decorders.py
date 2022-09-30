class number:
    def __init__(self,num):                             # we are adding this number 1 into
        self.num=num

    def __add__(self,num2):                             # this num2 so it makes to calculate 
        print("lets add")
        # return (300)
        return self.num+num2.num

                        #  for multiplacation
    def __mul__(self,num2):
        print('lets multiply')
        return self.num*num2.num


    def __str__(self):
        return f"the number is {self.num}"

    def __len__(self):
        return 13232

n=number(8)
print(n)
print(len(n))