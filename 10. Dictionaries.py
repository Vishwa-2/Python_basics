customer={
    "name" : "Vishwa",
    "age" : 20,
    "is_Verified" : True
}

print(customer["name"])        #Here we cant give index as 0 instead we need to give the key and then value will get printed. Also key
                               # should be case sensitive 
#Methods
# 
# 1 customer. get("Key")  --> it will send none if not present instead of error

print(customer.get("Name"))                               



#Also we can add new key and values pair here

customer["Birthdate"] = "11 Sept 1996"

print(customer)


# WAP in which you ask for phone no then it will give you the digits in name format

phone = input("Enter your phone no here")
phone_dict = {1 : "One",
              2 : "Two",
              3 : "Three",
              4 : "Four",
              5 : "Five",
              6 : "Six",
              7 : "Seven",
              8 : "Eight",
              9 : "Nine",
              0 : "Zero"              
              }
for i in phone:
    print(phone_dict.get(int(i)), end=" ")

# Please keep this in mind that strings are only iterable here in for loop


# OR for a loop by Mosh. he used the strings only as key. Here the exclamatory mark is if we inputted the different key and in dict
output = ""
for i in phone:
    output += phone_dict.get(i, "!") + " "
    
print(output)

# WAP for emoji converter and use a split method(this will split up the sentences into words with the given seperator and output will be
# in the form of lists )

message = input(">")
words = message.split(" ")
dict_A = {
    ":)" : "😊",
    "):" : "😢",
    "))" : "😘"
    }
output=""
for i in words:
    if dict_A.get(i) == None:
        output += i + " "
    else:
        output += dict_A.get(i) + " "

print(output)


