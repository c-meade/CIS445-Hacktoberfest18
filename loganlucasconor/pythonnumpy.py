# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 18:09:10 2018

@author: My Guy
"""

import numpy as np
print("How many classes do you have?")
numOfClass = input('Enter your input:')
a = np.zeros(int(numOfClass))
np.insert(a, 1, 5)
for x in range (0, int(numOfClass)):
    gradeOfClass = input('What is your first class grade:')
    a[x] = int(gradeOfClass)
    #np.insert(a, 1, 5)
#a = np.array([("A","B","C", "D"), (4,5,6,7)])
print(a)

a.dtype
