# 🍕 Python Pizza Deliveries

📌 **Project Overview**
This project is an interactive, command-line pizza ordering application built with Python. It prompts users to select their desired pizza size and toggle optional toppings like pepperoni and extra cheese, then calculates and displays the final bill based on their choices.

🚀 **Features**
* **Dynamic Cost Calculation:** Processes independent base prices for Small ($15), Medium ($20), and Large ($25) pizzas using a tiered conditional check.
* **Size-Scaled Toppings:** Automatically scales the cost of pepperoni based on the selected pizza size ($2 for Small, $3 for Medium/Large).
* **Flat-Rate Add-ons:** Appends a standard $1 fee for extra cheese regardless of the pizza size chosen.
* **Basic Input Warning:** Notifies the user if an invalid or unrecognized pizza size is entered during the initial prompt.

🛠 **Technologies Used**
* Python 3
* Conditionals and logical control flow structures (`if` / `elif` / `else`)
* String literal formatting (f-strings)

▶️ **Running the Project**

### Prerequisites
Make sure Python 3 is installed on your operating system.

### Execution
Run the script file via your terminal workspace:
```bash
python main.py
```

📸 **Example Output Execution**
```bash
Welcome to Python Pizza Deliveries!
What size pizza do you want? S, M or L: M
Do you want pepperoni on your pizza? Y or N: Y
Do you want extra cheese? Y or N: Y
Your final bill is: $24.
```

📚 **Concepts Practiced**
* Nested Conditional Blocks and Multi-Branch Decision Tree Execution
* Compound Mathematical Accumulation Syntax (`+=`)
* Text Prompt Formatting and Dynamic Value Variable Linking
