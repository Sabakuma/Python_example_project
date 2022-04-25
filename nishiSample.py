import nishiSampleClass

if __name__ == '__main__':

    animals = nishiSampleClass.AnimalHandling.createAllAnimalInfo()
    
    animal : nishiSampleClass.Animal
    for animal in animals:
       remainLife = animal.calculateDiff()
       print(f"{animal.animalName}:{remainLife}")