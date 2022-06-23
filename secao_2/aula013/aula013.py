n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')

try:
    print(float(n1) + float(n2))
except:
    print('Erro: Somente números são validos!')
