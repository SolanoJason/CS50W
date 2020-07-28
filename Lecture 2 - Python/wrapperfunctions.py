def announce(f):
    def wrapper():
        print("About tu run the function")
        f()
        print("Function done")
    return wrapper;

@announce
def hello():
    print("Hello World")

hello();
