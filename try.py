command = input("> ")
motor_on = False
while command.lower() != "quit":
    if command.lower() == "help":
        print('''start - to start the car
stop - to stop the car
quit - to exit''')
        command = input("> ")
    elif command.lower() == "start":
        if motor_on:
            print("car was allready on")
            command = input("> ")
        else:
            motor_on = True
            print("car started... ready to go!")
            command = input("> ")
    elif command.lower() == "stop":
        if motor_on:
            motor_on = False
            print("Car stoped")
            command = input("> ")
        else:
            print("car was allready stopped")
            command = input("> ")
    else:
            print("i dont understand")
            command = input("> ")
else:
    print("game quit")