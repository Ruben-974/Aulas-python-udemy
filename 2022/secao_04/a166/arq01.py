def function(funct):

    def inside(value):

        check_str(value)
        return funct(value)
    
    return inside


def check_str(value):

    if not isinstance(value, str):

        raise TypeError('O parametro deve ser uma "str".')
    
@function
def invert_str(s):

    return s[::-1]


print(invert_str(321))