class Pen:

    def __init__(self, color='Blue'):
        self._color = color

    def get_color(self):
        return self._color

    @property
    def color(self):
        return self._color


pen = Pen()

print(pen.color)
print(pen.get_color())
print(pen.color)
print(pen.color)
print(pen.color)
print(pen.color)
