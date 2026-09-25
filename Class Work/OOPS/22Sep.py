class A:
    #def __init__(self):
        #print("A Constructor")
    def fun1(self):
        print("A class")   
class B(A):
    #def __init__(self):
       # super().__init__()
       # print("B Constructor")
    def fun1(self):
        print("B class")   
class C(A):
    #def __init__(self):
        #super().__init__()
        #print("C Constructor")
    def fun1(self):
        print("C class")   

class D(B,C):
    #def __init__(self):
        #super().__init__()
       # print("D Constructor")
    def fun1(self):
        super().__init__()
        print("D class")    

obj = D()
obj.fun1()