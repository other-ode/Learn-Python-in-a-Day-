# Chapter 8: Working with Files

# Opening and Reading Text Files

f = open('C:\\Users\\dev-research\\Documents\\Projects\\Applications\\Learn-Python-in-a-Day-\\Chapter8\\myfile.txt', 'r')

firstline = f.readline()
secondline = f.readline()
print (firstline)
print (secondline)

f.close()

