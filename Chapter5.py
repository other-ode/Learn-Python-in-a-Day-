# In order to make your programme interactive. 
# Two built-in functions can do that for us: input() and print().

# input()
# The input() function differs slightly in Python 2 and Python 3. In Python
# 2, if you want to accept user input as a string, you have to use the
# raw_input() function instead.

# The print() function is used to display information to users. It accepts
# zero or more expressions as parameters, separated by commas.

myName = input("Please enter your name: ")
myAge = input("What about your age: ")
print ("Hello World, my name is", myName, "and I am", myAge, "years old.")

# Print name and age using % formatter
print ("Hello World, my name is %s and I am %s years old." %(myName, myAge))

# Print name and age using format()
print ("Hello World, my name is {} and I am {} years old".format(myName, myAge))

# Triple Quotes
# If you need to display a long message, you can use the triple-quote
# symbol (''' or """) to span your message over multiple lines. For instance,
print ('''Hello World.
My name is James and I am 20 years old.''')