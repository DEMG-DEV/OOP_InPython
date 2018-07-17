from character import Enemy

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("aaaaaghhh")
dave.describe()

dave.talk()
dave.set_weakness("cheese")

print("What will you figth with?")
fight_with = input()
dave.fight(fight_with)
