#Python 3 Tips

print(5 + 5) # Addition
print(5 - 5) #subtraction


print(3 * 5) # Multiplication,
print(10 / 2) #division, 
print(18 % 7) #modulo
print(4 ** 2) #exponentiation

print(100 * 1.1 ** 7) #basic interest calculation

#Lesson 2

#variables

height = 1.79
weight = 68.7

BMI = weight / height** 2
print(BMI)

type(BMI)

# float - real numbers
# int - integers
# string - text
# boolean - True or False

# Lists
# Use Square brackets
list = ['a',["a", "b"],
     ["c","d"], 
     ["e","f"]]

print(list[2]) # [c,d]
print(list[-1]) # [e,f]
print(list[0:2]) # [a,b], [c,d]
print(list[-2:]) # [c,d], [e,f]

# list manipulation

list[1][1] = "x" 
list_copy = list[:] # or  = list(list) (list is an operator is this case)

#Functions

# use help(function) to see how a function works

# strings, floats, and lists are all objects, they are defined by their type.
# Methods are functions that belong to their objects
# index and count are examples of a method

print(list.index('a'))  # 0
print(list.count("a"))  # 1

# each type of object has different methods defined for it
# you can call a method to a string or a list

list.append(["g", "h"])

print(list)

# some methods change the object it is called on and some do not.

#numpy arrays
#new_list = np.array([ 1, 2, 3])

#new_list[new_list < 2] # array of [1]
#numpy assumes a single type in the whole array
# you can multipy a np array by a scalar
#light =bmi < 21 # a boolean array

#print(bmi[light]) # the array of floats

# attributes do not have round brackets. Methods do.

#there are many ways to subset numpy arrays
list[1][1]


import numpy as np
np_list = np.array(list)
np_list[1]
print(np_list.size)
print(np_list)


