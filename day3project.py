print("Welcome to tressure Island. Your mission is to find the treasure.")
direction = input("Choose left or right: ")
if direction == "right" :
    print("Game Over")
else :
    action = input("You want to swim or wait : ")
    if action == "swim" :
        print("Game Over")
    else :
        door = input("Choose a door : blue or yellow or red : ")
        if door == "blue" or door == "red" :
             print("Game Over")
        elif door == "yellow" :
            print("You won !")