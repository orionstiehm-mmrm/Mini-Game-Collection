from random import sample                                                       # Imports a random value for the sample.

player_1 = input("Player 1 enter your name: ")
player_2 = input("Player 2 enter your name: ")
player_3 = input("Player 3 enter your name: ")

players = {                                                                     # Players are assigned to a list.
    player_1: 11,
    player_2: 12,
    player_3: 13
}

print("There are 9 different chalices -")
print("7 of them are safe for consumption, while 2, 'unfortunately', have been poisoned.")
print("Take turns choosing a chalice to drink from.")
print("The game doesn't end until there's only one player standing.")

chalices = {                                                                    # Types of chalices are assigned to a list.
    "Brass": 1,
    "Bronze": 2,
    "Bone": 3,
    "Gold": 4,
    "Mithril": 5,
    "Obsidian": 6,
    "Platinum": 7,
    "Quartz": 8,
    "Silver": 9
}

poison_chalice = sample(range(1, 10), 2)                                        # 2 of the 9 chalices are randomly poisoned.

alive = list(players.keys())
available = list(chalices.keys())

while len(alive) > 1 and len(available) > 0:                                    # When there's at least 2 players alive and at least 1 chalice remaining the game starts/continues.

    player = alive.pop(0)

    print(f"\n{player}'s turn")
    print("Pick one of these chalices (don't try anything cute):\n")
    print(", ".join(available))                                                 # All unchosen chalices are listed.

    choice = input("Choose a chalice wisely, it may be the last choice you make: ").title()         # Capitalizes the first letter of the player's choice.

    while choice not in available:                                                                  # When a valid choice isn't made.
        choice = input("Nice try. Pick an available chalice you schmo: ").title()                   # Capitalizes the first letter of the player's choice.

    chalice_number = chalices[choice]
    available.remove(choice)                                                    # Removes the chalice the player picked.

    print(f"{player} drinks from the {choice} chalice...\n")

    if chalice_number in poison_chalice:                                                            # If player choses a poisonous chalice.
        print("Good choice, you're dead! Your friends and family couldn't be happier.")
        print("HIP HIP HOORAY!")

    else:                                                                       # If a player choses a safe chalice.
        print("Hmmm... you seem unharmed, how unfortunate?")
        alive.append(player)                                                    # Player survived and is moved to the back of the picking line.

print ()

if len(alive) == 1:                                                             # Activates when one player is alive.
    print(f"{alive[0]} wins. *sigh*")
else:                                                                           # Filler else statement; should never activate.
    print("What do you know? Everyone survived, but this should never happen.")
