# 🪓 Hangman Game

📌 **Project Overview**
This project is an interactive, console-based implementation of the classic Hangman word-guessing game. The application dynamically chooses a hidden word from an expansive vocabulary library, manages a countdown of player lives, and renders structural ASCII art updates whenever an incorrect guess is made.

🚀 **Features**
* **Dynamic ASCII Asset Rendering:** Renders state-based gallows structures and thematic visual logo typography during runtime.
* **Duplicate Guess Alerts:** Actively checks user history to notify players when a character has already been attempted.
* **Granular State Display:** Shows hidden placeholders along with current remaining lifelines dynamically via the terminal.
* **Modular Asset Importing:** Distributes core variables across secondary modules to maintain a decoupled code structure.

🛠 **Technologies Used**
* Python 3
* Built-in `random` module
* Complex iterative evaluation blocks (`while` and `for` loops)

📂 **Module Structure Details**
* `main.py`: Drives core computational loops, tracks lifeline states, and handles inputs.
* `hangman_words.py`: Houses the list data array containing diverse, hard-to-guess terms.
* `hangman_art.py`: Stores structural row-string stages and primary game heading layouts.

▶️ **Running the Project**

### Prerequisites
Make sure Python 3 is installed on your operating system and all three game files exist inside the same directory level.

### Execution
Run the driver script file via your terminal window:
```bash
python main.py
```

📸 **Example Output Execution**
```bash
 _                                             

| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
pajama
Word to guess: ______
****************************6/6 LIVES LEFT****************************
Guess a letter: e
Word to guess: ______
You guessed e, that's not in the word. You lose a life.
  +---+
  |   |
  O   |
      |
      |
      |
=========
```

📚 **Concepts Practiced**
* Multi-File Module Importing (`from X import Y`)
* Multi-Line String Character Literal Handling (`r'''`)
* List Appends and Sequential Membership Evaluation (`in` / `not in`)
* Interactive State Management Loops
