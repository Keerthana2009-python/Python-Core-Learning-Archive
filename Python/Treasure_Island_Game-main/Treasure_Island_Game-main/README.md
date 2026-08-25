# 🏴‍☠️ Treasure Island Game

📌 **Project Overview**
This project is an interactive, text-based adventure game built with Python that takes players on a hazardous quest to locate hidden treasure. The application reads user choices sequentially, navigating through a strict multi-tiered branch structure where a single wrong decision results in an immediate game-over state.

🚀 **Features**
* **Thematic ASCII Art:** Greets players upon startup with a detailed, full-scale illustration of a treasure brick wall layout using safe raw string rendering (`r'''`).
* **Multi-Stage Decision Tree:** Paths are split across three distinct levels of interactive decision checkpoints (Crossroads, Lake Crossing, and Three Colored Doors).
* **Case-Insensitive Input Processing:** Integrates string normalization handling (`.lower()`) on all text inputs to ensure variation choices like "Left", "LEFT", and "left" match seamlessly.
* **Distinct Outlines for Game Failures:** Provides separate, unique terminal text descriptions for each failure state (falling into holes, getting attacked by fish, or stepping into trap rooms).

🛠 **Technologies Used**
* Python 3
* Multilayer nested conditional structures (`if` / `elif` / `else`)
* Case formatting standardizations (`.lower()`)

📂 **Module Structure Details**
* `main.py`: Contains the master application lifecycle script, ASCII presentation graphics, text prompts, and sequential game logic paths.

▶️ **Running the Project**

### Prerequisites
Make sure Python 3 is installed on your operating system terminal interface.

### Execution
Run the game driver file via your terminal window prompt:
```bash
python main.py
```

📸 **Example Output Execution**
```bash
[ASCII Art Bricks Logo Displays Here]

Welcome to Treasure Island.
Your mission is to find the treasure.
You're at a crossroad, where do you want to go? Type "left" or "right".
left
You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.
wait
You arrive at the island unharmed. There is house with 3 doors. One red, one yellow and one blue. Which colour do you choose?
yellow
You found the treasure. You Win!
```

📚 **Concepts Practiced**
* Multi-Tier Nested Conditional Logic Workflows
* Multi-Line Raw String Literal Assets (`r'''`)
* User Input Serialization and Normalization Methods
* Edge-Case Catching Failures via Comprehensive Catch-All Blocks (`else`)
