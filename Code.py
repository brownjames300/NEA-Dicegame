from time import sleep
import random
import sys
import hashlib

scoreFile = open("./data.csv", "a")

p1total = 0
p2total = 0
even = [2, 4, 6, 8, 10, 12, 14, 16, 18]
odd = [3, 5, 7, 9, 11, 13, 15, 17]
rolling = 0
rounds = 1
attempts = 3
minimum1 = min(p1total, 0)
minimum2 = min(p2total, 0)


# Password Checker
PASSWORD = "1d4f6fbcf1697331d9c650a5106b6f4785d411fc7c6c8484740b628a5cd87ad7"

def make_hash(text):
    return str(hashlib.sha3_256(bytes(str(text), 'utf-8')).hexdigest())



password = make_hash(input("What is the password: "))
if password == PASSWORD:
    print("That is the correct password!")
else:
    sys.exit("Wrong password")



print("Welcome to the dice game!")
sleep(0.5)

# Asking for the users names
player1name = input("Enter a name for player 1: ")
print(f"Welcome {player1name} to the dice game!")
sleep(0.5)
player2name = input("Enter a name for player 2?: ")
print(f"Welcome {player2name} to the dice game!")
sleep(0.5)


# The Main Game

while rounds < 6:
    while rolling == 0:

        # Player 1 rolling...
        p1 = input("Player 1 press 'r' to roll")
        if p1 == "r":
            print("Round: " + str(rounds))

            player1roll1 = random.randint(1, 6)
            player1roll2 = random.randint(1, 6)
            player1roll3 = player1roll1 + player1roll2
            print(f"{player1name} is rolling...")
            sleep(0.1)
            print(f"Dice 1 rolled {player1roll1}")
            print(f"Dice 2 rolled {player1roll2}")
            print(f"{player1name} your overall roll was {player1roll3}")

            # If Odd or Even or Double is rolled for player1
            if player1roll1 == player1roll2:
                print("You got a double so you get 1 more roll!")
                double1 = random.randint(1, 6)
                p1total = p1total + player1roll3 + double1
                print(f"The double dice rolled a {double1}")
                print(f"You got {p1total}")

            elif player1roll3 in odd:
                p1total = p1total + player1roll3 - 5
                print(f"{player1name} you rolled odd so 5 points are deducted! You have {p1total} points!")
            elif player1roll3 in even:
                p1total = p1total + player1roll3 + 10
                print(f"{player1name} you rolled even so you get 10+ points! You have {p1total} points!")

        # Player 2 rolling...
        p2 = input("Player 2 press 'r' to roll")
        if p2 == "r":
            print("Round: " + str(rounds))

            player2roll1 = random.randint(1, 6)
            player2roll2 = random.randint(1, 6)
            player2roll3 = player2roll1 + player2roll2
            print(f"{player2name} is rolling...")
            sleep(0.1)
            print(f"Dice 1 rolled {player2roll1}")
            print(f"Dice 2 rolled {player2roll2}")
            print(f"{player2name} your overall roll was {player2roll3}")

            # If Odd or Even or Double is rolled for player2
            if player2roll1 == player2roll2:
                print("You got a double so you get 1 more roll!")
                double2 = random.randint(1, 6)
                p2total = p2total + player2roll3 + double2
                print(f"The double dice rolled a {double2}")
                print(f"You got {p2total}")

            elif player2roll3 in odd:
                p2total = p2total + player2roll3 - 5
                print(f"{player2name} you rolled odd so 5 points are deducted! You have {p2total} points!")

            elif player2roll3 in even:
                p2total = p2total + player2roll3 + 10
                print(f"{player2name} you rolled even so you get 10+ points! You have {p2total} points!")

            rounds += 1

            if rounds == 6:
                break

# Scores for the winner
if p1total == p2total:
    print("\nYou both ended up with the same score so both get to roll 1 more dice!")
    droll1 = random.randint(1, 6)
    p1total = p1total + droll1
    print(f"{player1name} press 'r' to roll your last die!")
    p1 = "r"
    if p1 == "r":
        print(f"Player 1 you rolled {droll1}")

    droll2 = random.randint(1, 6)
    p2total = p2total + droll2
    print(f"{player2name} press 'r' to roll your last die!")
    p2 = "r"
    if p2 == "r":
        print(f"Player 2 you rolled {droll2}")

elif p1total > p2total:
    print(f"\n{player1name} You won the game with {p1total}\n")
    scoreFile.write(f"\n{player1name} {p1total}")

elif p1total < p2total:
    print(f"\n{player2name} You won the game with {p2total}\n")
    scoreFile.write(f"\n{player2name} {p2total}")

scoreFile.close()


with open("data.csv", "r") as f:
    score_history = f.read().split("\n")
    for scorer in score_history:
        print(scorer)

scoreFile.close()
