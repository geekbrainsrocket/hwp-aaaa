#Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:

    def __init__(self, length, width):
        if isinstance(length, int) and isinstance(width, int):
            self._length = length
            self._width = width
        else:
            print("Неправильно заданы параметры")
            self._length = 0
            self._width = 0

    def weight(self, depth=1):
        if self._length and self._width:
            # формула: длина * ширина
            # * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см (= 25кг)
            # * число см толщины полотна
            return self._length * self._width * 25 * depth
        else:
            print("не заданы параметры для расчета")


r = Road(130, 20)

print(f"На покрытие дороги ушло {r.weight(5) / 1000:.01f} тонн асфальта")
print(f'На покрытие дороги ушло бы {r.weight() / 1000:.01f} тонн асфальта если делать толщиной 1 см')
