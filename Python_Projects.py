

'''

...........................Project 1..................................

print("Welcome to My computer quiz! ")

playing =input("Do you want to play ? ")

if playing.lower() != "yes":
    quit()

print("Ok! Let's play :) ")
score=0
answer = input("What does CPU stand for ? ").lower()
if answer == "central processing unit":
    print("Correct! ")
    score+=1
else:
    print("Incorrect! ")


answer = input("What does GPU stand for ? ").lower()
if answer == "Graphical processing unit":
    print("Correct! ")
    score+=1
else:
    print("Incorrect! ")

answer = input("What does RAM stand for ? ").lower()
if answer == "Random Access Memory":
    print("Correct! ")
    score+=1
else:
    print("Incorrect! ")

answer = input("What does ROM stand for ? ").lower()
if answer == "Read only memory":
    print("Correct! ")
    score+=1
else:
    print("Incorrect! ")



answer = input("Which is the brain of Computer ? ").lower()
if answer == "CPU":
    print("Correct! ")
    score+=1
else:
    print("Incorrect! ")

print("You got "+str(score)+ " questions correct!  ")

print("You got "+ str((score/4) * 100)+ " questions correct ")



import random

top_of_range = input("Type a number ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger then 0 next time. ")
        quit()
else:
    print("Please type a number next time. ")
    quit()
random_number = random.randint(0, top_of_range)

#print(random_number)

guesses=0

while True:
    guesses +=1
    user_guess = input("Make a guess :- ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("type a number next time. ")
        continue
    if  user_guess == random_number:
        print("you got it !")
        break
    elif user_guess > random_number:
        print("You were above the number ")
    else:
        print("you were below the number ")


print("you got it in ",guesses,"guesses")





................... Project 2........................................






import random

user_wins=0
computer_wins=0


options= ["Rock","paper","scissors"]

while True:
    user_input=input("Type Rock/paper/scissors or Q to quit : ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    random_number= random.randint(0,2)
    # rock :0 , paper :1 scissors :2

    computer_pick=options[random_number]
    print("computers picked",computer_pick)


    if user_input == "rock" and computer_pick=="scissors":
        print("you won! ")
        user_wins+=1



    elif user_input == "rock" and computer_pick=="rock":
        print("you won! ")
        user_wins+=1



    if user_input == "scissors" and computer_pick=="paper":
        print("you won! ")
        user_wins+=1

    else:
        print("You lost! ")
        computer_wins += 1

print("you wons",user_wins,"times")

print("computer wins",computer_wins,"times ")



print("Goodbye! ")

............................ project 3................................

name=input("Type your name : ")
print("Welcome",name,"to this adventure")

answer=input("You are on a dirt road, it has come to an end and you can go left or right which way would you like to go ?").lower()

if answer == "left":
    answer=input("you come to a river, you can walk around it or swim accross ? type walk to walk around and swim to swim across :")
    if answer=="swim":
        print("you swim across and were eaten by an alligator. ")

    elif answer=="walk":
        print("You walk for many miles run out for water and you lost the game")

    else:
        print("Not a valid option you lose")


elif answer=="right":
    answer=input("you come to bridge it looks wobbly, do you want to cross it or head back ?(cross/back) ")

    if answer == "back":
        print("you back and lose ")

    elif answer == "cross":

        answer=input("You cross the bridge and meet the stranger . Do you talk to them (yes/no) ? ")

        if answer=="yes":
            print("you talk to the stranger and they give you gold . you win")

        elif answer=="no":
            print(" you ignore the stranger and they are offended and you lose .")

        else:
            print("not a valid option. you lose ")


       # print("You walk for many miles run out for water and you lost the game")

    else:
        print("Not a valid option you lose")

print("thanking for trying ", name)



........................project 4.....................................

from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

write_key()




def load_key():
    file =open("key.key","rb")
    key = file.read()
    file.close()
    return key


master_pwd= input("what is the master password ? ")

key=load_key() + master_pwd.encode()

fer=Fernet(key)

# key + password +text to encrypt + random text
# random text +key + password + text to encrypt





write_key()




def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readline():
            data = line.rstrip()
            user,passw = data.split("|")
            print("User:-",user,"password:- ",str(fer.decrypt(passw.encode())))


def add():
    name=input("Account Name :- ")
    pwd=input("Password :- ")

    with open('passwords.txt','a') as f:
        f.write(name+" |"+(fer.encrypt(pwd.encode()).decode()+" \n ")



        # "w" mode refers that if a file already exist to override the file. " r " mode refers that user can only read and last one is
# "a" mode it refers that to append the file or add some new thinf into the file .






while True:

   mode=input("would you like to add new password or view existing one (view, add)? press q to quit ? ").lower()

   if mode =="q":
       break


   if mode == "view":
    view()
   elif mode == "add":
    add()
   else:
    print("Invalid mode ")
    continue



....................... Project5..................................

import random

def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid input. Try again.")

max_score = 50
player_score = [0 for _ in range(players)]

while max(player_score) < max_score:
    for player_idx in range(players):
        current_score = 0
        while True:
            should_roll = input(f"Player {player_idx + 1}, would you like to roll (y/n)? ")
            if should_roll.lower() == "y":
                value = roll()
                if value == 1:
                    print("You rolled a 1! Turn done!")
                    break
                else:
                    current_score += value
                    print(f"You rolled a {value}. Your current score this turn is: {current_score}")
            elif should_roll.lower() == "n":
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

        player_score[player_idx] += current_score
        print(f"Player {player_idx + 1}'s total score is now: {player_score[player_idx]}")

        if player_score[player_idx] >= max_score:
            print(f"Player {player_idx + 1} wins with a score of {player_score[player_idx]}!")
            break
    if any(score >= max_score for score in player_score):
        break

print("Game over!")

....................................Project 6.........................






import random

import random

def roll():
    min_value = 1
    max_value = 6
    dice = random.randint(min_value, max_value)
    return dice

while True:
    players = input("Enter the number of players (1-4): ")
    if players.isdigit():
        players = int(players)
        if 1 <= players <= 4:
            break
        else:
            print("Must be between 1-4 players.")
    else:
        print("Invalid input, try again.")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("Player", player_idx + 1, "turn has just started!")
        current_score = 0
        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)
                print("Your current turn score is:", current_score)

        player_scores[player_idx] += current_score
        print("Player", player_idx + 1, "total score is:", player_scores[player_idx])
        if player_scores[player_idx] >= max_score:
            print("Player", player_idx + 1, "wins with a score of", player_scores[player_idx], "!")
            break
    else:
        continue
    break

time :- 2:41:56
.......................... Project 7 ..............................
'''

import random




MAX_LINES = 3
MAX_BET=100
MIN_BET=1

ROWS=3
COLS=3


symbol_count={

    "A" : 2,
    "B" :
}




def deposit():
    while True:
        amount=input("What would you like to deposit ? $")
        if amount.isdigit():
            amount=int(amount)
            if amount >0:
                break
            else:
                print("Amount must be greater then 0")
        else:
            print("Please enter a number")
    return amount
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1- "+str(MAX_LINES) + " ) ? ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Enter the valid number of lines ")
        else:
            print("Please enter a number")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line ? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <=MAX_BET:
                break
            else:
                print(f"Amount must between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number")
    return amount



def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True :
        bet=get_bet()
        total_bet= bet * lines

        if total_bet >= balance:
            print(f"You do not have enough to bet that amount. Your current balance is:- ${balance}")
        else:
            break
    print(f"you are betting $ {bet} on {lines} lines. Total bet is equal to {total_bet} ")


main()













