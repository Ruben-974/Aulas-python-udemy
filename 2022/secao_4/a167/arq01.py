


def create_decorator(x):

    print('create decorator')

    def create_function(funct):

        print('create function')
        
        def inner(y):

            print('create inner function')
            
            z = funct(x, y)

            return z
            
        return inner
    
    return create_function

@create_decorator(10)
def sum(x, y):
    return x + y

print(sum(2))