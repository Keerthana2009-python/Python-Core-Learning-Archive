# 🍕 Python Pizza Deliveries

📌 **Project Overview**
This project is an interactive, command-line pizza ordering application built with Python. It prompts users to select their desired pizza size and select optional toppings like pepperoni and extra cheese, then calculates and displays the accurate final bill based on their choices.

🚀 **Features**
* **Dynamic Cost Calculation:** Processes different base prices for Small, Medium, and Large pizzas.
* **Conditional Add-ons:** Automatically scales topping prices (like pepperoni) based on the chosen pizza size.
* **Interactive Command-Line Interface:** Uses user inputs to guide the pricing logic.
* **Error Prevention:** Validates size inputs to prevent incorrect orders.

🛠 **Technologies Used**
* Python 3
* Built-in `input()` and conditional logic structures

📂 **Pricing Logic Breakdown**
* **Base Pizza Prices:**
  * Small Pizza (`S`): $15
  * Medium Pizza (`M`): $20
  * Large Pizza (`L`): $25
* **Pepperoni Add-on:**
  * For Small Pizza: +$2
  * For Medium/Large Pizza: +$3
* **Extra Cheese Add-on:**
  * For any size: +$1

▶️ **Running the Project**

### Prerequisites
Make sure Python 3 is installed on your operating system.

### Execution
Run the script file via your terminal:
```bash
python main.py
```

📸 **Example Output Execution**
```text
Welcome to Python Pizza Deliveries!
What size pizza do you want? S, M or L: M
Do you want pepperoni on your pizza? Y or N: y
Do you want extra cheese? Y or N: y
Your final bill is: $24.
```

📚 **Concepts Practiced**
* Control Flow Statements (`if` / `elif` / `else`)
* Nested Conditional Blocks
* Dynamic Variable Assignment and Arithmetic Operators (`+=`)
* User Input Handling and String Formatting (f-strings)
