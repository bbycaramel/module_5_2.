class House:
    def __init__(self, name, number_of_floors):
        self.name = name  # Название дома
        self.number_of_floors = number_of_floors  # Количество этажей

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")  # Если этаж вне допустимого диапазона
        else:
            for floor in range(1, new_floor + 1):
                print(floor)  # Выводим этажи

    def __len__(self):
        return self.number_of_floors  # Возвращаем количество этажей

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"  # Возвращаем строку с информацией о доме


# Создание объектов класса House
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# Пример использования __str__
print(h1)
print(h2)

# Пример использования __len__
print(len(h1))
print(len(h2))