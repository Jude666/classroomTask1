#This is the code!

import os

def walk(dir):
    path_list = []
    for name in os.list(dir):
       path = os.path.join(dir, name)
       if os.path.isfile(path):
           path_list.append(path)
       else:
           walk(path)
    return path_list

def reverse(walk(dir)):
    path_list = path_list[::-1]
    print(path_list)


reverse(walk(dir))
'''This is the code modifies'''
'''And this is the program to print all the folders in reverse'''
