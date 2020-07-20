
# Exercise 1: Importing Modules

import random as r
import os

fileName = 'C:\\Users\\dev-research\\Documents\\Projects\\Applications\\Learn-Python-in-a-Day-\\Project_\\userScores.txt'

# Exercise 2: Getting the User’s Score
def getUserPoint(userName):
    try:
        f = open(fileName, 'r')
        for line in f:
            name, score = line.split(",")
            if (name == userName):
                return score
            return '-1'
            f.close()
    except IOError as e:
        print('File not found ', e)
    
# Exercise 3: Updating the User’s Score
def updateUserPoints(newUser, userName, score):
    if newUser:
        f = open(fileName,'a')
        f.append(userName, score)
    elif not newUser:
        f.open(fileName,'w')
        for line in f:
            name, score = line.split(",")
            #if (name == userName)