try:
    x = int(input("Print an integer value: "))
    print(x)
    print(x/0)
except ZeroDivisionError:
    print("Division entre 0 no permitida")
except ValueError:
    print("Valor no valido")
