def function(funct):

    def inside(value):

        check_str(value)
        return funct(value)
    
    return inside


def check_str(value):

    if not isinstance(value, str):

        raise TypeError('O parametro deve ser uma "str".')
    

def invert_str(str):

    return str[::-1]

invert = function(invert_str)

print(invert('321'))