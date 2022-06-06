nome, idade, altura, peso = 'Rúben', 17, 1.70, 45.5
ano = 2022
ano_nasc = ano - idade
imc = peso / altura ** 2

print(f'''\
{nome} tem {idade} anos, {altura} de altura e pesa {peso}Kg
O IMC de {nome} é {imc:.2f}
{nome} nasceu em {ano_nasc}''')
