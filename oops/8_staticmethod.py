class  students:
    branch='c.s.e'
    staticmethod                            # if we usestatic method we dont need to write self 
    def greet():                            #if we keep self  we get error
        print("good morning , class")
hemanth=students
hemanth.greet()



