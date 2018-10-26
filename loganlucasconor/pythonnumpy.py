# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 18:09:10 2018

@author: My Guy
"""

import numpy as np
print("How many classes do you have?")
numOfClass = input('Enter your input:')
a = np.zeros(int(numOfClass))
b = np.zeros(int(numOfClass))
np.insert(a, 1, 5)
for x in range (0, int(numOfClass)):
    gradeOfClass = input('What is your first class grade:')
    intGrade = int(gradeOfClass)
    a[x] = intGrade
    if intGrade >= 90 and intGrade <= 100:
        intGrade = 4
    elif intGrade >= 80 and intGrade < 90:
        intGrade = 3
    elif intGrade >= 70 and intGrade < 80:
        intGrade = 2
    elif intGrade >= 60 and intGrade < 70:
        intGrade = 1
    else:
        intGrade = 0
    b[x] = intGrade
    #np.insert(a, 1, 5)
#a = np.array([("A","B","C", "D"), (4,5,6,7)])
print(a)
print(b)

gpa = 0
for x in range (0, int(numOfClass)):
    gpa += b[x]
    
gpa = int(gpa)/int(numOfClass)
print("Your GPA is: " + str(gpa))
a.dtype
