#Prints the words "Hello World"
print("Hello World")

# This is a comment
# This is also a comment
# This is yet another comment

'''
    This is a comment
    This is also a comment
    This is yet another comment
'''

#Prints the another "Hello World"
print('Hello World')


# Chapter 3: The World of Variables and Operators
# 

userAge = 0 #  After you define the variable userAge, your program will allocate

# You can define multiple variables all at once.
userAge, userName = 30, 'Peter'

# Above variable definition is the same as below
userAge = 30
userName = 'Peter'

# Naming a variable
'''
    A variable name in Python can only contain letters (a - z, A - B), numbers
    or underscores (_). However, the first character cannot be a number.
    Hence, you can name your variables userName, user_name or
    userName2 but not 2userName.
'''

# The assignment sign
# = is the assignment sign

x = 5
y = 10
x = y

print("x = ", x)
print("y = ", y)


x = 5
y = 10
y = x

print("x = ", x)
print("y = ", y)

# Basic Operators
x = 5
y = 2

# Addition
x + y # = 7

# Subtraction
x - y # = 3

# Multiplication
x * y # = 10

# Division
x/y # = 2.5

# Floor Division
x//y # = 2 (rounds down the answer to the nearest whole number)

# Modulus
x%y # = 1 (gives the remainder when 5 is divided by 2)

# Exponent
x ** y # = 25 (5 to the power of 2)

# More Assignment Operators
'''
    Besides the = sign, there are a few more assignment operators in Python
    (and most programming languages). These include operators like +=, -=
    and *=.
'''

