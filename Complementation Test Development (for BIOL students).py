#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import math as mt

cTest = [[1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0], 
        [0, 0, 0, 0, 1]]

print(cTest)


# In[3]:


trial = cTest[1, 3]


# In[24]:


trial = cTest[0][0]
print(trial)

trial2 = cTest[1][1]

if trial == trial2:
    print('bruh, why are the indices so scuffed')
    
test2 = np.arange(6).reshape(2, 3)

print(test2)
print(test2[0][1])

len(test2) # finds the number of rows in the array


# In[20]:


## THIS IS THE MAIN DEVELOPMENT "BOX" ##


# Default settings + input
cTestInput = ([1, 0, 1], [0, 1, 0], [0, 0, 1])
groups = []
groupRow = 0
valid = True
i = 0
j = 0

# The input must have the identity matrix; the following code checks if this is the case.
# It also checks to make sure m = n (number of rows = number of columns)

while i <= len(cTestInput):
    if cTestInput[i][i] != 1: # I matrix check
        valid = False
        i = i + 1  
    elif len(cTestInput) != len(cTestInput[i]): # m = n check
        valid = False
        i = i + 1
    else: 
        i = i + 1

# THE ACTUAL GROUP SCANNING # (NOT DONE)
i = 0
j = 0

while i <= len():
    if len(cTestInput[0]) != len(cTestInput):
        valid = False
        
    elif cTestInput[i][j] != (0 or 1):
        valid = False
        
    elif cTestInput[i][j] == 1:
        groups.append(ij)
        i = i + 1
        
    elif cTestInput[i][j] == 0:
        i = i + 1
        
    else: i = i + 1

# Finally, either we have an answer or made an error

if valid == True:
    print(len(groups))
else: 
    print('ERROR: CHECK INPUT')
    


# In[7]:


# IGNORE, this is a testing box. 

cTestInput = ([1, 0, 1], [0, 1, 0], [0, 0, 1])

print(len(cTestInput))

x = 0

if x != (1 or 2):
    print('Task failed successfully')
else: print('task failed')


# In[14]:


x = [1, 2, 3, 4]

for m in 0:len(x)
print(x[m])


# In[19]:


cTestInput = ([1, 0, 1], [0, 1, 0], [0, 0, 1])

cTestInput[2][1]

i = 0

valid = True

while i <= len(cTestInput)-1:
    if cTestInput[i][i] == 0:
        valid = False
        i = i + 1
    else: 
        i = i + 1

if valid == False:
    print('Error')
else: 
    print('Identity matrix exists')


# In[ ]:




