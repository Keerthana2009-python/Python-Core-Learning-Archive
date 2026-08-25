import random
import art
print(art.logo)
answer = random.randint(0, 100)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 0 and 100")
while True:
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty_level == "easy":
        attempts = 10
        break
    elif difficulty_level == "hard":
        attempts = 5
        break
    else:
        print("Invalid input")
print(f"You have {attempts} attempts to guess the number")
while attempts > 0:
    guess = int(input("Make a guess: "))
    if guess < answer:
        print("Too low")
    elif guess > answer:
        print("Too high")
    else:
        print("You guessed the number")
        break
    attempts -= 1
    print(f"Try again\nYou have {attempts} attempts remaining to guess the number")
if attempts == 0:
    print("Good luck next time")