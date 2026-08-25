# 🎢 Rollercoaster Ticket Machine

📌 **Project Overview**
This project is an interactive, command-line ticket pricing utility built with Python. It qualifies users based on their height, calculates base ticket rates using distinct age-bracket milestones, offers a special promotional free-tier waiver, and handles custom digital photo add-on transactions dynamically.

🚀 **Features**
* **Safety Height Validation:** Blocks access immediately if the passenger does not meet the minimum safety height requirement of 120 cm.
* **Tiered Age Pricing Structure:** Automatically segments ticket costs into Child ($5), Youth ($7), and Adult ($12) categories.
* **Mid-Life Crisis Free Waiver:** Features a special conditional range filter that completely zeroes out ticket costs for riders aged between 45 and 55 inclusive.
* **Dynamic Add-on Billing:** Appends a $3 service fee to the cumulative bill if the customer requests a souvenir photo snapshot.

🛠 **Technologies Used**
* Python 3
* Nested structural conditional blocks (`if` / `elif` / `else`)
* Integer type-casting mutations (`int()`)

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
Welcome to the rollercoaster!
What is your height in cm? 175
You can ride the rollercoaster!
What is your age? 25
Adult tickets are $12.
Do you want a photo taken? Y or N. Y
Your final bill is $15
```

📚 **Concepts Practiced**
* Multi-Tier Nested Control Flow Operations
* Compound Logical Condition Evaluations (`and`)
* Mathematical Accumulation Updates (`+=`)
* Clean String Literal Output Interweaving (f-strings)
