"""
Manipulando strings

* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...

Sites:

    https://docs.python.org/3/library/stdtypes.html
    https://docs.python.org/3/library/functions.html
"""

txt = 'Abobrinha'

print(f'{txt[0]} = Primeiro caractere do texto [{txt}]')
print(f'{txt[-1]} = Ultimo caractere do texto [{txt}]')
print(f'{txt[:5]} = Do primeiro ao 5° caractere [{txt}]')
print(f'{txt[6:]} = Do 6° ao ultimo caractere [{txt}]')
print(f'{txt[::2]} = Texto pulando de 2 em 2 [{txt}]')