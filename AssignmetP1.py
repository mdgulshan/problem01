#from noAgrsPackage import fun_file as dec  # function decorator
#from noAgrsPackage import class_file as dwa  # class decorator
#from agrsPackage import fun_file as dwia  # function decorator
#from agrsPackage import class_file as cdwia  # class decorator


def dec(func):
    def inner(*args):

     print("Welcome.....")
     func(*args)

     print("end......")
    return inner



class dwa:
    def _init_(self,function):
        self.function = function
    def _call_(self,*args):
        self.function(*args)




def dwia(name1,name2,name3):
    print(name1,name2,name3)
    def function(func):
        def inner(*args):
            print("Welcome.....")
            func(*args)
            print("End.....")

        return inner
    return function




class cdwia:

    def _init_(self,name4,name5,name6):

        self.name4 = name4

        self.name5 = name5

        self.name6 = name6

    def _init_(self,function):

        self.function = function
    def _call_(self,*args):
        self.function(*args)




@dec
def fun2(a,b):
    print(f"we will win the soccer WC {a} {b}")
    fun2(111, 222)




@dec
def fun3(x, y, z):
    print(f"Happy Sunday fun3 {x} {y} {z}")

fun3(10,20,30)




@dwia("Sachin","Suarav","Rahul")

def fun4(x, y):
    print(f"fun4 .. {x} {y}")



fun4(88, 77)