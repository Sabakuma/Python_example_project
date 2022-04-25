from abc import abstractmethod,ABCMeta
import sampleData

class AnimalHandling():
    def createAllAnimalInfo():
        all = sampleData.getAnimalData()

        animals = []
        for e in all:
            tmp = None
            tId = e.get(sampleData.FIELD_NAME_ID)
            tCategory = e.get(sampleData.FIELD_NAME_CATEGORY)
            tName = e.get(sampleData.FIELD_NAME_NAME)
            tAge = e.get(sampleData.FIELD_NAME_AGE)

            if tCategory == sampleData.animalType.DOG.value:
                tmp = Dog(tId,tAge,tCategory,tName)
            elif tCategory == sampleData.animalType.CAT.value:
                tmp = Cat(tId,tAge,tCategory,tName)
            elif tCategory == sampleData.animalType.PIG.value:
                tmp = Pig(tId,tAge,tCategory,tName)
            elif tCategory == sampleData.animalType.RABBIT.value:
                tmp = Rabbit(tId,tAge,tCategory,tName)
            
            if tmp is not None :
                animals.append(tmp)
        return animals

class Animal(metaclass=ABCMeta):
    LIMIT_DOG = 25
    LIMIT_CAT = 50
    LIMIT_PIG = 10
    LIMIT_RABBIT = 80

    def __init__(self, id, age, category = None, name = None) -> None:
        self.__id = id
        self.__category = category
        self.__name = name
        self.__age = age
        return
    
    @abstractmethod
    def averageLife(self):
        pass    
    
    @property
    def animalName(self):
        return self.__name
    @property
    def animalCategory(self):
        return self.__category
    @property
    def animalId(self):
        return self.__id

    def calculateDiff(self):
        return self.averageLife() - self.__age

class Dog(Animal):
    def averageLife(self) :
        return self.LIMIT_DOG

class Cat(Animal):
    def averageLife(self): 
        return self.LIMIT_CAT

class Pig(Animal):
    def averageLife(self):
        return self.LIMIT_PIG

class Rabbit(Animal):
    def averageLife(self):
        return self.LIMIT_RABBIT