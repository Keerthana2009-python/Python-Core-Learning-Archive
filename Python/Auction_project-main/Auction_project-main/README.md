# 🔨 Secret Auction Program

📌 **Project Overview**
This project is a blind or secret auction utility built with Python that runs directly in the command-line interface. It allows multiple users to anonymously submit their names and bids into a private ledger, clears the screen between entries to prevent peeking, and automatically calculates the highest bidder when the bidding period closes.

🚀 **Features**
* **Blind Ledger Storage:** Dynamically populates a dictionary data structure with names as unique keys mapped to integer bid amounts.
* **Screen Clearing Mechanism:** Uses extensive string-multiplied terminal spacing (`\n` * 20) to hide previous entries and preserve bidding secrecy.
* **Automated Winner Calculation:** Iterates through collection records to find and return the maximum bid amount along with the buyer's name.
* **Continuous Entry Loop:** Runs smoothly inside a control loop until the administrator explicitly stops the process by choosing 'no'.

🛠 **Technologies Used**
* Python 3
* External graphics module (`art`)
* Dynamic collection mapping (Python Dictionaries)

📂 **Module Structure Details**
* `main.py`: Contains the interactive loop structure, record assignment syntax, and maximum value tracking functions.
* `art.py`: Houses the specific stylized auction hammer ASCII art logo rendered upon initialization.

▶️ **Running the Project**

### Prerequisites
Make sure Python 3 is installed on your operating system and both `main.py` and `art.py` exist within the same directory.

### Execution
Run the script file via your terminal window:
```bash
python main.py
```

📸 **Example Output Execution**
```bash
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\

What is your name?: Alice
What is your bid?: $150
Are there any other bidders? Type 'yes or 'no'.
yes

[Screen Clears]

What is your name?: Bob
What is your bid?: $210
Are there any other bidders? Type 'yes or 'no'.
no
The winner is Bob with a bid of $210
```

📚 **Concepts Practiced**
* Key-Value Pair Operations and Dictionary Traversal
* Screen Buffering and Terminal Formatting Emulation
* Maximum-Value Tracking Algorithms
* Intermittent Loop Termination and Logical Evaluation Flag Control
