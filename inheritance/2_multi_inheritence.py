class students:
        branch='cse'
        leve=0

class teachers:
    branch='comp'
    level=1
    def update(self):
        self.level=self.level+1
        
    


class total(students,teachers):  
    strength='full'


t=total()
print(t.branch)         # here the first class is wriien students so the branch will be cse when we write below code
t.update()
print(t.level)                    