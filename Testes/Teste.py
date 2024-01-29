def meu_decorador(funcao):
    def wrapper():
        print("Antes da execução da função")
        funcao()
        print("Depois da execução da função")
    return wrapper

@meu_decorador
def minha_funcao():
    print("Minha função")

minha_funcao()
