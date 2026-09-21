"""
bombGame.py
Jethro AA.

This is the mini-game that will blow you away!
"""

#Bellow I have created some ASCII art to signify the start of the game
print("""
============================================================
            BBBB      OOOO    MMM MMM   BBBB      v.0.0.1
            B   B    O    O  M   M   M  B   B
            BBBBBB   O    O  M   M   M  BBBBBB
            B     B  O    O  M   M   M  B     B
            BBBBBB    OOOO   M   M   M  BBBBBB
            
 SSSSS   TTTTTT  OOOO   PPPPPP   PPPPPP   EEEEEEE  RRRRRR
S          TT   O    O  P     P  P     P  E        R    R
SSSSSS     TT   O    O  PPPPPP   PPPPPP   EEEEEEE  RRRRRR
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
            guess = input(": ")
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
