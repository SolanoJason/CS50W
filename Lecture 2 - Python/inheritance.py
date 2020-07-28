class Mammal:
    def walk(self):
        print("just walk")

    def run(self):
        print("running")


class Dog(Mammal):
    pass


dog = Dog()
dog.walk()
