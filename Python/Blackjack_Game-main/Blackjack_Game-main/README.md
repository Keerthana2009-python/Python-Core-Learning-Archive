# 🃏 Command-Line Blackjack Game

📌 **Project Overview**
This project is a terminal-based implementation of the classic casino card game Blackjack (also known as 21) built with Python. The application handles complex card deck drawing rules, manages dealer automation behavior up to minimum soft scores, evaluates dynamic Ace card values (flipping between 11 and 1 based on necessity), and tracks final victory conditions instantly.

🚀 **Features**
* **Dynamic Ace Scoring Evaluation:** Automatically shifts the mathematical value of an Ace card from 11 down to 1 if the player's cumulative score risks bursting past 21.
* **Natural Blackjack Detection:** Features precise conditional checkpoints to instantly recognize a raw 21-point structural victory (Score = 0) from the initial dealing turn.
* **Dealer Intelligence Automation:** Implements a computerized dealer loop that intelligently hits or holds based on optimal standard protocol boundaries (holding on any score totaling 17 or higher).
* **Infinite Replay Iterations:** Operates within a structural wrapper sequence that safely flushes the terminal display matrix between rounds so users can restart playing instantly.

🛠 **Technologies Used**
* Python 3
* Built-in `random` module for unpredictable card distribution
* Multi-conditional logic maps and algorithmic function chaining

📂 **Module Structure Details**
* `main.py`: Houses card evaluation calculators, mathematical score rules, automated loops, and state-tracking functions.
* `art.py`: Contains the themed typographical ASCII art graphic displayed whenever a game round initializes.

▶️ **Running the Project**

### Prerequisites
Make sure Python 3 is installed on your operating system and both `main.py` and `art.py` sit comfortably inside the same active directory workspace.

### Execution
Run the driver script file using your choice of terminal engine:
```bash
python main.py
```

📸 **Example Output Execution**
```bash
Do you want to play a game of blackjack? Type 'y' or 'n': y

.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           

Your cards:, Current Score: 17
Computer's first card: 8
Type 'y' to get another card or type 'n' to pass: n
Your final hand:, final score: 17
Computer's final hand:, final score: 17
Draw
Do you want to play a game of blackjack? Type 'y' or 'n': 
```

📚 **Concepts Practiced**
* Advanced Array Injections and Element Mutation Methodologies
* Modularized Component Architectures and Positional Mapping Calls
* Flag-Controlled Conditional Iterations (`while not is_game_over`)
* Game-Logic Boundary Evaluation Sequences
