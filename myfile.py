#This is the code!

import os

def walk(dir):
    for name in os.list(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)

print(walk(dir))
