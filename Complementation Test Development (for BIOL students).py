#!/usr/bin/env python
# coding: utf-8

# PLEASE COMMENT ANY CHANGES NOT MADE BY THE PROJECT LEADER



## THIS IS THE MAIN DEVELOPMENT "BOX" ##

# Default settings + input
cTestInput = ([1, 0, 1], [0, 1, 0], [1, 0, 1]).  # One == does not complement (-ve sign), Zero == does complement (+ve sign)
groups = []
groupRow = 0
valid = True
i = 0
j = 0

# The input must have the identity matrix; the following code checks if this is the case.
# It also checks to make sure m = n (number of rows = number of columns)

while i <= len(cTestInput)-1:
    if cTestInput[i][i] != 1: # I matrix check
        valid = False
        i = i + 1  
    elif len(cTestInput) != len(cTestInput[i]): # m = n check
        valid = False
        i = i + 1
    else: 
        i = i + 1

# THE ACTUAL GROUP SCANNING #
i = 0
j = 0

while i <= len(cTestInput)-1:   # SKIPPING THE SECOND ROW FOR SOME REASON
        c = 0  
        while c <= len(cTestInput[i])-1:
            if cTestInput[i][c] not in [0, 1]:
                valid = False
                c = c + 1
                    
            elif cTestInput[i][c] == 1:
                mutGroupCol = [i, c]   
                if mutGroupCol not in groups:
                    groups.append(mutGroupCol)
                    c = c + 1
                else: c = c + 1                
                
            else: c = c + 1      # do NOT include pass functions; they will make the loop run indefinitely.
            
                            
        if cTestInput[i][j] not in [0, 1]:
            valid = False
            i = i + 1
         
        elif cTestInput[i][j] == 1:
            mutGroupRow = [i, j]
    
            if mutGroupRow not in groups:
                groups.append(mutGroupRow)
                i = i + 1
            else: i = i + 1
        
        elif cTestInput[i][j] == 0:
                i = i + 1 
                    
        else: i = i + 1
    

# Exit Loop: now it's time to make post-appended array modifications ###################################

reverse = []

for gene in groups:  # fills variant up with the reverse of each sub-array
    if len(gene) != 2:  # checks to make sure each sub-array is the correct length of 2
        valid = False
    elif gene != gene[::-1]:
        reverse.append(gene[::-1])
    elif gene == gene[::-1]:
        pass
    else: 
        valid = False

check = 0

while check <= len(groups)-1:
    if groups[check][0] < groups[check][1]:
        groups.pop(check)
        check = check + 1
    else: check = check + 1

# Finally, either we have an answer or made an error

if valid == True:
    print(len(groups))
    print('groups:', groups)
elif valid == False: 
    print('ERROR: CHECK INPUT')
else: print('ERROR: CONTACT DEV')


print('reverse:', reverse)
