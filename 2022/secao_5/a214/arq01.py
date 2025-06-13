class Foo:

    def __init__(self):
        self.public = 'Is public'
        self._protected = 'Is protected'
        self.__private = 'Is Private'

    def public(self):
        print(self.public)

    def _protected(self):
        print(self._protected)

    def __private(self):
        print(self.__private)


f = Foo()
print(f.public)
print(f._protected)
print(f.__private)

