# public-   open for all
# private - Open for certain user
# protected - Only for Me

class Employee:
    no_of_leaves = 8
    var = 8

    _protec = 9     # it's a protective
    __phone = 8622324411


    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"


    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod

    def change_leaves(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good "+ string)


emp = Employee("Sabbir", 1500, "Programmer")

print(emp._protec)

# print(emp.__phone)   this will give error because protective

print(emp._Employee__phone)    # name mangling   _Employee
