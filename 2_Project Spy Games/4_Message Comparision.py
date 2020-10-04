# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 17:04:41 2020

@author: Om Computers
"""

# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here

#Function to compare message
def compare_msg(message_d,message_e):
    
    #Splitting the message into a list
    a_list=message_d.split()
    
    #Splitting the message into a list
    b_list=message_e.split()
    
    #Comparing the elements from both the lists
    c_list = [i for i in a_list if i not in b_list]
    
    #Combining the words of a list back to a single string sentence
    final_msg=" ".join(c_list)
    
    #Returning the sentence
    return final_msg


#Calling the function to read file
message_4=read_file(file_path_4)

#Calling the function to read file
message_5=read_file(file_path_5)

#Calling the function 'compare messages'
secret_msg_3=compare_msg(message_4,message_5)

#Printing the secret message
print(secret_msg_3)

#Code ends here