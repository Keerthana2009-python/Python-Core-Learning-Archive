import random
import game_data
import art
print(art.logo)
game_over = True
score = 0
a = random.choice(game_data.data)
b = random.choice(game_data.data)
while game_over:
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(art.vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")
    guess1 = a['follower_count']
    guess2 = b['follower_count']
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n" * 20)
    print(art.logo)
    if guess1 > guess2:
        answer = 'A'.lower()
    else:
        answer = 'B'.lower()
    if guess == answer:
        score += 1
        print(f"You're right!, Your current score is {score}")
        a = b
        b = random.choice(game_data.data)
    if guess != answer:
        print(f"Sorry, that's wrong. Final score: {score}")
        break