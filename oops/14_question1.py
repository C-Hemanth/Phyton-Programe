class Programmer:
    company='microsoft'
    def __init__(self,name,product,salary):
        self.name=name
        self.product=product
        self.salary=salary
    def details(self):
        print(f"the name is {self.name}")
        print(f"the famous produict is {self.product}")
        print(f"the saalery is {self.salary}")
hemanth=Programmer('johnnydepp','pirates','50k')
harshitha=Programmer('harshi','pirates','50k')
hemanth.details()
harshitha.details()

