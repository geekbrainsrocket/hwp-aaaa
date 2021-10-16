# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
# метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:

    def __init__(self, title):
        if title and isinstance(title, str):
            self.title = title
        else:
            self.title = "Stationery title"

    def draw(self):
        print(f"Запуск отрисовки {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Рисуем ручкой {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Чертим карандашом {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Закрашиваем маркером {self.title}")


stationery = Stationery("по умолчанию")
stationery.draw()

pen = Pen("из пенала")
pen.draw()

pencil = Pencil("из коробки")
pencil.draw()

handle = Handle("зеленый")
handle.draw()
