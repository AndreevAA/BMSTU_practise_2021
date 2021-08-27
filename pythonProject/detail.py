import component


# Объект Детали
class Detail:
    # Публичные поля детали
    name = None
    position = None
    color = None

    # Приватные поля детали
    _canvas = None
    _components_list = None

    # Создание Детали
    def __init__(self, name, position, color, canvas, components_list):
        self.name = name
        self.position = position
        self.color = color
        self._canvas = canvas
        self._components_list = components_list

    # Отрисовка Детали
    def draw(self, canvas):
        planes = list()
        for d_component in self._components_list:
            d_component.draw(planes, canvas)
