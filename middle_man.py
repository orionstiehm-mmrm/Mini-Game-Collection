"""
middle_man.py
Orion Stiehm

A mini game for the final project 1 where the goal is to pick the middle option
"""

# Used the video https://www.youtube.com/watch?v=KWgYha0clzw to learn for loops
# I also learned about time.sleep and having to import time at https://stackoverflow.com/questions/510348/how-do-i-make-a-time-delay
# Also def/functions were handy And i got it from https://www.w3schools.com/python/python_functions.asp

import time

#All used vars
anything: str
player_round: int
player_points: list[int] = [0,0,0]
int_ans: list[int] = [0,0,0]
str_ans: list[str] = ["0","0","0"]
size_end: list[int] = [0,0,0]
loop: int
loop1: int
mid_round: int
scrable_lookup: list[str] = ["a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H","i","I","j","J","k","K","l","L","m","M","n","N","o","O","p","P","q","Q","r","R","s","S","t","T","u","U","v","V","w","W","x","X","y","Y","z","Z"]
scrable_points: list[int] = [1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]
scrable_convert: int
tie_int: int = 0
play1_word: str
play2_word: str
play3_word: str
mid_tie: int = 0
winner: int = 0

#The intro of MIDDLE MAN to explane the rules
print("""
[]      []  []  [][]    [][]    []      [][][][]      []      []    []    []    []
[][]  [][]  []  []  []  []  []  []      []            [][]  [][]  []  []  [][]  []
[]  []  []  []  []  []  []  []  []      [][][]        []  []  []  []  []  []  [][]
[]      []  []  []  []  []  []  []      []            []      []  [][][]  []    []
[]      []  []  [][]    [][]    [][][]  [][][][]      []      []  []  []  []    []
==================================================================================

In this mini game the goal is for whatever you enter to be the most middle option
out of everyone elses. Here is an example:


            P1 Gave 17              P2 Gave 37              P3 Gave 29

                                 P1     P3     P2
                                 17  <  29  <  37
                                     P3 WINS!

The mini game in total  will have three total round,  in which  different ruling
will  be used.  When you submit your  answer it will hide  it and you  will pass
control to the next play,  once everyone has answered, everybody  will watch the
results as the answers  are revealed. If there is a tie, there is an extra round""")


def end_result(): #made the figuring out who is the middle a function to use again
    for loop in range(0,3): #evaluate what numbers are bigger smaller and middle
        if int_ans[loop] < int_ans[(1+loop)%3]:
            if int_ans[loop] < int_ans[(2+loop)%3]:
                size_end[0] = loop
            elif int_ans[loop] > int_ans[(2+loop)%3]:
                size_end[1] = loop
            else:
                size_end[loop] = 3+loop
        elif int_ans[loop] > int_ans[(1+loop)%3]:
            if int_ans[loop] < int_ans[(2+loop)%3]:
                size_end[1] = loop
            elif int_ans[loop] > int_ans[(2+loop)%3]:
                size_end[2] = loop
            else:
                size_end[loop] = 3+loop
        else:
            size_end[loop] = 3+loop
#Should output something like [0,2,1] where from left to right is the player with the smaller number, so in this example player 3 won



anything = input("Enter anything to continue:")

if anything in {"anything", "Anything"}: #Fun quip if player enters "anything"
    print(f"\nYou think you clever huh? Entering \"{anything}\"...")
    time.sleep(2.5)

mid_round = 1 #Round 1 collecting the answers (Will always be int):

for loop in range(1,4):
    int_ans[loop-1] = int(input(f"\nOnto player {loop}s answer. Everyone else look away. Now enter a integer:"))
    for clear in range(0,50):
        print(" ")
end_result()

        #Round 2 ending results being displayed
print("well lets see the results...\n")
time.sleep(2.6)
print("According to size\n")
time.sleep(2)
if size_end[0] < 3 and size_end[1] < 3 and size_end[2] < 3:
    print(f"The smallest number was {int_ans[size_end[0]]}, from player {size_end[0]+1}\n") #To check how many ties there were
    time.sleep(2.6)
    print(f"The biggest number was {int_ans[size_end[2]]}, from player {size_end[2]+1}\n")
    time.sleep(3)
    print(f"But the middle number was {int_ans[size_end[1]]}, from player {size_end[1]+1}, so they get the point")
    player_points[size_end[1]] += 1
else:
    if size_end[0] >= 3 and size_end[1] >= 3 and size_end[2] >= 3:
        print(f"You somehow all picked the same number: {int_ans[1]}, so no one gets points")
    else:
        mid_tie = 0
        if size_end[0] < 3: #Setting all the words from the players
            tie_int = int_ans[(size_end[0]+2)%3]
            player_points[size_end[0]] += 1
            winner = 1
        elif size_end[1] < 3:
            tie_int = int_ans[(size_end[1]+2)%3]
            player_points[size_end[1]] += 1
            mid_tie = 1
            winner = 2
        else:
            tie_int = int_ans[(size_end[2]+2)%3]
            player_points[size_end[2]] += 1
            winner = 2
        print(f"There unfortunately was a tie between two players entering {tie_int}, so player {winner} gets a point")
time.sleep(4)


anything = input("\nPress enter to continue:")

if anything in {"anything", "Anything"}: #Fun anything quip part two
    print("\nI didn't even say type anything... why...?")
    time.sleep(2.5)

size_end = [0,0,0]
int_ans = [0,0,0]

mid_round = 2 #Round 2 will now ask for strings and judge on length

for loop in range(1,4):
    str_ans[loop-1] = input(f"\nOnto player {loop}s answer. Everyone else look away. Now enter a string:")
    int_ans[loop-1] = len(str_ans[loop-1])
    for clear in range(0,50):
        print(" ")
end_result()

print("well lets see the results...\n") #Round 2 ending results being displayed
time.sleep(2.6)
print("According length\n")
time.sleep(2)
if size_end[0] < 3 and size_end[1] < 3 and size_end[2] < 3: #To check how many ties there were
    play1_word = str_ans[size_end[0]%3]
    play2_word = str_ans[size_end[2]%3]
    play3_word = str_ans[size_end[1]%3]
    print(f"The smallest word was \"{str_ans[size_end[0]]}\" with {int_ans[size_end[0]]} characters, from player {size_end[0]+1}\n")
    time.sleep(2.6)
    print(f"The biggest word was \"{str_ans[size_end[2]]}\" with {int_ans[size_end[2]]} characters, from player {size_end[2]+1}\n")
    time.sleep(3)
    print(f"But the middle word was \"{str_ans[size_end[1]]}\" with {int_ans[size_end[1]]} characters, from player {size_end[1]+1}, so they get the point")
    player_points[size_end[1]] += 1
else:
    if size_end[0] >= 3 and size_end[1] >= 3 and size_end[2] >= 3:
        print(f"You somehow all picked the same value of \"{str_ans[0]}\", \"{str_ans[1]}\", and \"{str_ans[2]}\", so no one gets points")
    else:
        mid_tie = 0
        if size_end[0] < 3: #Setting all the words from the players
            play1_word = str_ans[(size_end[0]+2)%3]
            play2_word = str_ans[(size_end[0]+1)%3]
            play3_word = str_ans[size_end[0]]
            player_points[size_end[0]] += 1
            winner = 1
        elif size_end[1] < 3:
            play1_word = str_ans[(size_end[1]+2)%3]
            play2_word = str_ans[(size_end[1])%3]
            play3_word = str_ans[size_end[1]+1]
            player_points[size_end[1]] += 1
            mid_tie = 1
            winner = 2
        else:
            play1_word = str_ans[(size_end[2]+2)%3]
            play2_word = str_ans[(size_end[2]+1)%3]
            play3_word = str_ans[size_end[2]]
            player_points[size_end[2]] += 1
            winner = 2
        print(f"There unfortunately was a tie between \"{play1_word}\" and \"{play2_word}\", so player {winner} gets a point with \"{play3_word}\"")

time.sleep(4)

anything = input("\nPress enter to continue:")

if anything in {"anything", "Anything"}: #Fun anything quip part three
    print("\nJust stop doing that")
    time.sleep(2.5)

size_end = [0,0,0]
int_ans = [0,0,0]

mid_round = 3 #Round 3 will also ask fro a string, but will be judge on their score in scabble

for loop in range(1,4):
    str_ans[loop-1] = input(f"\nOnto player {loop}s answer. Everyone else look away. Now enter a string:")

    for loop1 in range(0,len(str_ans[loop-1])):
        try:
            scrable_convert = scrable_lookup.index(str_ans[loop-1][loop1])
        except ValueError:
            scrable_convert = -1
        if scrable_convert != -1:
            int_ans[loop-1] += scrable_points[int(scrable_convert/2)]  #What have I done

    for clear in range(0,50):
        print(" ")
end_result()

print("well lets see the results...\n") #Round 3 ending results being displayed
time.sleep(2.6)
print("According to scrabble\n")
time.sleep(2)
if size_end[0] < 3 and size_end[1] < 3 and size_end[2] < 3: #To check how many ties there were
    play1_word = str_ans[size_end[0]%3]
    play2_word = str_ans[size_end[2]%3]
    play3_word = str_ans[size_end[1]%3]
    print(f"The worst word was \"{play1_word}\" scoring {int_ans[size_end[0]]} points, from player {size_end[0]+1}\n")
    time.sleep(2.6)
    print(f"The best word was \"{play2_word}\" scoring {int_ans[size_end[2]]} points, from player {size_end[2]+1}\n")
    time.sleep(3)
    print(f"But the middle word was \"{play3_word}\" scoring {int_ans[size_end[1]]} points, from player {size_end[1]+1}, so they get the point")
    player_points[size_end[1]] += 1
else:
    if size_end[0] >= 3 and size_end[1] >= 3 and size_end[2] >= 3:
        print(f"You somehow all picked the same scoring words of \"{str_ans[0]}\", \"{str_ans[1]}\", and \"{str_ans[2]}\" with the score {int_ans[1]}, so no one gets points")
    else:
        mid_tie = 0
        if size_end[0] < 3: #Setting all the words from the players
            play1_word = str_ans[(size_end[0]+2)%3]
            play2_word = str_ans[(size_end[0]+1)%3]
            play3_word = str_ans[size_end[0]]
            player_points[size_end[0]] += 1
            winner = 1
        elif size_end[1] < 3:
            play1_word = str_ans[(size_end[1]+2)%3]
            play2_word = str_ans[(size_end[1])%3]
            play3_word = str_ans[size_end[1]+1]
            mid_tie = 1
            winner = 2
        else:
            play1_word = str_ans[(size_end[2]+2)%3]
            play2_word = str_ans[(size_end[2]+1)%3]
            play3_word = str_ans[size_end[2]]
            player_points[size_end[2]] += 1
            winner = 3
        print(f"There unfortunately was a tie between \"{play1_word}\" and \"{play2_word}\" scoring {int_ans[1+mid_tie]}, so player {winner} gets a point with \"{play3_word}\" scoring {int_ans[2-mid_tie]}")
time.sleep(4)
