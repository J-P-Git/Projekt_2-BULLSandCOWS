"""
projekt_2: druhý projekt do Engeto Akademie
author: Jakub Prokeš
discord: jpctf
"""
import random

cowart = """ 
           (____)   (__)
      ,-----(oo)    (oo)-----.
     /||    (..)    (__)    ||'
      ||---||         ||---w|| """

def sec_num():

    while True:
        num = random.sample('1234567890', 4)
        if num[0] != '0':
            return ''.join(num)

def val_tip(tip):

    if len(tip) != 4:
        return False
    if not tip.isdigit():
        return False
    if len(set(tip)) != 4: 
        return False
    if tip[0] == '0':
        return False
    return True

def r_tip(tip, sec_num):

    bulls = sum([1 for i in range(4) if tip[i] == sec_num[i]])
    cows = sum([1 for i in range(4) if tip[i] in sec_num and tip[i] != sec_num[i]])
    
    return bulls, cows

def res(bulls, cows):

    if bulls == 1:
        print(f"{bulls} bull", end="")
    else:
        print(f"{bulls} bulls", end="")
    
    if cows == 1:
        print(f" a {cows} cow.")
    else:
        print(f" a {cows} cows.")

def play_again():

    odpoved = input("Play again? (yes/no): ")

    if odpoved == "yes":
        main()

    elif odpoved == "no":
        print("Bye!")
        exit()

    else:
        print("For play again 'yes' for exit 'no'.")
        play_again()

def main():

    c="#"*50

    print(cowart,c,"BULLS and COWS",c,"Hi there!.","I've generated a random 4 digit number for you",
        "Let's play a bulls and cows game.",sep="\n")
    secr_num = sec_num() 
    #print(f"secret number is:",secr_num) #test
    num_in=1
    while True:
        print(c)
        tip = input("Enter a number: ")

        if not val_tip(tip):
            print("Invalid tip. Make sure the number is 4 digits, \nunique, contains no duplicates,"
            " and does not \nstart with number zero")
            continue
        
        bulls, cows = r_tip(tip, secr_num)
        res(bulls, cows)
        
        if bulls == 4:
            print(c)
            print(f"Correct, you've guessed the right number in {num_in} guesses!")
            break
        num_in += 1
    if num_in <6:
        print("Thats amazing!")
    elif 6 <= num_in < 11:
        print("average")
    elif num_in >10:
        print("not so good")
    print(c)
    play_again()

main()

       
