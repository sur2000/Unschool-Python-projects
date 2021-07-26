import random


def main():
    command = str(input("Welcome odysseus, this is the prison cell where the investigation began. To play, type EXAMINE and then the object you want to examine. (Firstly PRESS ENTER to Start): "))
    command = str(input(" ROUND 1- A small room with a single window and a bed. There is a toilet in one corner, and a small desk lies along the wall directly in front of the door -> "))
    while command != "examine toilet":
          command = input("You see nothing special about it.\nPlease examine further: ")

    if command == "examine toilet":
        command = str(input("A steel pot with no ventilation system except for a grill window. A washing basin over it for brushing and washing and a broken mirror in front. The tile behind seems a little offset -> "))
    while command != "examine tile":
          command = input("There is nothing.\nPlease examine further: ")

    if command == "examine tile":
        command = str(input("On moving the tile, a little depression in the floor, with some rags and a small flask filled with alcohol. A journal stares back at you from beneath the rags. One of the rags has a dark brown stain on it, likely dried blood -> "))
    while command != "examine journal":
          command = input("You see nothing special about it.\nPlease examine further: ")

    if command == "examine journal":
        command = str(input("A standard journal with a brown cover. On opening it, multiple pages seem to be missing, going back to over a year, while reading it, you also notice a mirror laying on the floor -> "))
    while command != "examine mirror":
        command = input("There is nothing.\nPlease examine further: ")

    if command == "examine mirror":
        command = str(input("The mirror seems broken from the top left corner. There is some gap between the mirror case and the back of the mirror. The inmate must have gotten hurt/injured while hiding something there. You  also notice a paper sticking out from behind it -> "))
    while command != "examine paper":
        command = input("You see nothing special about it.\nPlease examine further: ")

    if command == "examine paper":
        command = str(input("For all the information I have passed over to you, you better hold up to it. I better contact you again soon, I will have to set up a phone call woth you guys. For now, the only choice for you is to get out of this shithole once and for all. ( PRESS ENTER ): "))


    command = input("Your work is completed. Get out of here ASAP. (Type Quit to quit): ")
    
    
    print("-------------Game Over!-------------")
    

main()
