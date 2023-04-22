# Modules are files in which particular code is saved

# WAP to find the max value in the given nos from inporting utils module
import utils

numbers = input("Enter the nos need to find the largest: ")
num = numbers.split(" ")

print(utils.find_max(num))

# Also importing can be done in another way if we dont whole module to be imported then we can do one more way

from utils import find_max
list_a ={}
find_max(list_a)                 # Here no need to use utils.find_max