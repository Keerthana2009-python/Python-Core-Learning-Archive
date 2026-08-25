# 🔑 PyPassword Generator

📌 **Project Overview**
This project is an interactive, command-line password generation utility built with Python. It prompts users to define their target security requirements—specifying the exact count of letters, symbols, and numbers—and automatically builds a strong, highly secure randomized password.

🚀 **Features**
* **Custom Complexity Controls:** Allows users to define exact proportions of alphabetic characters, numeric digits, and unique symbols.
* **Dual Logic Preparation:** Contains structured framework pathways for both predictable ordered generation (sequential) and randomized shuffling layouts.
* **Cryptographic-Style Shuffling:** Utilizes list mutation mechanics to entirely randomize character positions, preventing predictable structural patterns.
* **Dynamic String Construction:** Reassembles randomized character arrays back into clean, copy-ready string formats.

🛠 **Technologies Used**
* Python 3
* Built-in `random` module (`random.choice` and `random.shuffle`)
* Sequential looping structures (`for` loops)

📂 **Character Pools Included**
* **Letters:** 52 characters (Full lower-case `a-z` and upper-case `A-Z`)
* **Numbers:** 10 digits (`0-9`)
* **Symbols:** 9 punctuation selections (`!`, `#`, `$`, `%`, `&`, `(`, `)`, `*`, `+`)

▶️ **Running the Project**

### Prerequisites
Make sure Python 3 is installed on your operating system.

### Execution
Run the script file via your terminal:
```bash
python main.py
```

📸 **Example Output Execution**
```bash
Welcome to the PyPassword Generator!
How many letters would you like in your password?
4
How many symbols would you like?
2
How many numbers would you like?
2
['K', 'g', 'r', 'm', '(', '+', '5', '0']
['r', '+', '0', 'g', '5', 'm', ')', 'K']
Your password is: r+0g5m$K
```

📚 **Concepts Practiced**
* Array/List Mutations and Shuffling Methods
* Multi-Type Array Iteration and Data Merging
* Algorithmic Complexity Shifts (Transitioning from Sequential to Randomized Logic)
* String and Array Conversion Mechanisms
