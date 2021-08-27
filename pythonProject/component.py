import config


# Объект Component
class Component:
    # Публичные данные компонента
    c_type = None
    position = None
    color = None
    information = None

    # Создание объекта Component
    def __init__(self, c_type, position, color, information):  # position - массив с восьмью вершинами
        self.c_type = c_type
        self.position = position
        self.color = color
        self.information = information

    # Установка позиции компоненты
    def setNewPosition(self, position):
        self.position = position


# Наследуемый объекта компоненты Куб
class Cube(Component):
    # Приватные уникальные поля объета
    _allCubeVertexes = None

    def _readPlanes(self):
        all_planes = self.information[8:]

        plane_0 = list(map(int, all_planes[0].split()))
        plane_1 = list(map(int, all_planes[1].split()))
        plane_2 = list(map(int, all_planes[2].split()))
        plane_3 = list(map(int, all_planes[3].split()))
        plane_4 = list(map(int, all_planes[4].split()))
        plane_5 = list(map(int, all_planes[5].split()))

        plane_0_n = []
        plane_1_n = []
        plane_2_n = []
        plane_3_n = []
        plane_4_n = []
        plane_5_n = []

        for i in range(0, 12, 3):
            plane_0_n.append(RectanglePlane(plane_0[i], plane_0[i + 1], plane_0[i + 2], plane_0[i + 4]))

    # Отрисовка Куба
    def draw(self, planes, canvas):

        print("self.position[0].x", self.position[0].x, self.position[0].y, "\n",
              self.position[1].x, self.position[1].y, "\n",
              self.position[2].x, self.position[2].y, "\n",
              self.position[3].x, self.position[3].y, "\n",
              self.position[4].x, self.position[4].y, "\n",
              self.position[5].x, self.position[5].y, "\n",
              self.position[6].x, self.position[6].y, "\n",
              self.position[7].x, self.position[7].y, )

        canvas.create_polygon(self.position[0].x, self.position[0].y,
                              self.position[1].x, self.position[1].y,
                              self.position[2].x, self.position[2].y,
                              self.position[3].x, self.position[3].y,
                              self.position[4].x, self.position[4].y,
                              self.position[5].x, self.position[5].y,
                              self.position[6].x, self.position[6].y,
                              self.position[7].x, self.position[7].y,
                              fill=self.color, outline="black")


# Плоскость прямоугольника
class RectanglePlane:
    vertex_1 = None
    vertex_2 = None
    vertex_3 = None
    vertex_4 = None

    def __init__(self, vertex_1, vertex_2, vertex_3, vertex_4):
        self.vertex_1 = vertex_1
        self.vertex_2 = vertex_2
        self.vertex_3 = vertex_3
        self.vertex_4 = vertex_4
