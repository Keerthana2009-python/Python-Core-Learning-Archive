# ☕ Coffee Machine Simulator

📌 **Project Overview**
This project is a terminal-based Coffee Machine simulation application built with Python. It manages recipe ingredients and pricing structures, tracks live machine ingredient levels, processes physical-equivalent coin inputs, manages transaction adjustments, and runs an administrator control gate system via specific keyword overrides.

🚀 **Features**
* **Dynamic Resource Checking:** Traverses current storage records to verify if adequate water, milk, and coffee levels exist before initiating any transaction.
* **Coin Value Calculation:** Accepts and aggregates distinct itemized counts for quarters ($0.25), dimes ($0.10), nickels ($0.05), and pennies ($0.01) into floating-point currency values.
* **Live System Analytics:** Features a hidden `report` query command enabling administrators to view left-over supply volumes along with total cumulative revenues instantly.
* **Smart Resource Deductions:** Subtracts recipe quantities cleanly from the base machine stocks only after financial processing successfully clears.

🛠 **Technologies Used**
* Python 3
* Multilayer nested tracking dictionaries (`MENU` and `resources`)
* Floating-point mathematical transaction adjustments (`round()`)

📂 **Core Function Modules**
* `is_resource_sufficient()`: Scans ingredient thresholds to permit or deny beverage requests.
* `process_coins()`: Manages direct itemized integer currency prompts to compute overall coin values.
* `is_transaction_successful()`: Authorizes drink production, appends profit balances, and calculates change values.
* `make_coffee()`: Modifies tracking values and delivers the terminal asset product.

▶️ **Running the Project**

### Prerequisites
Make sure Python 3 is installed on your operating system.

### Execution
Run the driver script file via your terminal window:
```bash
python main.py
```

📸 **Example Output Execution**
```bash
What would you like? (espresso/latte/cappuccino): espresso
Please insert coins.
how many quarters?: 6
how many dimes?: 0
how many nickles?: 0
how many pennies?: 0
Here is $0.0 in change.
Here is your espresso ☕️. Enjoy!
What would you like? (espresso/latte/cappuccino): report
Water: 250ml
Milk: 200ml
Coffee: 82g
Money: $1.5
What would you like? (espresso/latte/cappuccino): off
```

📚 **Concepts Practiced**
* Multi-Level Dictionary Manipulation Techniques
* Global State Variable Control Modifiers (`global`)
* Dynamic Function Composition workflows with Booleans
* User Command Hidden Control Gate Overrides
