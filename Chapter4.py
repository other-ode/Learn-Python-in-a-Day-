# Using % to format message
brand = 'Apple'
exchangeRate = 1.235235245
message = 'The price of this %s laptop is %d USD and the exchange rate is %4.2f USD to 1 EUR' %(brand, 1299, exchangeRate)
print (message)

print('\n')


# Using format() method 
# The parameter ‘Apple’ has a position of 0,
# 1299 has a position of 1 and
# 1.235235245 has a position of 2.
# Positions always start from ZERO.

message = 'The price of this {0:s} laptop is {1:d} USD and the exchange rate is {2:4.2f} USD to 1 EUR'.format('Apple', 1299, 1.235235245)
print(message)
print('\n')


# Without formatting, leave the curly brackets empty
message = 'The price of this {} laptop is {} USD and the exchange rate is {} USD to 1 EUR'.format('Apple', 1299, 1.235235245)
print(message)
print('\n')

message1 = '{0} is easier than {1}'.format('Python','Java')
message2 = '{1} is easier than {0}'.format('Python','Java')
message3 = '{:10.2f} and {:d}'.format(1.234234234, 12)
message4 = '{}'.format(1.234234234)
print (message1)
#You'll get 'Python is easier than Java'
print (message2)
#You'll get 'Java is easier than Python'
print (message3)
#You'll get ' 1.23 and 12'
#You do not need to indicate the positions of theparameters.
print (message4)
#You'll get 1.234234234. No formatting is done.

'''
There are three built-in functions in Python that allow us to do type
casting. These are the int(), float(), and str() functions.

The int() function in Python takes in a float or an appropriate string and
converts it to an integer. To change a float to an integer, we can type
int(5.712987). We’ll get 5 as the result (anything after the decimal
point is removed). To change a string to an integer, we can type int
(“4”) and we’ll get 4. However, we cannot type int (“Hello”) or
int (“4.22321”). We’ll get an error in both cases.

The float() function takes in an integer or an appropriate string and
changes it to a float. For instance, if we type float(2) or float(“2”),
we’ll get 2.0. If we type float(“2.09109”), we’ll get 2.09109 which is
a float and not a string since the quotation marks are removed.

The str() function on the other hand converts an integer or a float to a
string. For instance, if we type str(2.1), we’ll get “2.1”.

'''

# List
# listName = [initial values]

userAge = [21,22,23,24,25]
print (userAge)



'''
We can also declare a list without assigning any initial values to it. We
simply write listName = []. What we have now is an empty list with
no items in it. We have to use the append() method mentioned below to
add items to the list.

'''

print(userAge[2]) #23
print(userAge[-1]) #25

userAge2 = userAge
print(userAge2) # [21,22,23,24,25]

userAge3 = userAge[2:4]
print (userAge3) # [23,24]

del userAge[2]
print (userAge)

userAge.append(55)
print (userAge)


#declaring the list, list elements can be of different data types 
myList = [1, 2, 3, 4, 5, "Hello"]

#print the entire list.
print(myList)
#You'll get [1, 2, 3, 4, 5, "Hello"]

#print the third item (recall: Index starts from zero).
print(myList[2])
#You'll get 3

#print the last item.
print(myList[-1])
#You'll get "Hello"

#assign myList (from index 1 to 4) to myList2 and print (myList2)
myList2 = myList[1:5]
print (myList2)
#You'll get [2, 3, 4, 5]

#modify the second item in myList and print the updated list 
myList[1] = 20
print(myList)
#You'll get [1, 20, 3, 4, 5, 'Hello']

#append a new item to myList and print the updated list 
myList.append("How are you")
print(myList)
#You'll get [1, 20, 3, 4, 5, 'Hello', 'How are you']

#remove the sixth item from myList and print the updated list 
del myList[5]
print(myList)
#You'll get [1, 20, 3, 4, 5, 'How are you']

# Tuple
# tupleName = (initial values)

'''
Tuples are just like lists, but you cannot modify their values. The initial
values are the values that will stay for the rest of the program. An
example where tuples are useful is when your program needs to store
the names of the months of the year.
To declare a tuple, you write tupleName = (initial values).
'''

monthsOfYear = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
print (monthsOfYear[0]) # Jan
print (monthsOfYear[-1]) # Dec

# Dictionary
'''
To declare a dictionary, you write dictionaryName = {dictionary
key : data}, with the requirement that dictionary keys must be unique
(within one dictionary). That is, you cannot declare a dictionary like this
myDictionary = {“Peter”:38, “John”:51, “Peter”:13}.
'''
print('\n')

userNameAndAge = {"Peter":38, "John":51, "Alex":13, "Alvin":"Not Available"}
print(userNameAndAge)
print('\n')
# You can also declare a dictionary using the dict( ) method. To declare
# the userNameAndAge dictionary above, you write
userNameAndAge = dict(Peter = 38, John = 51, Alex = 13, Alvin = "Not Available")
print(userNameAndAge)

print(userNameAndAge["John"]) # 51

#declaring the dictionary, dictionary keys and data can be of different data types
myDict = {"One":1.35, 2.5:"Two Point Five", 3:"+",7.9:2}
#print the entire dictionary
print(myDict)
#You’ll get {2.5: 'Two Point Five', 3: '+', 'One': 1.35, 7.9: 2}

#Note that items in a dictionary are not stored in the same order as the way you declare them.
#print the item with key = "One".
print(myDict["One"])
#You’ll get 1.35

#print the item with key = 7.9.
print(myDict[7.9])
#You’ll get 2
#modify the item with key = 2.5 and print the updated dictionary
myDict[2.5] = "Two and a Half"
print(myDict)
#You’ll get {2.5: 'Two and a Half', 3: '+', 'One': 1.35, 7.9: 2}

#add a new item and print the updated dictionary
myDict["New item"] = "I’m new"
print(myDict)
#You’ll get {'New item': 'I’m new', 2.5: 'Two and aHalf', 3: '+', 'One': 1.35, 7.9: 2}

#remove the item with key = "One" and print the updated dictionary
del myDict["One"]
print(myDict)
#You’ll get {'New item': 'I’m new', 2.5: 'Two and a Half', 3: '+', 7.9: 2}