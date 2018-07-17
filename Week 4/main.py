from room import Room
from character import Character, Enemy, Friend
from item import Item

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("aaaaaghhh")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

tabitha = Enemy("Tabitha", "An enormous spider with countless eyes and furry legs.")
tabitha.set_conversation("Sssss....I'm so bored...")
tabitha.set_weakness("book")
ballroom.set_character(tabitha)

catrina = Friend("Catrina", "A friendly skeleton")
catrina.set_conversation("Why hello there.")
ballroom.set_character(catrina)

cheese = Item("cheese")
cheese.set_description("A large and smelly block of cheese")
ballroom.set_item(cheese)

book = Item("book")
book.set_description("A really good book entitled 'Knitting for dummies'")

current_room = kitchen
backpack = []

dead = False

while dead == False:
    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant == None or isinstance(inhabitant, Friend):
            print("There is no one here to fight with")
        else:
            print("What will you fight with?")
            fight_with = input()

            if fight_with in backpack:
                if inhabitant.fight(fight_with) == True:
                    print("Hooray, you won the fight!")
                    current_room.set_character(None)
                else:
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
    elif command == "hug":
        if inhabitant == None:
            print("There is no one here to hug :(")
        else:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you...")
            else:
                inhabitant.hug()
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to" + command)
# take the item
# move from the room
