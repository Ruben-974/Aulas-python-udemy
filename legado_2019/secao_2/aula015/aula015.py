"""
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO) f -  Quantidade de casas decimais (float)
:(CARACTERE)(> OU < OU ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""
text = 'texto'
num1 = 1
num2 = 6.537

print(f'{"R":-<3}')

print(f'Formatado em {text:s} [str] ')
print(f'Formatado em {num1:d} [int]')
print(f'Formatado em {num2:f} [float]')

print(f'Formatado com 1 casa decimal {num2:.1f} [float]')
print()
print(f'Número de 3 algarismos {num1:0>3}')
print()
print(f'Str alinhado a direita {text:.<15}')
print(f'Str alinhado ao centro {text:.^15}')
print(f'Str alinhado a esquerda {text:.>15}')
