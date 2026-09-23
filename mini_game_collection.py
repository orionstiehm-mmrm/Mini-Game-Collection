"""
    mini_game_collection


    A small collection of games including:
        Middle Man
        Bomb Game
        Poison Pill
"""
game: int =1
game_word: str
while game != 0:
    game_word = input("""Type 1 if you want to play \"Poison Chalice\",
type 2 if you want to play \"Middle Man\",
type 3 if you want to play \"Bomb Stopper\",
or type 0 if you want to exit\n""")
    while game_word.isdigit is False:
        game_word = input("Please enter valid number:\n")
    game = int(game_word)

    if game == 1:
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

    if game == 2:
        import time

        #All used vars
        player_points: list[int] = [0,0,0]
        int_ans: list[int] = [0,0,0]
        str_ans: list[str] = ["0","0","0"]
        size_end: list[int] = [0,0,0]
        loop: int
        loop1: int
        scrable_lookup: list[str] = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
                                    "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        scrable_points: list[int] = [1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]
        scrable_convert: int
        tie_int: int = 0
        play1_word: str
        play2_word: str
        play3_word: str
        winner: int = 0

        #The intro of MIDDLE MAN to explain the rules 
        print("""
        []      []  []  [][]    [][]    []      [][][][]      []      []    []    []    []
        [][]  [][]  []  []  []  []  []  []      []            [][]  [][]  []  []  [][]  []
        []  []  []  []  []  []  []  []  []      [][][]        []  []  []  []  []  []  [][]
        []      []  []  []  []  []  []  []      []            []      []  [][][]  []    []
        []      []  []  [][]    [][]    [][][]  [][][][]      []      []  []  []  []    []
        ==================================================================================

        In this mini game the goal is for  whatever you enter to be the most middle option
        out of everyone elses. Here is an example:


                    P1 Gave 17              P2 Gave 37              P3 Gave 29

                                        P1     P3     P2
                                        17  <  29  <  37
                                            P3 WINS!

        The mini game in total  will have  three total round,  in which  different  ruling
        will  be used.  When you  submit your  answer it  will hide  it and you  will pass
        control  to the next Player, once everyone  has answered, everybody will watch the
        results as the  answers  are revealed.  If there  is a tie, the other Player wins.""")


        def end_result(): #made the figuring out who is the middle a function to use again
            for loop in range(0,3): #evaluate what numbers are bigger smaller and middle
                if int_ans[loop] < int_ans[(1+loop)%3]:
                    if int_ans[loop] < int_ans[(2+loop)%3]:
                        size_end[loop] = 0
                    elif int_ans[loop] > int_ans[(2+loop)%3]:
                        size_end[loop] = 1
                    else:
                        size_end[loop] = 3
                elif int_ans[loop] > int_ans[(1+loop)%3]:
                    if int_ans[loop] < int_ans[(2+loop)%3]:
                        size_end[loop] = 1
                    elif int_ans[loop] > int_ans[(2+loop)%3]:
                        size_end[loop] = 2
                    else:
                        size_end[loop] = 3
                else:
                    size_end[loop] = 3
        #Should output something like [0,2,1] where from left to right is the player number
        # with 0 = small, 1 = mid, 2 = big, and 3 = tie


        input("\nPress enter to continue:")


        for loop in range(1,4): #Round 1 collecting the answers (Will always be int):

            str_ans[loop-1] = input(f"\nOnto Player {loop}s answer. "
                                "Everyone else look away. Now enter a integer:")
            while str_ans[loop-1].isdigit() is False:
                str_ans[loop-1] = input(f"\nPlayer {loop}, please answer with an"
                                " actual integer:")
            int_ans[loop-1] = int(str_ans[loop-1])
            print("\n" * 50)
        end_result()

        input("Press enter to see:")
        print("\nwell lets see the results...\n")
        time.sleep(2.6)
        print("According to size\n")
        time.sleep(2)

        #This same if else stuff is used two more times with other print strings

        if size_end[0] < 3 and size_end[1] < 3 and size_end[2] < 3: #To check for no ties
            print(f"The smallest number was {int_ans[size_end.index(0)]}, "
                    f"from Player {size_end.index(0)+1}\n")

            time.sleep(2.6)
            print(f"The biggest number was {int_ans[size_end.index(2)]}, "
                f"from Player {size_end.index(2)+1}\n")

            time.sleep(3)
            print(f"But the middle number was {int_ans[size_end.index(1)]}, "
                f"from Player {size_end.index(1)+1}, so they get the point")

            player_points[size_end.index(1)] += 1
        elif size_end[0] == 3 and size_end[1] == 3 and size_end[2] == 3: #Check if only ties
            print(f"You somehow you all picked the same number: {int_ans[1]}, so no one gets points")

        else: #Only one pair of ties
            if size_end[0] < 3: #Setting all the numbers from the players
                tie_int = int_ans[1]
                player_points[0] += 1
                winner = 1
            elif size_end[1] < 3:
                tie_int = int_ans[0]
                player_points[1] += 1
                winner = 2
            else:
                tie_int = int_ans[1]
                player_points[2] += 1
                winner = 3
            print(f"There unfortunately was a tie between two players entering "
                f"{tie_int}, so Player {winner} gets a point")

        time.sleep(4)


        input("\nPress enter to continue:")
        print("\n" * 50)

        size_end = [0,0,0]
        int_ans = [0,0,0]


        for loop in range(1,4): #Round 2 will now ask for strings and judge on length
            str_ans[loop-1] = input(f"\nOnto Player {loop}s answer. "
                                    "Everyone else look away. Now enter a string:")
            int_ans[loop-1] = len(str_ans[loop-1])
            print("\n" * 50)
        end_result()

        input("Press enter to see:")
        print("\nwell lets see the results...\n") #Round 2 ending results being displayed
        time.sleep(2.6)
        print("According to length\n")
        time.sleep(2)
        if size_end[0] < 3 and size_end[1] < 3 and size_end[2] < 3: #To check how many ties there were
            print(f"The smallest word was \"{str_ans[size_end.index(0)]}\" with "
                f"{int_ans[size_end.index(0)]} characters, from Player {size_end.index(0)+1}\n")

            time.sleep(2.6)
            print(f"The biggest word was \"{str_ans[size_end.index(2)]}\" with "
                f"{int_ans[size_end.index(2)]} characters, from Player {size_end.index(1)+1}\n")

            time.sleep(3)
            print(f"But the middle word was \"{str_ans[size_end.index(1)]}\" with "
                f"{int_ans[size_end.index(1)]} characters, from Player {size_end.index(1)+1}, "
                "so they get the point")

            player_points[size_end[1]] += 1
        elif size_end[0] >= 3 and size_end[1] >= 3 and size_end[2] >= 3:
            print(f"You somehow all picked the same value of \"{str_ans[0]}\", "
                f"\"{str_ans[1]}\", and \"{str_ans[2]}\", so no one gets points")

        else:
            if size_end[0] < 3: #Setting all the words from the players
                play1_word = str_ans[1]
                play2_word = str_ans[2]
                play3_word = str_ans[0]
                player_points[0] += 1
                winner = 1
            elif size_end[1] < 3:
                play1_word = str_ans[0]
                play2_word = str_ans[2]
                play3_word = str_ans[1]
                player_points[1] += 1
                winner = 2
            else:
                play1_word = str_ans[0]
                play2_word = str_ans[1]
                play3_word = str_ans[2]
                player_points[2] += 1
                winner = 3
            print(f"There unfortunately was a tie between \"{play1_word}\" and \"{play2_word}\", "
                    f"so Player {winner} gets a point with \"{play3_word}\"")

        time.sleep(4)

        input("\nPress enter to continue:")

        print("\n" * 50)

        size_end = [0,0,0]
        int_ans = [0,0,0]


        for loop in range(1,4): #Round 3 will ask for a string, but will be judge on their score in scabble
            str_ans[loop-1] = input(f"\nOnto Player {loop}s answer. "
                                    "Everyone else look away. Now enter a string:")

            for loop1 in range(0,len(str_ans[loop-1])):
                try:
                    scrable_convert = scrable_lookup.index(str_ans[loop-1][loop1].title())
                except ValueError:
                    scrable_convert = -1
                if scrable_convert != -1:
                    int_ans[loop-1] += scrable_points[int(scrable_convert)]  #convert letter to score

            print("\n" * 50)
        end_result()

        input("Press enter to see:")
        print("\nwell lets see the results...\n") #Round 3 ending results being displayed
        time.sleep(2.6)
        print("According to scrabble\n")
        time.sleep(2)
        if size_end[0] < 3 and size_end[1] < 3 and size_end[2] < 3: #To check how many ties there were
            print(f"The worst word was \"{str_ans[size_end.index(0)]}\" scoring "
                f"{int_ans[size_end.index(0)]} points, from Player {size_end.index(0)+1}\n")

            time.sleep(2.6)
            print(f"The best word was \"{str_ans[size_end.index(2)]}\" scoring "
                f"{int_ans[size_end.index(2)]} points, from Player {size_end.index(2)+1}\n")

            time.sleep(3)
            print(f"But the middle word was \"{str_ans[size_end.index(1)]}\" scoring "
                f"{int_ans[size_end.index(1)]} points, from Player {size_end.index(1)+1}, "
                "so they get the point")

            player_points[size_end[1]] += 1
        elif size_end[0] >= 3 and size_end[1] >= 3 and size_end[2] >= 3:
            print(f"You somehow all picked the same scoring words of \"{str_ans[0]}\", "
                f"\"{str_ans[1]}\", and \"{str_ans[2]}\" with the score {int_ans[1]}, "
                "so no one gets points")

        else:
            if size_end[0] < 3: #Setting all the words from the players
                play1_word = str_ans[1]
                play2_word = str_ans[2]
                play3_word = str_ans[0]
                tie_int = int_ans[1]
                player_points[0] += 1
                winner = 1
            elif size_end[1] < 3:
                play1_word = str_ans[0]
                play2_word = str_ans[2]
                play3_word = str_ans[1]
                tie_int = int_ans[0]
                player_points[1] += 1
                winner = 2
            else:
                play1_word = str_ans[0]
                play2_word = str_ans[1]
                play3_word = str_ans[2]
                tie_int = int_ans[1]
                player_points[2] += 1
                winner = 3
            print(f"There unfortunately was a tie between \"{play1_word}\" and \"{play2_word}\" "
                    f"scoring {tie_int}, so Player {winner} gets a point with "
                    f"\"{play3_word}\" scoring {int_ans[winner-1]}")

        input("\nPress enter to continue:")

        print("\n" * 50)
        print("Alright the scores are in, it was a close game...") # Giving final results
        time.sleep(3)
        print("\nprobably")
        time.sleep(3)
        print(f"\nWell anyways the scores were Player 1 at {player_points[0]}")
        time.sleep(3)
        print(f"\nAnd Player 2s score at {player_points[1]}")
        time.sleep(3)
        print(f"\nwhich leaves Player 3s score at {player_points[2]}")
        time.sleep(4)
        int_ans = player_points
        end_result()

        if size_end[0] == 2 or size_end[1] == 2 or size_end[2] == 2:
            print(f"\nSo congratulations Player {size_end.index(2)+1}, you get a star")

            ### players_stars[size_end.index(2)] += 1
        elif size_end[0] == size_end[1] == size_end[2]:
            print("\nSo you all tied, no one gets a star. What the heck, what a waist of time")
        else:
            if size_end[0] < 3: #Setting all the words from the players
                play1_word = "2"
                play2_word = "3"
                play3_word = "1"
                ### players_stars[0] += 1
            elif size_end[1] < 3:
                play1_word = "1"
                play2_word = "3"
                play3_word = "2"
                ### players_stars[1] += 1
            else:
                play1_word = "1"
                play2_word = "2"
                play3_word = "3"
                ### players_stars[2] += 1
            print(f"\nThere was a tie between Player {play1_word} and Player {play2_word}, "
                f"so they both lose and Player {play3_word} gets the star, hooray!")

    if game == 3:
                #Bellow I have created some ASCII art to signify the start of the game
        print("""
        ============================================================
                    BBBB      OOOO    MMM MMM   BBBB      v.0.0.1
                    B   B    O    O  M   M   M  B   B
                    BBBBBB   O    O  M   M   M  BBBBBB
                    B     B  O    O  M   M   M  B     B
                    BBBBBB    OOOO   M   M   M  BBBBBB
                    
         SSSSS   TTTTTT  OOOO   PPPPPP   PPPPPP   EEEEEEE  RRRRR
        S          TT   O    O  P     P  P     P  E        R    R
        sSSSSS     TT   O    O  PPPPPP   PPPPPP   EEEEEEE  RRRRRR
             S     TT   O    O  P        P        E        R   R 
        SSSSS      TT    OOOO   P        P        EEEEEEE  R    R
        ============================================================
        """)
        input("TYPE ANYTHING TO CONTINUE:... ")

        players = ["Player 1", "Player 2"]
        player_number = 0
        game_score = [0]

        while player_number < len(players):
            playing = players[player_number]
            print(playing + "'s turn first")
            #Prints a user manual script interacting with player giving them instructions periodically printed

            print("""
            _____________________________________________________________________
                                USER: INSTRUCTIONS                  
            (playerNumb) Listen up Cause I'm Only going to say this once!
                    THERE ARE THREE TOTAL PUZZLE TYPES 
                    IF YOU FAIL A PUZZLE 3 TIMES YOU DIE!         
                IF YOU SUCCEED A PUZZLE 3 TIMES YOU WIN A STAR!
            GUESS BETTER THAN YOUR COMPETITOR TO AVOID A TIE ROUND 
            (If a tie is even possible since one of you will likely die)
            _____________________________________________________________________
            """)
            input("....: ")

            ##print("""
            #_____________________________________________________________________
            #                      USER: MANUAL                  
            #                1. 
            #                2.
            #                3.
            #_____________________________________________________________________
            #""")
            ##input("....: ")

            # In here I have a list of my placeholder questions, alongsides their answers
            questions = [
            ("What rhymes with rat and fly's without wings", "Cat"),
            ("whats 6/3 + 17", "19"),
            ("How many minutes does it take to soft boil an egg?", "6"),
            ]
            # Keeps track of how many rounds won, and what round we are on
            round_number = 0
            rounds_won = 0

            # Main game round loop system
            while round_number < 3:
                question = questions[round_number][0]
                answer = questions[round_number][1]
                correct_guess = False
                player_guess = 0
                print(f"""
                _____________________________________________________________________
                                                                    
                        T-  [X 15:00 X]~~ {question}                  
                _____________________________________________________________________
                """)

                # A loop inside the main one that ends the game if theres too many guesses
                while player_guess < 3 and correct_guess == False:
                    guess = input(": ").title()
                    if guess == answer:
                        correct_guess = True
                        print("Correct! only a few fuses left to go...")
                    else:
                        player_guess += 1
                        print("WRONG -5 MINUTES ON THE TIMER")
                if correct_guess == True:
                    rounds_won += 1
                else:
                    break
                round_number += 1

            if rounds_won >= 3:
                print("You have survived for now...!")
            else:
                print("""
                    * BOOM BOOM * GAME OVER * BOOM BOOM  *
                                *         *
                    *               *       *
                """)
            #updates game score to tell whos winning after all players go
            game_score.append(rounds_won)
            player_number += 1
        #simple two player based  win system for now will refine later
        if game_score[0] > game_score[1]:
            print(players[0] + " wins the points!")
        elif game_score[0] > game_score[0]:
            print(players[1] + " wins the points!")
        else:
            print("It's a tie so lets have a tie breaker!")

        # Code a hard tie breaker where each player gets their own individual random hard question whoever gets it right gets a point
        # find a way to make the text print slowly? Make the transitions better, include more player options, colors, font changes, better ascii, 
        # updating timer print, make smoother, get finalized questions, decide if user manual is to be kept etc.
