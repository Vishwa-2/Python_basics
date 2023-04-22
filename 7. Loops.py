#Guessing game using while loop
import random
i = 0
guess_no = random.randint(0,10)
while i<=2:
    num = int(input("Enter the no which I am guessing between 0 to 10 and use same  "))
    if num == guess_no:
        print("You gotcha the number is correct")
        break
    elif num < guess_no:
        print("Your no is less than guess no")
    else:
        print("Your num is greater than the guess no")

#While loop is also have else clause
# while condition:
#       ...
# else:
#       ...

#2. FOR loops : These loops are used to iterate over items

#Below loop contains item variable which will traverse through each parameter in Python string till end
for item in 'Python':
    print(item)

for item in [1,2,3]:
    print(item)

#This below range function will print the numbers from 0 to 9
for item in range(10):
    print(item)    

for item in range(1,10):
    print(item)  #This will print from 1 to 9 
for item in range(1,10, 2):
    print(item)  #This will print with seperation of 2 elements


#Nested Loop
# Draw F shape using nested loop
#    xxxxx
#    xx
#    xxxxx
#    xx
#    xx

numbers = [5,2,5,2,2]
for i in numbers:
    for j in range(i):
        print('x', end="")                
    print("")
        
#OR ---

numbers = [5,2,5,2,2]
for i in numbers:
    print('x'*i)

#More better way
numbers = [5,2,5,2,2]
for i in numbers:
    c = ''
    for j in range(i):
        c += "x"
    print(c)
    
