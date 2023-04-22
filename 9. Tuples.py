# Tuples are the same as list but the contents cant be changed here also they are noted with  the () brackets

cyz = (1,2,3) #Delcaration and defination

cyz[0] = 2  #Error as it is constant

print(cyz)

map

#Unpacking of values

#Lets say if we want to do the assignment
a = cyz[0]
b = cyz[1]
c = cyz[2]

# OR we can also directly write as so this is unpacking

a, b, c, = cyz
print(a)

#This is also applicable to Lists
list_a = [1,2,5]
a, b, c = list_a
print(c)