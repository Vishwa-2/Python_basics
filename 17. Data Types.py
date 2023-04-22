# Python Data Types:
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

# To get a type
x = 10
print(type(x))  #<class 'int'>

x = {"apple", "banana", "cherry"}	            # set	
x = frozenset({"apple", "banana", "cherry"})	# frozenset
x = b"Hello"                                    # Bytes
x = bytearray(5)                                # ByteArray
x = memoryview(bytes(5))	                    # memoryview
x = None	                                    # NoneType

#If we want to set the specific data type then
x = list((1,2,2,3))
x = complex(0+1j)

# Iterable -- object which is iterated
# Iteral -- object who iterated over iterable

#iter() method is to create an iteral from iterable and using next() funciton we can anytime iterate over this' but keep in mind there is a stopiterator exception as well
x  = [1,2,3,4]
i = iter(x)
print(next(i))   #1  
# ... so on