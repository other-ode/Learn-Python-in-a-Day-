
# Exercise 1: Importing Modules

import random as r
import os

# Exercise 2: Getting the User’s Score
def getUserPoint(userName):
    f = open('C:\\Users\\dev-research\\Documents\\Projects\\Applications\\Learn-Python-in-a-Day-\\Project_\\userScores.txt', 'r')
    for line in f:
        name, score = line.split(",")
        if (name == userName):
            return score
        return '-1'

print(getUserPoint("Ann"))