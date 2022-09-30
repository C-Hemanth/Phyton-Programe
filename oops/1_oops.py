

a = 66
b = 88
print("the sum of a+b is", a+b)


def add(sum):
    return(a+b)


a = 55
b = 44
print(add(sum))


class Number:
    def sum(self):
        return self.a+self.b


num = Number()
num.a = 55
num.b = 66
s = num.sum()
print(s)


class addition:
    def sum(self):
        print(self.a+self.b)


add = addition()
add.a = 33
add.b = 66
