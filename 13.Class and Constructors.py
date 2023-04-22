# Class name is always start with Capital letter and no _ instead use a Capital letter only

# The __init__(self) method in a class is called as a constructor which is getting called when u create an object.
# Attributes -- These are nothing but class variables.
# Class Attributes -- These variables are inherited by every object in ca class and value of it is always same. Defined outside constructor
# Instance Attrited -- These variables are object specific and defined inside the constructor

class Student:
    school = "SMC English School Washim"
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


Vishwa = Student("Vishwa", 25)
Vishwa.x = 10                    # Here we can define one attribute even if it is not present in the class.(Kahi pan na)
print(Vishwa.x)
Komal = Student("Komal", 24)

print(Vishwa.name)
print(Komal.name)

#WAP with Person class with name attribute and Talk method

class Person:
    def __init__(self, name) -> None:
        self.name = name
    def talk(self):
        print(f"Hi I am {self.name} !")


john = Person("John")
john.talk()





