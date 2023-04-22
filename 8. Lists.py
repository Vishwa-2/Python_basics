#List contains collections of items of same type

# similar to strings we have list operations as below

names = ['John', 'Harry', 'Chandler','Vishwa']

print(names[0])
print(names[0:3])
print(names[1:])
print(names[:2])
print(names[:])

names[1] = "Ross"
print(names)

#To find the largest no in the list
numbers = [3,6,2,4,8,10,54,10]
max = 0
for i in numbers:
    if max < i:
        max = i
print(max)      


# 2-D Lists
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix)

# List methods
#Append
numbers = [1,2,3,4,5,6]
numbers.append(10)
print(numbers)

#
numbers = [1,2,3,4,5,6]
numbers.clear()  #clears whole list
numbers = [1,2,3,4,5,6]
numbers2 = numbers.copy() #copy the list
print(numbers2.count(2))  #how many no of elemets are there
numbers.extend([1,2])   #extend the list by another list
print(numbers)

numbers.index(10)   # Raises index of the first "10" and error when not found
numbers.sort()
print(numbers)


# WAP to remove duplicates in a list

numbers = [1,2,3,1,2,1,1,5,6]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)