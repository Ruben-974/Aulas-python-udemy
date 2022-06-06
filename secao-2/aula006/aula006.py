"""
iniciar com letra, pode conter números, separar _, letras minúsculas
"""

nome = 'Rúben Israel'
idade = 17
altura = 1.70
peso = 45
maior_idd = idade > 18
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos e seu IMC é: {imc:.2f}')
