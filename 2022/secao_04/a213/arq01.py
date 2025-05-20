class Pen:

    def __init__(self, color):
        self._color = color
        self._lid_color = None

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def lid_color(self):
        return self._lid_color

    @lid_color.setter
    def lid_color(self, lid_color):
        self._lid_color = lid_color


pen = Pen('Blue')
print(pen.color)
print(pen.lid_color)

pen.color = 'Red'
pen.lid_color = 'Black'
print(pen.color)
print(pen.lid_color)