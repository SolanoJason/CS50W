x = input()
while(x != "exit"):
    if(x == "help"):
        print("start - to start the car\nstop - to stop the car\nexit - to exit")
    elif(x == "start"):
        print("Car started...Ready to go!")
    elif(x == "stop"):
        print("Car stopped")
    else:
        print("I don't understand that")
    x = input()
