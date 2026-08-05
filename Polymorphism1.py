
class Base:
    def fun(self):
        print("Inside base fun")

class Derived(Base):
    def fun(self):
        print("Inside Derived fun")

dobj = Derived()

dobj.fun()