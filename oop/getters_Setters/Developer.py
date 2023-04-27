
class Developer:
    def __init__(self,name):
        #declaring private class attributes
        self.__name=name

    def getName(self):
        return print(f'{self.__name}')

    def setName(self,name):
        self.__name=name

dev1=Developer('Allison Parker')
dev1.getName()

dev1.setName('Allison Beckham parker')
dev1.getName()