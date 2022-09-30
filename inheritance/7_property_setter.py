class employee:
    salary=3000
    salarybonus=200

    @property                                       # run the totalsaalary with as property
    def totalsalary(self):
        return self.salary+self.salarybonus

    @totalsalary.setter
    def totalsalary(self,tot):
         self.salarybonus = tot-self.salary

e=employee()
# print(e.totalsalary())                  # if wekeep braces beside totalsalry then the output will come
print(e.totalsalary)                    # if we wnt to get outcome as totalsalary as a property then we use @proprety method
e.totalsalary=(5000)                    # if we want to set totalsalary as fixed then we want o change the salarybonus   
print(e.salary)
print(e.salarybonus)                        # to get the above neew salary how much salary bonuss is required