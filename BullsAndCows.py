"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jan Kupeček
email: honzakupecek@gmail.com
discord: ming0092
"""

import random

def welcome():
    print("Hi there!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")

def generate_secret_number():
    digits = list(range(1, 10))
    random.shuffle(digits)
    secret_number = ''.join(map(str, digits[:4]))
    return secret_number

def validate_guess(guess):
    if len(guess) != 4 or not guess.isdigit() or guess[0] == '0' or len(set(guess)) != 4:
        return False
    return True

def evaluate_guess(secret_number, guess):
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret_number[i]:
            bulls += 1
        elif guess[i] in secret_number:
            cows += 1
    return bulls, cows

def main():
    welcome()
    secret_number = generate_secret_number()
    attempts = 0

    while True:
        guess = input("Enter a number: ")
        attempts += 1

        if not validate_guess(guess):
            print("You can guess only 4 random numbers and 0 can't be first. Try again.")
            continue

        bulls, cows = evaluate_guess(secret_number, guess)

        print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, {cows} {'cow' if cows == 1 else 'cows'}")

        if bulls == 4:
            print(f"Correct, you've guessed the right number {secret_number} in {attempts} guesses!")
            break

if __name__ == "__main__":
    main()