# Instance Variable vs Class Variable
# logic --> Class variable mhnje je sglyana common rahnar an instance variable mhnje te tya particular instance sathi
class Employee:
    companyName = "Apple" # class variable
    def __init__(self,name):
        self.name = name
        self.raise_amount = 0.02 # instance variable are those who are insatnce associated
    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount in {self.companyName} is {self.raise_amount}")

emp1 = Employee("Vedant")
# emp1.companyName = "Apple India" priority --> instance var > class var
emp1.raise_amount = 0.3
emp1.showDetails()
emp2 = Employee("Rohan")
emp2.showDetails()