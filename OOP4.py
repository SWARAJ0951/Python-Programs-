class Demo:
    Value1 = 10      #CLASS VARIABLES
    Value2 = 20

    def __init__(self):
        self.No1 = 11
        self.No2 = 21

    #INSTANCE METHOD
    def fun(self):
        print("Inside instnace method named as fun")
        print(self.No1)
        print(self.No2)
        print(Demo.Value1)
        print(Demo.Value2)

    @classmethod
    def gun(cls):
        print("Inside class method named as gun")
        #print(Demo.No1).    #NOT ALLOWED
        #print(Demo.No2).    #NOT ALLOWED
        print(Demo.Value1)
        print(Demo.Value2)
        
#Call with Object
dobj=Demo()
dobj.gun()