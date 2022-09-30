class cse:
    student='hemanth'
    marks='90'
    clg='iisc'

    def changemarks(self,marks):         # if we uisew this then the marks of class will only printedf
        self.marks=marks


    # def changemarks(self,marks):
        # self.__class__.marks=marks        # if we wnat to get the chnage marks in the class  cse wqe use this
   
            #   OR
    @classmethod
    def changemarks(cls,marks):         # if we usew this then maeks of class chasnges and the instance amrks will be in class
        cls.marks=marks

c=cse()
print(c.marks)
c.changemarks(95)
print(c.marks)
# print(cse.marks)                    # if we write this then we get marks of the class bu not the instance marks