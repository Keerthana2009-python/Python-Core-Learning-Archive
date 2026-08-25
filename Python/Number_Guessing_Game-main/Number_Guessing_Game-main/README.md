# 🔢 Number Guessing Game

📌 **Project Overview**
This project is an interactive, command-line number-guessing game built with Python. The engine generates a pseudo-random integer between 0 and 100, prompts the user to select an operational difficulty tier, and manages an active countdown tracking structural guesses until the player either discovers the hidden target or exhausts their available attempts.

🚀 **Features**
* **Tiered Difficulty Scales:** Features a dual-difficulty entry switch allowing players to choose between 'easy' (10 attempts) or 'hard' (5 attempts).
* **Guided Feedback Clues:** Provides dynamic runtime hints ('Too high' or 'Too low') immediately after each input to assist users in narrowing down their search.
* **Input Boundary Protection:** Employs a robust loop structure at setup to continuously prompt the user until a valid difficulty selection is provided.
* **Live Attempt Tracker:** Actively prints real-time count metrics telling players exactly how many lifelines remain after every missed turn.

🛠 **Technologies Used**
* Python 3
* Built-in `random` module (`random.randint`)
* Infinite runtime verification loops (`while True`) with strict `break` logic

📂 **Module Structure Details**
* `main.py`: Drives interactive text prompts, comparison operations, and difficulty-based configuration metrics.
* `art.py`: Stores the styled numeric themed typographical ASCII art graphic printed upon launching the game.

▶️ **Running the Project**

### Prerequisites
Make sure Python 3 is installed on your operating system and both `main.py` and `art.py` sit in the same active workspace directory.

### Execution
Run the driver script file via your terminal window:
```bash
python main.py
```

📸 **Example Output Execution**
```bash

 /$$$$$$                                               /$$$$$$$$ /$$                       /$$   /$$                         /$$                          
 /$$__  $$                                             |__  $$__/| $$                      | $$$ | $$                        | $$                          
| $$  \__/ /$$   /$$  /$$$$$$   /$$$$$$$ /$$$$$$$         | $$   | $$$$$$$   /$$$$$$       | $$$$| $$ /$$   /$$ /$$$$$$/$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ 
| $$ /$$$$| $$  | $$ /$$__  $$ /$$_____//$$_____/         | $$   | $$__  $$ /$$__  $$      | $$ $$ $$| $$  | $$| $$_  $$_  $$| $$__  $$ /$$__  $$ /$$__  $$
| $$|_  $$| $$  | $$| $$$$$$$$|  $$$$$$|  $$$$$$          | $$   | $$  \ $$| $$$$$$$$      | $$  $$$$| $$  | $$| $$ \ $$ \ $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$  \ $$| $$  | $$| $$_____/ \____  $$\____  $$         | $$   | $$  | $$| $$_____/      | $$\  $$$| $$  | $$| $$ | $$ | $$| $$  | $$| $$_____/| $$      
|  $$$$$$/|  $$$$$$/|  $$$$$$$ /$$$$$$$//$$$$$$$/         | $$   | $$  | $$|  $$$$$$$      | $$ \  $$|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$$| $$      
 \______/  \______/  \_______/|_______/|_______/          |__/   |__/  |__/ \_______/      |__/  \__/ \______/ |__/ |__/ |__/|_______/  \_______/|__/      


Welcome to the Number Guessing Game!
I am thinking of a number between 0 and 100
Choose a difficulty. Type 'easy' or 'hard': hard
You have 5 attempts to guess the number
Make a guess: 50
Too low
Try again
You have 4 attempts remaining to guess the number
Make a guess: 75
You guessed the number
```

📚 **Concepts Practiced**
* Pseudo-Random Number Generation Implementations
* Flagless Intermittent Conditional Breaking (`while True` / `break`)
* Nested Multi-Branch Comparison Tree Logic (`if` / `elif` / `else`)
* Terminal Tracking Arithmetic Decrement Operations (`-=`)
