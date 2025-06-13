def concatenate(str=''):

    def sum(letter=''):

        nonlocal str

        str += letter

        return str

    return sum


letters = concatenate('a')

print(letters('b'))
print(letters('c'))
print(letters('d'))
