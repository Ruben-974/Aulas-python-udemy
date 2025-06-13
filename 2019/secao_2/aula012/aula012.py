user = input('Usuário: ')
senha = input('Senha: ')

if user == 'ruben974' and senha == '1234':
    print('Usuário logado com sucesso!')
elif user == 'ruben974':
    print('Senha incorreta!')
else:
    print('Usuário desconhecido!')