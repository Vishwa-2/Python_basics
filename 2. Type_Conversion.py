#Keep in mind the "input" function always input a string. Hence type conversion is used.
# int(),float(), bool() are some type conversions

weight = input("Weight : ")
print("His weight in Kg is "+weight+" and in pounds it is "+str(float(weight)*2.20462))
