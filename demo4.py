#4. Create a class, objects, constrcutors, functions and other oops concepts (inheritance, polymorphism,encapsulation) in python

class car(): # this a class in python using class word
    def __init__(self,model_name,price, varient,year):
        self.model_name = model_name
        self.price=price
        self.varient=varient
        self.year=year


honda =car('city',20000,'xz',2022)      #This is the object made using class
tata=car('neon',2200,'zz',2022)         #This is the object made using class

print(honda.__dict__) # We have print the object

# inheritance
# parent class is employee
class Employee:
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):
        return f"The name is {self.name} Salary is {self.salary} He's role is {self.role}"
# We are inheriting the parent class to the child class
class Programmer(Employee):
    def printProg(self):
        return f"The Programmer name is {self.name} Salary is {self.salary} He's role is {self.role} "

Rohan = Programmer('rohan',29990,'developer')
print(Rohan.printdetails())
print(Rohan.printProg())


# polymorphism
def adition(a,b):
    return a+b

def adition(a,b,c=0):
    return a+b+c

z=adition(1,5,4)
print(z)
obj=adition(1,2)
print(obj)


