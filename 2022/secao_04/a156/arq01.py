import importlib

import arq02

print(arq02.variable)

for c in range(10):
    
    importlib.reload(arq02)

print('End')