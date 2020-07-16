inputFile = open('C:\\Users\\dev-research\\Documents\\Projects\\Applications\\Learn-Python-in-a-Day-\\Chapter8\\myimage.png', 'rb')
outputFile = open('C:\\Users\\dev-research\\Documents\\Projects\\Applications\\Learn-Python-in-a-Day-\\Chapter8\\myoutputimage.png', 'wb')

msg = inputFile.read(10)
while len(msg):
    outputFile.write(msg) 
    msg = inputFile.read(10)

inputFile.close() 
outputFile.close()