class employee:
    sal=50
    bonos=10

    @property
    def salary(self):
        return self.sal*self.bonos

    @salary.setter
    def salary(self,tot):
        self.bonos = tot/self.salary


e=employee()
print(e.salary)
e.salary=1000
print(e.salary)
# print(e.salary)
print(e.bonos)