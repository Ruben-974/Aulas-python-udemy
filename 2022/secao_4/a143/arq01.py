# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
# Mutáveis [] {} set()
# Imutáveis () "" 0 0.0 None False range(0, 10)

list = []
dictionary = {}
set = set()
tuple = ()
string = ''
integer = 0
float = 0.0
nothing = None
false = False
range_obj = range(0)

def falsy(value):
    return 'falsy' if not value else 'truthy'

print(f'TEST', falsy('TEST'))
print(f'{list=}', falsy(list))
print(f'{dictionary=}', falsy(dictionary))
print(f'{set=}', falsy(set))
print(f'{tuple=}', falsy(tuple))
print(f'{string=}', falsy(string))
print(f'{integer=}', falsy(integer))
print(f'{float=}', falsy(float))
print(f'{nothing=}', falsy(nothing))
print(f'{false=}', falsy(false))
print(f'{range_obj=}', falsy(range_obj))