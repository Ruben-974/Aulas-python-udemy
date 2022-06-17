nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

if 20 <= idade <= 30:
    print(f'{nome} pode pegar o emprestimo')
else:
    print(f'{nome} NÂO pode pegar o emprestimo')