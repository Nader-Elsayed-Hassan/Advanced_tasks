# # Bytecode Inspection:
# Define a Python function square(x) that returns the square of It’s input. 
def square(x): 
    return x**2 


# use the dis module (import dis; dis.dis(square)) to inspect It’s bytecode. 
import dis 
def square(x): 
    return x * x 
dis.dis(square)

 
# Identify which bytecode instruction correspond to the multiplication 
# operation. How does this compare to the BINARY_ADD instruction seen 
# in the add function example  
def multiply(x ,y): 
    return x*y

 
# Now , define a function multiply(a, b) that returns the product of a and 
# b. Disassemble its bytecode and compare It with the add() function 
# example from the chapter. Note any similarities or differences in the 
# bytecode instructions for arithmetic operations. 
def multiply(a, b): 
    return a * b 
import dis 
dis.dis(multiply) 


# # Dynamic Tying in Action:
# create variable named data. 
data = 10 


# Assign an integer value to data and print It’s type using type(data). 
data = 10 
print (type(data))


# Reassign data to a list and print It’s type again. 
data = [1 , 2 , 3] 
print (type(data))


# Finally reassign data to simple function and print It’s type. 
data = def my_func(): 
pass 
print (type(data))
