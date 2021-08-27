import config, detail, uploading

from tkinter import *


# Объект Interface
class Interface:
    # Данные создания интерфейса
    width = None
    height = None

    # Окно программы
    window = None

    # Экран программы
    canvas = None

    # Создание объекта Interface
    def __init__(self):
        # Устновка размеров окна
        self.width = config.width
        self.height = config.height

    # Отображение объекта Interface
    def start(self):
        # Создание окна программы
        self.window = Tk()

        # Установка названия окна
        self._set_title()

        # Установка MenuItem
        MenuItems(self.window, self.canvas).show()

        # Отрисовка окна рисования
        self.canvas = Scrim(self.window, self.canvas).update()

        # Создание блока управления
        self.canvas = ControlCenter(self.window, self.canvas).update()

        loader = uploading.BaseLoader("/Applications/BMSTU_practise_2021/pythonProject/models_packs/игрушка_кубик_1.txt")

        detail1 = detail.Detail(loader.getDetailName(),
                                loader.getDetailPosition(),
                                loader.getDetailColor(),
                                self.canvas,
                                loader.getListOfComponents())

        detail1.draw(self.canvas)

        # Упаковка элементов приложения
        self.canvas.pack()

        # Запуск всех настроек
        self.window.mainloop()

    # Удаление объекта Interface
    def stop(self):
        exit(self)

    # Установка названия окна
    def _set_title(self):
        self.window.title(config.window_title)


# Наследуемый базовый объект InterfaceElement
class InterfaceElement(Interface):
    # Базовый элементы
    _window = None

    # Создание Базового объекта
    def __init__(self, window, canvas):
        super().__init__()
        self._window = window

    # Отображение объекта InterfaceElement
    def show(self):
        print()


# Наследуюемый объект MenuItems
class MenuItems(InterfaceElement):
    # Текущий Item
    _menu = None
    _window = None

    # Создание наследуемого объекта MenuItems
    def __init__(self, window, canvas):
        super().__init__(window, canvas)
        self._window = window
        self._menu = Menu(self.window)

    # Отображение наследуемого объекта MenuItems
    def show(self):
        # Установка _scene
        self._scene()

        # Обновление данных
        self._update()

    # Установка модуля Scene
    def _scene(self):
        # Выводимый объект
        new_item = Menu(self._menu)

        # Команда выводимого объекта
        new_item.add_command(label='Clear all')

        # Добавление массива команда в выводимую строку
        self._menu.add_cascade(label='Scene', menu=new_item)

    # Обновление данных Window
    def _update(self):
        self._window.config(menu=self._menu)


# Наследуемый объект Scrim
class Scrim(InterfaceElement):
    # Приватные данные
    _canvas = None

    # Создание объекта Scrim
    def __init__(self, window, canvas):
        super().__init__(window, canvas)
        self._canvas = Canvas(window, width=self.width, height=self.height, bg="lightgrey",
                              cursor="pencil")

    # Обновление данных Scrim
    def update(self):
        return self._canvas


# Наследуемый объект ControlCenter
class ControlCenter(InterfaceElement):
    # Приватные данные
    _canvas = None
    _isFileUploaded = False

    # Создание объекта ControlCenter
    def __init__(self, window, canvas):
        super().__init__(window, canvas)
        self._canvas = canvas

    # Обновление Canvas
    def update(self):
        return self._canvas
