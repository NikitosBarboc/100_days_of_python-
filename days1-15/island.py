print("Welcome to Treasure Island. \nYour mission is to find the treasure")
side = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"')

if side.lower() == "left":
    what_next = input('You come to a like. There is an island in the middle of the lake. Type "Wait" to'
                      ' wait for a boat. Type "swim" to swim across')
    if what_next.lower() == "wait":
        door = input('You\'re arrive at the island unharmed. This is'
                     ' a house with 3 doors. One red, one yellow and one blue. Which color do you choose?')
        if door.lower() == "yellow":
            print('You win!')
        elif door.lower() == "blue":
            print('You were eaten by beasts.\n Game Over')
        else:
            print('You were burned by fire \n Game Over')
    else:
        print('You were attacked by trout. \n Game Over')
else:
    print("You're Fall into a hole.\n Game Over.")