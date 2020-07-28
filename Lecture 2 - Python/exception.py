import sys

x = int(input("x: "))
y = int(input("y: "))

try:
    result = x/y
    print(f"{x}/{y} is equals to {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by 0")
    sys.exit(1)
