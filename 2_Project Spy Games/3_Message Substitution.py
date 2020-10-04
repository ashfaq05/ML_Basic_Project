# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 17:03:58 2020

@author: Om Computers
"""


#Code starts here

#Function to substitute the message
def substitute_msg(message_c):
    
    #If-else to compare the contents of the file
    if message_c=='Red':
        sub= 'Army General'
    elif message_c=='Green':
        sub= 'Data Scientist'
    elif message_c=='Blue':
        sub ='Marine Biologist'
    
    #Returning the substitute of the message
    return sub

#Calling the function to read file
message_3=read_file(file_path_3)

#Calling the function 'substitute_msg'
secret_msg_2=substitute_msg(message_3)   

#Printing the secret message
print(secret_msg_2)

#Code ends here