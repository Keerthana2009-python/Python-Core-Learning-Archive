# 🔼🔽 Higher Lower Game

📌 **Project Overview**
This project is a terminal-based clone of the popular web game "Higher Lower". The application prompts players to compare two social media personalities, brands, or celebrities and guess who has a larger follower count. The game tracks your current score and continues sequentially until a single incorrect guess terminates the session.

🚀 **Features**
* **Dynamic Data Streaming:** Fetches comparative entity profiles (names, descriptions, and countries) at random out of an external structural data module.
* **Persistent Win Streak Chaining:** Progresses seamlessly by sliding previous target options forward into the primary comparison slot (`a = b`) after every successful guess.
* **Double ASCII Branding Layouts:** Renders separate custom stylized headings (`logo`) and dividing layout splits (`vs`) at specific execution boundaries.
* **Instant Terminal Buffer Flushes:** Employs large newline multiplication lines (`\n` * 20) between rounds to maintain a neat interface and prevent answer peeking.

🛠 **Technologies Used**
* Python 3
* External modular data mapping and configurations
* Infinite control loops with manual termination markers (`break`)

📂 **Module Structure Details**
* `main.py`: Drives structural choice calculations, tracks current scoring tallies, and validates input strings against follower fields.
* `game_data.py`: Stores the array database housing descriptive entities and true follower count metric integers.
* `art.py`: Houses both the typography logo elements and the classic versus visual partition graphics.

▶️ **Running the Project**

### Prerequisites
Make sure Python 3 is installed on your operating system and all three script elements (`main.py`, `game_data.py`, and `art.py`) rest inside the same directory level.

### Execution
Run the driver file via your terminal prompt workspace:
```bash
python main.py
```

📸 **Example Output Execution**
```bash
[ASCII Art Logo Displays Here]

Compare A: Instagram, a Social media platform, from United States
[ASCII Art VS Displays Here]
Against B: Cristiano Ronaldo, a Footballer, from Portugal
Who has more followers? Type 'A' or 'B': a

[Screen Clears]

[ASCII Art Logo Displays Here]
You're right!, Your current score is 1
Compare A: Cristiano Ronaldo, a Footballer, from Portugal
[ASCII Art VS Displays Here]
Against B: Ariana Grande, a Musician and actress, from United States
Who has more followers? Type 'A' or 'B': 
```

📚 **Concepts Practiced**
* Nested Dictionary Reading and Attribute Extracting Techniques
* Interactive Data Shuffling and Sequential List Replacements
* Character Case Normalization and Validation Loops
* State-Accumulation Tracker Layout Mechanics
