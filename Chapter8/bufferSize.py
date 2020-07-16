inputFile = open('C:\\Users\\dev-research\\Documents\\Projects\\Applications\\Learn-Python-in-a-Day-\\Chapter8\\myfile.txt', 'r')
outputFile = open('C:\\Users\\dev-research\\Documents\\Projects\\Applications\\Learn-Python-in-a-Day-\\Chapter8\\myoutputfile.txt', 'w')

msg = inputFile.read(10)
while len(msg):
    outputFile.write(msg + '\n') 
    msg = inputFile.read(10)

inputFile.close() 
outputFile.close()