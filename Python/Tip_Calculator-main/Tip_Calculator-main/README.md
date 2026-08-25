# 💸 Tip Calculator

📌 **Project Overview**
This project is an interactive, command-line financial utility built with Python. It prompts users to enter a total bill amount, select a target tip percentage milestone, and input the number of individuals splitting the cost. The engine then processes the cumulative mathematical distributions to return a perfectly rounded payment split per person.

🚀 **Features**
* **Interactive Dynamic Inputs:** Captures live financial metrics, percentage values, and group sizes sequentially through console user prompts.
* **Proportional Tip Compounding:** Translates integer percentages dynamically into float multipliers to evaluate total gratuity values accurately.
* **Automated Cost Splitting:** Combines base costs with secondary tip distributions, dividing totals cleanly across custom group counts.
* **Precise Currency Rounding:** Implements float precision clipping via the built-in mathematical `round()` method down to two decimal places.

🛠 **Technologies Used**
* Python 3
* Floating-point and integer type-casting modifications (`float()` and `int()`)
* String literal variable insertion formatting (f-strings)

📂 **Module Structure Details**
* `main.py`: Drives input prompt parsing, floating-point math aggregation stacks, and handles final split output text strings.

▶️ **Running the Project**

### Prerequisites
Make sure Python 3 is installed on your operating system terminal workspace.

### Execution
Run the script file via your terminal prompt:
```bash
python main.py
```

📸 **Example Output Execution**
```bash
Welcome to the tip calculator!
What was the total bill? $150.00
What percentage tip would you like to give? 10 12 15: 12
How many people to split the bill? 5
Each person should pay: $33.6
```

📚 **Concepts Practiced**
* Standard Terminal Multi-Type Input Conversions
* Fractional Mathematical Percentage Allocations
* Floating-Point Variable Precision Adjustments
* Scalable Direct String Arithmetic Interpolation
