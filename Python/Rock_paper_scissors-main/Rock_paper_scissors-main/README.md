# 🪨📄✂️ Rock Paper Scissors Game

📌 **Project Overview**
This is a classic command-line implementation of the traditional Rock, Paper, Scissors game built with Python. Players compete directly against an AI computer that makes unpredictable, randomized selections. 

🚀 **Features**
* **ASCII Art Visuals:** Displays detailed text-art graphics for every choice made by the player or the computer.
* **Randomized AI Opponent:** Uses Python's native randomization libraries to ensure completely un-biased computer moves.
* **Instant Outcome Logic:** Evaluates win, lose, and draw mechanics instantly after the player inputs their turn.
* **Input Protection:** Includes basic boundary handling to detect when an invalid number is entered.

🛠 **Technologies Used**
* Python 3
* Built-in `random` module
* Conditional control flow logic

📂 **Game Rules & Inputs**
* **0:** Selects **Rock** (Beats Scissors, Loses to Paper)
* **1:** Selects **Paper** (Beats Rock, Loses to Scissors)
* **2:** Selects **Scissors** (Beats Paper, Loses to Rock)

▶️ **Running the Project**

### Prerequisites
Make sure Python 3 is installed on your operating system.

### Execution
Run the script file via your terminal:
```bash
python main.py
```

📸 **Example Output Execution**
```markdown
What you want to choose? Type 0 for rock, 1 for paper and 2 for scissors:
 0
You chose:

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

Computer chose:

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

You won!
```

📚 **Concepts Practiced**
* Multi-line String Literals (`'''`)
* List Data Structures for Asset Management
* External Library Module Integration (`import random`)
* Complex Nested Control Flow Structures (`if` / `elif` / `else`)
