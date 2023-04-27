class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        print('bark bark')


x = Dog('Jeff', 5, 'chiwawa')
print(x.name)
print(x.age)
print(x.breed)
x.bark()
