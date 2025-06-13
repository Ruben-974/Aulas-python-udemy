#      Índices
#      0123456789.......................33
txt = 'o rato roeu a roupa do rei de roma'

len_txt = len(txt)
cont = 0
new_str = ''

while cont < len_txt:

    letra = txt[cont]
    cont += 1

    if letra == 'r':
        new_str += letra.upper()
    else:
        new_str += letra

print(new_str)
