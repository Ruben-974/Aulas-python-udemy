nome = 'Rúben Israel'
idade = 17
altura = 1.70
peso = 45.5
maior_idd = idade > 18
imc = peso / altura ** 2

print(nome, 'tem', idade, 'anos e seu IMC é:', imc)
print(f'{nome} tem {idade} anos e seu IMC é: {imc:.2f}')
print('{} tem {} anos e seu IMC é: {:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos e seu IMC é: {im:.2f}'.format(n=nome, i=idade, im=imc))
print('IMC: {2:.2f} | Nome: {0} | Idade: {1}'.format(nome, idade, imc))
print('IMC: {im:.2f} | Nome: {n} | Idade: {i}'.format(n=nome, i=idade, im=imc))

