class train:
    details='raiway booking'
    def __init__(self,ticket,status,information,seats):
        # print(" if u want to book a ticket click the below seat numbers")
        # print("how many nseats do u want")
        # a=int(input("enter the number of seats"))
        self.bookticket=ticket
        self.getstatus=status
        self.information=information
        self.seats=seats
    def getdetails(self):
        print("*****************************************")
        print(f"the rate of the ticket is {self.bookticket}")
        print(f"the status of the train is {self.getstatus}")
        print(f"the info of the train is {self.information}")
        print(f"the total reserved seats are{self.seats}")

    def reserve(self):
        if(----------------------+self.seats > 0):
            print(f"the reserved seats are {self.seats}")
            self.seats=self.seats-1
        else:
            print("the seats will be finished")
tirupathi=train('1200','good','few seats are available','200')
tirupathi.getdetails()
tirupathi.reserve()

