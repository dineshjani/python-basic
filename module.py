import random as rand
import math
import os
import sys


print(rand.randint(1,5))
print(rand.randrange(1,10,2))

a=1.3
print(math.ceil(a))
print (math.floor(a))
a=5
print(math.factorial(a))



print(os.name)
print(os.getcwd())
path = "/users/djani/Documents/Basic python practice"
print(os.listdir(path))

print(os.getlogin())
print(os.getpid())

print(sys.version)
print(sys.executable)
print(sys.builtin_module_names)
print(sys.platform)
print(sys.argv)
print(sys.getdefaultencoding())














