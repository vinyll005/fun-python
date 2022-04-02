is_done = False
is_started = False
labyrinth = ['left', 'right', 'right', 'straight', 'left', 'straight']
while is_done is False:
    if not labyrinth:
        print("Congrats you win!!!")
        is_done = True
        break
    user_message = input(">").lower()
    match user_message:
        case 'help':
            print("start - for start the car game")
            print("stop - stop the car game")
            print("quit - quit from the car game")
            print("left - turn to the left")
            print("right - turn to the right")
            print("straight - go straight")
        case 'start':
            if is_started is False:
                print("You start car game")
                is_started = True
            else:
                print("Game is already started")
        case 'left' | 'right' | 'straight':
            if is_started is False:
                print("Start game at first")
            else:
                if (labyrinth[0] == user_message):
                    print("Right move from your side!")
                    del labyrinth[0]
                else:
                    print("Ooooops wrong direction!")
        case 'stop':
            if is_started is True:
                print("You stopped car game")
                is_started = False
                labyrinth = ['left', 'right', 'right', 'straight', 'left', 'straight']
            else:
                print("Game is already stopped")
        case 'quit':
            print("Quitting...")
            is_done = True
        case _:
            print("I don't understand...")