class Flight():
    def __init__(self, x):
        self.capacity = x
        self.passengers = []

    def add_passenger(self, name):
        if self.available():
            self.passengers.append(name)

    def available(self):
        if self.capacity - len(self.passengers) == 0:
            print("No seats available")
            return False
        print("Succesfull")
        return True


planex = Flight(3)
People = ["Brian", "Eli", "Jason", "Hermione"]
for person in People:
    planex.add_passenger(person)
