# Chapter 7: Functions and Modules
'''
Functions are simply pre-written codes that perform a certain task. For an
analogy, think of the mathematical functions available in MS Excel. To
add numbers, we can use the sum() function and type sum(A1:A5)
instead of typing A1+A2+A3+A4+A5.

Depending on how the function is written, whether it is part of a class (a
class is a concept in object-oriented programming) and how you import it, we can call a function simply by
typing the name of the function or by using the dot notation. Some
functions require us to pass data in for them to perform their tasks. These
data are known as parameters and we pass them to the function by
enclosing their values in parenthesis ( ) separated by commas.
For instance, to use the print() function for displaying text on the
screen, we call it by typing print(“Hello World”) where print is
the name of the function and “Hello World” is the parameter.
'''

# Defining Your Own Functions
'''
We can define our own functions in Python and reuse them throughout
the program. The syntax for defining a function is as follows:

def functionName(parameters): 
    code detailing what the function should do 
    return [expression]

There are two keywords here, def and return.

once the function executes a return
statement, the function will exit. If your function does not need to return
any value, you can omit the return statement. Alternatively, you can
write return or return None
'''

def checkIfPrime (numberToCheck): 
    for x in range(2,numberToCheck): 
        if (numberToCheck % x == 0):
            return False 
        return True

# print(checkIfPrime(31))


# Variable Scope
'''
An important concept to understand when defining a function is the
concept of variable scope. Variables defined inside a function are treated
differently from variables defined outside. There are two main differences.

Firstly, any variable declared inside a function is only accessible within
the function. These are known as local variables. Any variable declared
outside a function is known as a global variable and is accessible
anywhere in the program.
'''
message1 = "Global Variable"

def myFunction():
    print("\n INSIDE THE FUNCTION") 
# Global variables are accessible inside a function 
    print (message1)
# Declaring a local variable 
    message2 = "Local Variable"
    print (message2)

# Calling the function 
myFunction()

print("\nOUTSIDE THE FUNCTION")

# Global variables are accessible outside function
print (message1)

# Local variables are NOT accessible outside function.
#print (message2)

'''
The second concept to understand about variable scope is that if a local
variable shares the same name as a global variable, any code inside the
function is accessing the local variable. Any code outside is accessing
the global variable. Try running the code below
'''
message1 = "Global Variable (shares same name as a local variable)"

def myFunction2():
    message1 = "Local Variable (shares same name as a global variable)"
    print("\nINSIDE THE FUNCTION") 
    print (message1)
# Calling the function 
myFunction2()

# Printing message1 OUTSIDE the function 
print("\nOUTSIDE THE FUNCTION") 
print (message1)



# Importing Modules
'''
Python comes with a large number of built-in functions. These functions
are saved in files known as modules. To use the built-in codes in Python
modules, we have to import them into our programs first. We do that by
using the import keyword. There are three ways to do it.

The first way is to import the entire module by writing import
moduleName.

For instance, to import the random module, we write import random.
To use the randrange() function in the random module, we write
random.randrange(1, 10).

import random as r (where r is any name of your choice).

The third way to import modules is to import specific functions from the
module by writing from moduleName import name1[, name2[, ...
nameN]].

'''

# Creating our Own Module
'''
Besides importing built-in modules, we can also create our own modules.
This is very useful if you have some functions that you want to reuse in
other programming projects in future.

Creating a module is simple. Simply save the file with a .py extension and
put it in the same folder as the Python file that you are going to import it
from.
'''

