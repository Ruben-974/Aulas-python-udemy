x = 1

def escopo():

    def escopo2():

        x = 100

    escopo2()

    x = 10

escopo()

print(x)