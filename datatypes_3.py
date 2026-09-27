#This is 2nd part of 1st chapter of the book Think Python.

integer_a = 5  ;  print("This is an integer: " + str(integer_a)) # 5

#This is a float: a number with a decimal point.

#Python can check the type of a variable using the type() function.
print("Type of variable a: " + str(type(integer_a)))

float_b = 5.0
print("Type of variable b: " + str(type(float_b)))
 
string_c = "This is a string"
print("Type of variable c: " + str(type(string_c)))



#Variables can be reassigned to different types of values.
#These get rounded down  when data types are used as functions to 
# convert values from one type to another.

integer_a = 5.8 # Function int() rounds down the float to the nearest integer.
print("This is a converted integer: " + str(int(integer_a))) # 5


float_b = 5     # Function float() converts the integer to a float. 
                # We still need str() to print the float as a string and concatenate it to the string. 
print("This is a converted float: " + str(float(float_b))) 

