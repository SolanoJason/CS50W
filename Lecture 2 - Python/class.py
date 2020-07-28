class Point:
    x = "as"

    def __init__(self):
        print("Point created")
        self.x = "po"

    def square(self):
        print("square")


x = Point()
x.square()
print(x.x)
