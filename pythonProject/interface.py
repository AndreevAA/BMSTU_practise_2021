import config
from tkinter import *


# Объект Interface
class Interface:
    # Данные создания интерфейса
    width = None
    height = None

    # Окно программы
    window = None

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
        MenuItems(self.window).show()

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
    def __init__(self, window):
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
    def __init__(self, window):
        super().__init__(window)
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


