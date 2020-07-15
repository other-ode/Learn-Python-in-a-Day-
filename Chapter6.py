# Chapter 6: Making Choices and Decisions

'''
if statement, for loop and while
loop. These are known as control flow tools; they control the flow of the
program. In addition, we’ll also look at the try, except statement that
determines what the program should do when an error occurs

The most common condition statement is the comparison statement. If
we want to compare whether two variables are the same, we use the ==
sign (double =). For instance, if you write x == y, you are asking the
program to check if the value of x is equals to the value of y. If they are
equal, the condition is met and the statement will evaluate to True. Else,
the statement will evaluate to False.

Other comparison signs include != (not equals), < (smaller than), >
(greater than), <= (smaller than or equals to) and >= (greater than or
equals to). The list below shows how these signs can be used and gives
examples of statements that will evaluate to True.
'''

# Equals - ==
print(5==2)

# Not equals - !=
print (5!=2)

# Greater than - >
print (5>2)

# Smaller/lesser than - <
print (5<2)

# Greater than or equals to: 5>=2
print (5>=2)

# Smaller than or equals to: 2 <= 5
print (5<=2)

# 3 logical operators - and, or, not
print(5==5 and 2>1) # True

print (5 > 2 or 7 > 10 or 3 == 2) # True

print (not 2>5) # True

print('\n')

# If Statement

'''
The if statement is one of the most commonly used control flow
statements. It allows the program to evaluate if a certain condition is met,
and to perform the appropriate action based on the result of the
evaluation.

if condition 1 is met: do A
elif condition 2 is met: do B
elif condition 3 is met: do C
elif condition 4 is met: do D
else: do E
'''

userInput = input('Enter 1 or 2: ')
if userInput == "1": 
    print ("Hello World") 
    print ("How are you?") 
elif userInput == "2": 
    print ("Python Rocks!") 
    print ("I love Python") 
else:
    print ("You did not enter a valid number")

print('\n')


# Inline If
'''
An inline if statement is a simpler form of an if statement and is more
convenient if you only need to perform a simple task. The syntax is:
do Task A if condition is true else do Task B
'''

myInt = 10
num = 12 if myInt == 10 else 13 #13
print(num)

print ("This is task A" if myInt == 10 else "This is task B")
print('\n')

# For Loop
'''
The for loop executes a block of code
repeatedly until the condition in the for statement is no longer valid.
'''
pets = ['cats', 'dogs', 'rabbits', 'hamsters']
for myPets in pets:
    print (myPets)
print('\n')

# We can also display the index of the members in the list. To do that, we
# use the enumerate() function.

for index, myPets in enumerate(pets):
    print (index, myPets)
print('\n')

# The next example shows how to loop through a string.

message = 'Hello'
for i in message:
    print (i)
print('\n')

# Looping through a sequence of numbers
'''
To loop through a sequence of numbers, the built-in range() function
comes in handy. The range() function generates a list of numbers and
has the syntax range (start, end, step).
If start is not given, the numbers generated will start from zero.
'''

for i in range(5):
    print (i) # will generate the list [0, 1, 2, 3, 4]
print('\n')

for i in range(3, 10):
    print (i) # will generate [3, 4, 5, 6, 7, 8, 9]
print('\n')

for i in range(4, 10, 2):
    print (i) # will generate [4, 6, 8]
print('\n')

# While Loop
'''
A while loop repeatedly executes
instructions inside the loop while a certain condition remains valid. The
structure of a while statement is as follows:
while condition is true:
do A
Most of the time when using a while loop, we need to first declare a
variable to function as a loop counter.
'''

counter = 5
while counter > 0:
    print ("Counter = ", counter) 
    counter = counter -1
print('\n')


# Break
'''
When working with loops, sometimes you may want to exit the entire loop
when a certain condition is met. To do that, we use the break keyword.
'''

j = 0
for i in range(5): 
    j = j + 2
    print ('i = ', i, ', j = ', j) 
    if j == 6: 
        break
print('\n')


# Continue
'''
Another useful keyword for loops is the continue keyword. When we
use continue, the rest of the loop after the keyword is skipped for that
iteration. 
'''

j = 0
for i in range(5): 
    j = j + 2
    print ('\n i = ', i, ', j = ', j) 
    if j == 6:
        continue
    print ('I will be skipped over if j=6')
print('\n')


# Try, Except
'''
This statement controls how the program proceeds when an error occurs.
The syntax is as follows:
try:
    do something
except:
    do something else when an error occurs
'''

try:
    answer = 12/0
    print (answer)
except:
    print ("An error occurred")

print('\n')

'''
If you want to display more specific error messages to your users
depending on the error, you can specify the error type after the except
keyword.

For a complete list of all the error types in Python, you can refer to
https://docs.python.org/3/library/exceptions.html.
'''

try:
    userInput1 = int(input("Please enter a number: "))
    userInput2 = int(input("Please enter another number:")) 
    answer = userInput1/userInput2
    print ("The answer is ", answer) 
    myFile = open("missing.txt", 'r') 
except ValueError as e:
    print (e)
    print ("Error: You did not enter a number") 
except ZeroDivisionError: 
    print ("Error: Cannot divide by zero") 
except Exception as e:
    print ("Unknown error: ", e)

print('\n')
