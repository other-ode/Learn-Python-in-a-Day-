# Chapter 8: Working with Files

'''
The commonly used modes are
'r' mode:
For reading only.

'w' mode:
For writing only.
If the specified file does not exist, it will be created.
If the specified file exists, any existing data on the file will be erased.

'a' mode:
For appending.
If the specified file does not exist, it will be created.
If the specified file exist, any data written to the file is automatically added
to the end

'r+' mode:
For both reading and writing.
'''

# Using a For Loop to Read Text Files

f = open('C:\\Users\\dev-research\\Documents\\Projects\\Applications\\Learn-Python-in-a-Day-\\Chapter8\\myfile.txt', 'r')

for line in f:
    print (line, end = '')
f.close()


# Writing to a Text File
'''
Now that we’ve learned how to open and read a file, let’s try writing to it.
To do that, we’ll use the ‘a’ (append) mode. You can also use the ‘w’
mode, but you’ll erase all previous content in the file if the file already
exists. Try running the following program.
'''
f = open('C:\\Users\\dev-research\\Documents\\Projects\\Applications\\Learn-Python-in-a-Day-\\Chapter8\\myfile.txt', 'a')

f.write('\nThis sentence will be appended.')
f.write('\nPython is Fun!')
f.close()