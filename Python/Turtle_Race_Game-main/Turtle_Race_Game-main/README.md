# 🐢 Multi-Turtle Racing Game

📌 **Project Overview**
This project is an interactive, graphical betting game built with Python's Turtle graphics library. Upon startup, the game initializes a racetrack with six uniquely colored turtles lined up at the starting gates. The player places a text-based bet on which color will cross the finish line first, after which the turtles race across the screen using randomized stepping distances.

🚀 **Features**
* **Dynamic Graphical Line-up:** Uses an automated loop to instantiate six unique turtle graphics components, spacing them out perfectly along the Y-axis coordinates.
* **Interactive Betting Interface:** Prompts players with a graphical pop-up text entry box (`screen.textinput`) to capture their preferred winning color choice before starting the race.
* **Randomized Movement Mechanics:** Loops through all active participants each frame, moving them forward by a pseudo-random integer step distance (`randint(0, 10)`).
* **Finish Line Detection:** Actively scans the X-coordinate (`xcor() > 230`) of every turtle to immediately stop the game loop, compare the result against the user's bet, and announce a win or loss accordingly.

🛠 **Technologies Used**
* Python 3
* Native `turtle` graphics and canvas display window framework
* Built-in `random` module (`randint` method)

📂 **Module Structure Details**
* `main.py`: Drives the entire standalone program layout, coordinates turtle grid setup loops, checks finish boundary crossings, and prints game results.

▶️ **Running the Project**

### Prerequisites
Make sure Python 3 is installed on your operating system and a desktop display environment is accessible for launching the graphical canvas window.

### Execution
Run the script file via your terminal window:
```bash
python main.py
```

🎮 **Game Controls**
1. A graphical text pop-up window will appear asking: *Which turtle will win the race? Enter a color:*
2. Type one of the available racer options exactly: `red`, `orange`, `yellow`, `green`, `blue`, or `purple`.
3. Watch the race unfold in the canvas window.

📸 **Example Output Execution**
```bash
# Terminal Console Display (If you guess correctly)
You've won! The red turtle is the winner!

# Terminal Console Display (If you guess incorrectly)
You've lost! The blue turtle is the winner!
```

📚 **Concepts Practiced**
* Coordinate Plane Mechanics and Dynamic Grid Positioning Loops
* Pop-up UI Prompt Event Capitalization & Processing (`.textinput()`)
* Object Instance Arrays for Handling Group Variable Iterations
* State-Flag Loop Control Workflows (`while is_race_on`)
