import config


# Объект Model
class Model:
    # Публичные поля модели
    name = None
    numberOfVertex = None
    allVertexes = None
    color = None
    canvas = None

    # Иницирование модели
    def __init__(self, name, numberOfVertex, allVertexes, color):
        self.name = name
        self.numberOfVertex = numberOfVertex
        self.allVertexes = allVertexes
        self.color = color

    # Отрисовка модели
    def draw(self):
        self.canvas = (Vertex(10, 10, 10, self.color)).update(self.canvas)

    # Обновление Canvas
    def update(self, canvas):
        self.canvas = canvas
        for i in range(self.numberOfVertex):
            self.canvas = (Vertex(self.allVertexes[i].x, self.allVertexes[i].y, self.allVertexes[i].z, self.color)).update(self.canvas)
            print(self.allVertexes[i].x)
        return self.canvas

    # Перемещение вправо-влево
    def _moveHorizontal(self, step):
        for vertex_number in range(self.numberOfVertex):
            self.allVertexes[vertex_number].x += step

    # Перемещение вверх-вниз
    def _moveVertical(self, step):
        for vertex_number in range(self.numberOfVertex):
            self.allVertexes[vertex_number].y += step

    # Перемещение в глубину
    def _moveDeep(self, step):
        for vertex_number in range(self.numberOfVertex):
            self.allVertexes[vertex_number].z += step

    # Перемещение модели
    def move(self, direction, step):
        if direction == config.RIGHT:
            self._moveHorizontal(step)
        if direction == config.LEFT:
            self._moveHorizontal(-step)
        if direction == config.DOWN:
            self._moveHorizontal(step)
        if direction == config.TOP:
            self._moveHorizontal(-step)
        if direction == config.IN:
            self._moveHorizontal(step)
        if direction == config.OUT:
            self._moveHorizontal(-step)


# # Объект Vertex
# class Vertex:
#     # Публичные поля координат Вершины
#     x = None
#     y = None
#     z = None
#     color = None
#     canvas = None
#
#     # Создание объекта вершины
#     def __init__(self, x, y, z, color):
#         self.x = x
#         self.y = y
#         self.z = z
#         self.color = color
#
#     # Отрисовка вершины
#     def draw(self):
#         self.canvas.create_oval(self.x, self.y, self.x, self.y, fill=self.color)
#
#     # Обновление данных Canvas
#     def update(self, canvas):
#         self.canvas = canvas
#
#         self.draw()
#         return self.canvas
#
