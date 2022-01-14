# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Apparel(ABC):
    def __init__(self, x):
        self._name = "Apparel"
        self._parameter_name = "Apparel parameter name"
        if x and (isinstance(x, int) or isinstance(x, float)):
            self.parameter = x
        else:
            self.parameter = 0
            self._parameter_name = f"Apparel parameter name = ERROR {str(x)}"
            print(self._parameter_name)

    def __str__(self):
        return f"{self._name} : {self._parameter_name} = {self.parameter}"

    @abstractmethod
    def consumption(self):
        return self.parameter


class Costume(Apparel):
    def __init__(self, x):
        super().__init__(x)
        self._name = "костюм"
        self._parameter_name = "рост"

    @property
    def consumption(self):
        return 2 * self.parameter + 0.3


class Coat(Apparel):
    def __init__(self, x):
        super().__init__(x)
        self._name = "пальто"
        self._parameter_name = "размер"

    @property
    def consumption(self):
        return self.parameter / 6.5 + 0.5


a = float(input('Введите размер пальто: '))
b = float(input('Введите размер костюма: '))
my_coat = Coat(a)
print(my_coat)
my_costume = Costume(b)
print(my_costume)

print()
print(f"Суммарный расход ткани :  {my_coat.consumption + my_costume.consumption:>5.02f} кв.метров")
