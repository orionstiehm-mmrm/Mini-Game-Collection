from random import sample

player_1 = input("Player 1 enter your name: ")
player_2 = input("Player 2 enter your name: ")
player_3 = input("Player 3 enter your name: ")

# players = [player_1, player_2, player_3]

players = {
    player_1: 11,
    player_2: 12,
    player_3: 13
}

print("There are 9 different chalices -")
print("7 of them are safe, while 2, unfortunately, contain cyanide.")
print("Take turns drinking from a chalice until there's only one player standing.")

chalices = {
    "Bronze": 1,
    "Gold": 2,
    "Silver": 3,
    "Platinum": 4,
    "Bone": 5,
    "Iron": 6,
    "Tin": 7,
    "Copper": 8,
    "Steel": 9
}

poison_chalice = sample(range(1, 10), 2)

alive = list(players.keys())
available = list(chalices.keys())
for player in players:

    print(f"\n{player}'s turn")
    print("Pick one of these chalices (don't try anything cute):")
    print(", ".join(available))

    choice = input("Choose a chalice wisely, it may be the last choice you make: ").title()

    while choice not in available:
        choice = input("Nice try. Pick an available chalice you schmo: ").title()

    chalice_number = chalices[choice]

    available.remove(choice)

    if chalice_number in poison_chalice:
        print(f"{player} drinks from the {choice} chalice...")
        print("Good choice, you're dead and everyone couldn't be happier.")
        #alive.remove(player)
    else:
        print(f"{player} drinks from the {choice} chalice...")
        print("Hmmm... your safe, how unfortunate.")

# players_alive = ", ".join(players)
# print(f"{players_alive} are still alive! This is no good, let's go again!")

while len(alive) > 1 and len(available) > 0:
    player = alive.pop(0)

    print(f"\n{player}'s turn")
    print("Pick one of these chalices (don't try anything cute):")
    print(", ".join(available))

    choice = input("Choose a chalice wisely, it may be the last choice you make: ").title()

    while choice not in available:
        choice = input("Nice try. Pick an available chalice you schmo: ").title()

    chalice_number = chalices[choice]
    available.remove(choice)
    
    if chalice_number in poison_chalice:
        print(f"{player} drinks from the {choice} chalice...")
        print("Good choice, you are dead and everyone couldn't be happier.")
        #alive.remove(player)
    else:
        print(f"{player} drinks from the {choice} chalice...")
        print("Hmmm... your safe, how unfortunate.")
