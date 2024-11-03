class House:
    houses_history = []

    def __new__(cls, args, kwargs):
        return object.__new__(cls)

    def __init__(cls, name, numbers_of_floors):
        cls.name = name
        cls.numbers_of_floors = numbers_of_floors
        cls.houses_history.append(name)

    def __del__(self):
        print(f"{self.name} снесен, но он останется в истории.")


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)

