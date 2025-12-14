print('''
88888888888888888888888888888888888888888888888888888888888888888888888
88.._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..88
88   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  88
88      | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  88
88..__  |     |`-!._ | `.| |_______________||."'|  _!.;'   |     _|..88
88   |``"..__ |    |`";.| i|_|MMMMMMMMMMM|_|'| _!-|   |   _|..-|'    88
88   |      |``--..|_ | `;!|l|MMoMMMMoMMM|1|.'j   |_..!-'|     |     88
88   |      |    |   |`-,!_|_|MMMMP'YMMMM|_||.!-;'  |    |     |     88
88___|______|____!.,.!,.!,!|d|MMMo * loMM|p|,!,.!.,.!..__|_____|_____88
88      |     |    |  |  | |_|MMMMb,dMMMM|_|| |   |   |    |      |  88
88      |     |    |..!-;'i|r|MPYMoMMMMoM|r| |`-..|   |    |      |  88
88      |    _!.-j'  | _!,"|_|M<>MMMMoMMM|_||!._|  `i-!.._ |      |  88
88     _!.-'|    | _."|  !;|1|MbdMMoMMMMM|l|`.| `-._|    |``-.._  |  88
88..-i'     |  _.''|  !-| !|_|MMMoMMMMoMM|_|.|`-. | ``._ |     |``"..88
88   |      |.|    |.|  !| |u|MoMMMMoMMMM|n||`. |`!   | `".    |     88
88   |  _.-'  |  .'  |.' |/|_|MMMMoMMMMoM|_|! |`!  `,.|    |-._|     88
88  _!"'|     !.'|  .'| .'|[@]MMMMMMMMMMM[@] \|  `. | `._  |   `-._  88
88-'    |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-88
88      |_.'|   .' | .' |/                   \  \ |  `.  | `._    |  88
88     .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  88
88  _.'     !'|   .' | /                       \|  `  |  `.    |`.|  88
88 vanishing point 888888888888888888888888888888888888888888888(FL)888
''')
print("Welcome to the Lost Labyrinth of Aztara you will find your true self here or you will die, depend on you!?")
print("You wake up at the entrance of the ancient Labyrinth of Aztara.!! Every path have their owen ending !!")
print("Three glowing corridors stand before you.")
choose_corridors = input("Choose a corridor: A Blue Light B Red Light C Golden Light\n")
print(choose_corridors)

#this path for corridors A Blue light path
if choose_corridors == "A" or choose_corridors == "a":
    print("You enter the Chamber of Symbols")
    a_puzzle = input("A puzzle appears chose the correct symbol: Moon, Crescent, Sun.\n ")
    if a_puzzle == "Moon" or a_puzzle == "moon":
        print("You go to Crystal Room")
        crystal_room = input("What will you do? A1 Take the Blue Crystal A2 Break the Crystal\n")
        if crystal_room == "A1" or crystal_room == "a1":
            print("congratulation INTELLECT ENDING")
        else:
            print("game over a Guardian awakens")
    else:
        print("Crystal Prison → GAME OVER")

#corridors B red light path
elif choose_corridors == "B" or choose_corridors == "b":
    print("A massive Minotaur Behemoth blocks your path.")
    choose_action = input("Choose your action: B1 Run into a narrow corridor B2 Scare it away with a torch B3 Fight the monster\n")
    if choose_action == "B2" or choose_action == "b2":
        print( "Enter the Floor Trap Chamber")
        floor_trap = input("brake this riddle: What goes up but never comes down?\n")
        if floor_trap == "Age" or floor_trap == "age" or floor_trap == "Your age":
            print("applause WARRIOR ENDING")
    elif choose_action == "B1" or choose_action == "b1":
        print("Run into a narrow corridor → but can't escape → GAME OVER")
    else:
        print(" Fight the monster → you die → GAME OVER")

#corridors C golden light path
elif choose_corridors == "C" or choose_corridors == "c":
    print("You meet the Whispering Sage")
    sage_ask = input("I exist before you are born, I exist after you die, yet I am not time.\n")
    if sage_ask == "Silence" or sage_ask == "silence":
        print("Salutes MULTIVERSE ENDING (secret)")
    else:
        print("Your memories fade → GAME OVER")
else:
    print("You are not chose the corridor → You are crushed by stones → GAME OVER")


