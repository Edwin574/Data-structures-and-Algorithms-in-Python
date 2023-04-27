class Pet:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed


class Dog(Pet):
    def bark(self):
        print('bark bark')


class Cat(Pet):
    def meow(self):
        print('Meow')


x = Dog('Scooby', 3, 'german Shepherd')
print(f'Dog Name:{x.name} Dog Age:{x.age} Dog Breed:{x.breed}')
x.bark()

y = Cat('Milo', 1, 'Ragdol')
print(f'Cat Name:{y.name} Cat age:{y.age} Cat breed:{y.breed}')
y.meow()
