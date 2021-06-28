'''

this file holds the logic for connecting views with models

'''

import random

def genCode():
    src = [str(random.randint(a = 0, b = 9)) for i in range(7)]
    code = ''.join(src)
    return int(code)
        

print(genCode())
