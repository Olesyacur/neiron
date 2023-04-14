# определение класса объектов Dog
class Dog:
    # метод для инициализации объекта внутренними данными
    def __init__(self, petname, temp):
        self.name = petname
        self.temperature = temp
    
    # получить состояние
    def status(self):
        print("имя собаки: ", self.name)
        print("температура собаки: ", self.temperature)
        pass
    # задать температуру
    def setTemperature(self, temp):
        self.temperature = temp
        pass
    # собаки могут лаять
    def bark(self):
        print('Гав!')
        pass
    pass