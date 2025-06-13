class A:
    ...
    def im(self):
        print("I'm A")

class B(A):
    ...
    #def im(self):
    #    print("I'm B")

class C(A):
    ...
    #def im(self):
    #    print("I'm C")

class D(B, C):
    ...
    #def im(self):
    #    print("I'm D")


d = D()
d.im()

