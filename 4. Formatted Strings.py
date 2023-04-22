#To remove complications in the print concat we use formatted strings which looks better
Name = 'Vishwa'
Hello = "John and " +'['+Name+']'+" are good friends"
Hello_ = f"John and {[Name]} are good friends" 

print(Hello)
print(Hello_)

#Output
#John and [Vishwa] are good friends
#John and ['Vishwa'] are good friends

#Strings Methods
#1. Len()

name = "Vishwa"
print(len(name))

#If we type name.  --- then you could see the 

#When a function belongs to the specific type of objects eg. strings here we say they are "methods".(eg are upper , capatalize). 
#In contract the len and print function are for general purpose hence we call them as "Functions"

print(name.upper())         #Here the operation is getting performed but we are changing the value of name variable"
print(name)


#2. 'in' method

course = "Python for Beginners"
print('Python' in course)   #True
print('python' in course)   #False

#Other methods are such as find upper lower ect