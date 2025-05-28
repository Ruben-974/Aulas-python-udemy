class Writer:

    def __init__(self, name=None, tool=None):
        self._name = name
        self._tool = tool

    @property
    def tool(self):
        return self._tool

    @tool.setter
    def tool(self, tool):
        self._tool = tool


class WritingTool:
    def __init__(self, tool):
        self.tool = tool

    def to_write(self):
        print(f'The {self.tool} is written...')


writer = Writer('Mike')

pen = WritingTool('pen')
writer.tool = pen
writer.tool.to_write()

typewriter = WritingTool('typewriter')
writer.tool = typewriter
writer.tool.to_write()

