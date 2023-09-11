# super keyword  kbhi kbhi child class se parent class ke methods call karna padta hai 

"""class ParentClass:
    def parent_method(self):
        print("This is the parent method.")

class ChildClass(ParentClass):
    def child_method(self):
        print("This is the child method")

        super().parent_method() 

child_object = ChildClass()
child_object.child_method()"""

# In Constructor

class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self,name,id,lang):
        # self.name = name
        # self.id = id while using this we used
        super().__init__(name,id)
        self.lang = lang
    
rohan = Employee("Rohan Das",782)
Om = Programmer("Om",786,"python")

print(rohan.name)
print(rohan.id)