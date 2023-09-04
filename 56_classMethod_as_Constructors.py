class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])

e1 = Employee("Harry",12000)
print(e1.name)
print(e1.salary)
string = "Harry-12000" # if this are given
e2 = Employee.fromStr(string)
print(e2.name)
print(e2.salary)

# Watch video for undestand