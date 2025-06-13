class MyStr(str):

    def upper(self):
        print('upper -> MyStr')
        return super().upper()


text = MyStr('test')
print(text.upper())

class A:

    latter_a = 'the A'

    def print_latter(self):
        print('A')


class B(A):

    latter_b = 'the B'

    def print_latter(self):
        print('B')


class C(B):

    latter_c = 'the C'

    def print_latter(self):
        print('C')
        print(super().print_latter())


print('ola'.upper())

c = C()
print(c.latter_a)
print(c.latter_b)
print(C.latter_c)
c.print_latter()


