class MyStr(str):

    def upper(self):
        return super().upper()


text = MyStr('test')


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
        super(C, self).print_latter()
        super(B, self).print_latter()


c = C()
c.print_latter()

#print(c.latter_a)
#print(c.latter_b)
#print(C.latter_c)
#c.print_latter()


