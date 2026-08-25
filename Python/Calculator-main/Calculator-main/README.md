# 🧮 Dynamic Console Calculator

📌 **Project Overview**
This project is an interactive, terminal-based calculator built with Python. It supports continuous mathematical operations by chaining calculations together using the previous result, or starting fresh with brand-new numbers. The architecture leverages first-class functions mapped inside a dictionary to handle arithmetic selections dynamically.

🚀 **Features**
* **Chained Calculations:** Dynamically accumulates results, allowing users to pass the current output straight into the next operation without resetting.
* **First-Class Function Mapping:** Links math operations directly to their respective function references within a dictionary for modular execution.
* **Continuous Execution Loop:** Automatically recurses the main initialization loop when starting a clean mathematical session.
* **Screen Refresh Clearing:** Employs vertical screen padding (`\n` * 20) between calculations to keep the terminal layout neat and legible.

🛠 **Technologies Used**
* Python 3
* Dictionary-based function dispatch tables
* Recursive function workflows

📂 **Module Structure Details**
* `main.py`: Drives inputs, handles calculations via the operational dictionary, and contains core game-state recursive loops.
* `art.py`: Stores the custom styled typographic math calculation logo printed at startup.

▶️ **Running the Project**

### Prerequisites
Make sure Python 3 is installed on your operating system and both `main.py` and `art.py` sit inside the same project folder.

### Execution
Run the driver script file via your terminal window:
```bash
python main.py
```

📸 **Example Output Execution**
```bash
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|

What is the first number?: 5
+
-
*
/
Pick an operation: *
What is the next number?: 3
5.0 * 3.0 = 15.0
Type 'y' to continue calculating with 15.0, or type 'n' to start a new calculation: n

[Screen Clears and Restarts]
```

📚 **Concepts Practiced**
* First-Class Functions and Dispatch Dictionaries
* While Loop Accumulation States
* Function Recursion for Flow Control
* Clean Console Interface Spacing Mechanics
