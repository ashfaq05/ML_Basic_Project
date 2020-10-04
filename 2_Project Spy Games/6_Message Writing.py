# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 17:06:00 2020

@author: Om Computers
"""

#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]


final_path= user_data_dir + '/secret_message.txt'

#Code starts here

#Combining the secret message parts into a single complete secret message
secret_msg=" ".join(message_parts)

#Function to write inside a file
def write_file(secret_msg,path):
       
#     #Opening a file named 'secret_message' in 'write' mode
    file = open(path, 'a+')

#     #Writing to the file
    file.write(secret_msg)

#     #Closing the file
    file.close()

# #Calling the function to write inside the file    
write_file(secret_msg, final_path)

#Printing the entire secret message
print(secret_msg)

#Code ends here