# 🏓 Pong Game

📌 **Project Overview**
This project is a complete, object-oriented 2D arcade Pong game built with Python's custom Turtle graphics canvas library. It features a fully functional two-player workspace configuration, automatic dynamic speed increments, custom bounding coordinate bounce mechanics, and a real-time retro scoring interface.

🚀 **Features**
* **Object-Oriented Architecture:** Decouples structural entities cleanly across localized sub-classes for optimized state management.
* **Intelligent Collision Physics:** Employs radial distance evaluation limits and coordinate triggers to manage vector reversals across walls and dynamic paddle obstacles.
* **Progressive Difficulty Scaling:** Accelerates ball movement metrics progressively (`move_speed *= 0.9`) after every successful paddle volley to escalate player challenge.
* **Asynchronous Keyboard Bindings:** Listens to event queues simultaneously via distinct key hooks for fluid independent double-player movement.

🛠 **Technologies Used**
* Python 3
* Native `turtle` graphics framework engine
* Clock synchronization libraries (`time.sleep`)

📂 **Module Structure Details**
* `main.py`: Synchronizes clock loops, binds operational inputs, checks coordinate bounds, and manages canvas refreshes.
* `paddle.py`: Instantiates geometric tracking entities capable of moving vertically along fixed side offsets.
* `ball.py`: Contains coordinate stepping logic, wall vector inversion routines, and score-event position resets.
* `scoreboard.py`: Inherits canvas rendering properties to update dynamic retro numerical layouts dynamically.

▶️ **Running the Project**

### Prerequisites
Make sure Python 3 is installed on your desktop operating system along with a graphical display window configuration.

### Execution
Ensure all four files reside together in the same directory workspace, then boot the script file via your terminal window:
```bash
python main.py
```

🎮 **Game Controls**
* **Left Paddle Player:** Use `w` to climb up, use `s` to drop down.
* **Right Paddle Player:** Use `Up` arrow to climb up, use `Down` arrow to drop down.

📸 **Visual Representation**
```text
[A black window launches rendering two white paddles, a central circle ball, and a retro score dashboard layout]
```

📚 **Concepts Practiced**
* Strict OOP Architecture Class Configurations and `super().__init__()` Parent Inheritance
* Asynchronous Coordinate Listening Flags (`screen.listen()` and `onkey()`)
* Canvas Multi-Buffer Update Overrides (`screen.tracer(0)` and `screen.update()`)
* Variable Vector Inversions for Mathematical Physics Simulation
