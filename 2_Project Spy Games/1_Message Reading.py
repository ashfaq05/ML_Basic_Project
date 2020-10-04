# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 17:01:55 2020

@author: Om Computers
"""

##File path for the file 
file_path 

#Code starts here

#Function to read file
def read_file(path):
    
    #Opening of the file located in the path in 'read' mode
    file = open(path, 'r')
    
    #Reading of the first line of the file and storing it in a variable
    sentence=file.readline()
    
    #Closing of the file
    file.close()
    
    #Returning the first line of the file
    return sentence


#Calling the function to read file
sample_message=read_file(file_path)

#Printing the line of the file
print(sample_message)

#Code ends here