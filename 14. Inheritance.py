# In Inheritance one parent class methods tranfers its properties and methods to the child classes. 
# To inherit child class should be defined with Parent class name as Parameter

class Parent:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Parent):
    pass               # this is like continue or do nothing

S2 = Student("Vishwa","Vishwa")
S2.printname()

# now if we add our child class init function then this will override the parent init function

class Student1(Parent):
    def __init__(self, fname, lname):
        self.fname = fname + "Child"
        self.lname = lname + "Child"

S3 = Student1("Vishwa","Vishwa")
S3.printname()                   # This will give an error as there is self.firstname present as init of Parent not invoked


# So to do so, we can edit out child code as 
class Student1(Parent):
    def __init__(self, fname, lname, tname):
        self.fname = fname + "Child"
        self.lname = lname + "Child"
        self.tname = tname + "Child"
    
    def printchild(self):
        print(self.fname + self.lname + self.tname)

S3 = Student1("Vishwa","Vishwa", "Voishw")
S3.printchild()      


# Also in child class we can still invoke parent class init 

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

# Also this can be done using super() function
class Abc(Person):
    def __init__(self) -> None:
        super().__init__()                 # This will inherit all the properties from parent class
