class SucessForm:
    formtype='SucessForm'
    def printData(self):
        print(f"Name is {self.Name}")
        print(f"Suc is {self.Suc}")


reqApplication=SucessForm()
reqApplication.Name='heamnth'
reqApplication.Suc='meeting my legends'
reqApplication.printData()
# print(reqApplication.formtype)

