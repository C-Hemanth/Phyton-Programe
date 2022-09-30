class Pirate:
    theif='smugle'
    def getsucess(self):                                    # if we dont write self then it shows 1 argumnet is given
        print(f"he is my inspiration is {self.sucess}")
        print(f"he is my inspiration as {self.theif} is {self.sucess}")
        print("he is my inspiration")

johnnydepp=Pirate()
johnnydepp.sucess='he is my moitvation'
johnnydepp.getsucess()                    # or it can be written as
# Pirate.getsucess(johnnydepp)


