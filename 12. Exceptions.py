# How to handle the exceptions
# 1. TypeError

age = int(input("Enter the age"))
print(age)

#Lets say if we inputted some range string instead of value then typecasting will fail with exception ValueError with exit code 1
# So to fix

try:
    age = int(input("Enter the age "))
    print(age)
except ValueError:
    print("Invalid Value")

#There is also Divide by exception and typeerror (here traverse in number)
try:
    age = int(input("Enter the age "))
    print(age)
    print(100/age)
    for i in age:
        print(i)
except ValueError:
    print("Invalid Value")
except ZeroDivisionError:
    print("Divide by zero is not possible")
except TypeError:
    print("Typeerror --")