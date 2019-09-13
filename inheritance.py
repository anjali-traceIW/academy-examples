class Animal:
    def what_am_i(self):
        return "I am an animal"
class Dog(Animal):
    def what_am_i(self):
        print(Animal.what_am_i(self))
        return "I am a dog"
dog = Dog()
animal = Animal()

print("THIS IS DOG")
print(dog.what_am_i()) #"I am a dog"

print("\n\nTHIS IS ANIMAL")
print(animal.what_am_i()) #"I am an animal")

print("Henry is really cool...")
