# user type your all input at a time so sololearn compiler willntake and produce output 
import random
# print(Rchoose)
i = 1
a = 0
b = 0

# Numbers of game battles 
N = int(input())

while i <= N :

    choose = ["G", "S", "W"]
    Rchoose = random.choice(choose)
    
    # Enter your choice S, W, G
    user_choice = input()
    
    if user_choice.upper() == Rchoose:
        print("play again")
        continue
    elif user_choice.upper() == "S" and Rchoose == "W":
        print("user is won the battle no", i)
        a += 1
    elif user_choice.upper() == "S" and Rchoose == "G":
        print("Computer is won the battle no ", i)
        b += 1
    elif user_choice.upper() == "W" and Rchoose == "S":
        print("Computer is won the battle no ", i)
        b += 1
    elif user_choice.upper() == "W" and Rchoose == "G":
        print("user is won the battle no ", i)
        a += 1
    elif user_choice.upper() == "G" and Rchoose == "S":
        print("user is won the battle no ", i)
        a += 1
    elif user_choice.upper() == "G" and Rchoose == "W":
        print("Computer is won the battle no ", i)
        b += 1
    i = i + 1

if a > b:
    print(f"user won the battle {a} times ")
    print("winner of the battle is user ")
elif a < b:
    print(f"computer won the battle {b} times ")
    print("winner of the battle is computer ")
elif a == b:
    print("Battle is tie ")
