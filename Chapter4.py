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
