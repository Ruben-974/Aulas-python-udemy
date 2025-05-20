class Pen:

    def __init__(self, color='Blue'):
        self.color_ink = color

    def get_color(self):
        return self.color_ink

    @property
    def color(self):
        return self.color_ink


pen = Pen()

print(pen.color)
print(pen.get_color())
print(pen.color)
print(pen.color)
print(pen.color)
print(pen.color)
