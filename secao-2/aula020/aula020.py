"""
For in em Python
Iterando strings com for
Função range(start=0, stop, step=1)
"""

txt = 'python'
new = ''

for l in txt:

    if l == 'p':
        new += l.upper()
    elif l == 'y':
        new += l.upper()
    else:
        new += l

print(new)
