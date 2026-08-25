# 🐍 Snake Game (with High Score Persistence)

📌 **Project Overview**
This project is an object-oriented, 2D Snake game built with Python's Turtle graphics framework. The application handles segmented movement tracking, dynamic body elongation upon food consumption, collision boundary checks, and reads/writes to a local text file tracking an all-time persistent player high score across separate game sessions.

🚀 **Features**
* **Object-Oriented Architecture:** Decouples game components cleanly into dedicated classes for the snake body, random food generation, and scoreboard tracking.
* **Persistent High Score Memory:** Integrates direct File I/O stream handling (`data.txt`) to dynamically load and overwrite the top score so progress is saved when closing the game.
* **Segmented Follower Physics:** Updates body segments backwards sequentially from tail to head, creating a fluid, realistic slithering path.
* **Non-Reversible Direction Gates:** Protects steering logic by blocking illegal inputs that would force the snake to immediately fold back into its own neck segment.

🛠 **Technologies Used**
* Python 3
* Native `turtle` canvas rendering engine
* File Input/Output workflows (`open()`, `read()`, `write()`)

📂 **Module Structure Details**
* `main.py`: Drives the main application lifecycle loop, screen coordinate listener trees, and component interaction tests.
* `Snake.py`: Manages coordinate offsets, segment arrays, structural body resets, and direction state boundaries.
* `food.py`: Inherits canvas rendering properties to instantiate downscaled blue target entities at randomized intervals.
* `scoreboard.py`: Draws and updates string metrics to screen while handling high-score comparison logs and resetting state fields.
* `data.txt`: Local database holding the single integer string tracking the highest score achieved.

▶️ **Running the Project**

### Prerequisites
Make sure Python 3 is installed on your operating system and all 5 files sit cleanly within the same project directory level.

### Execution
Run the driver file via your choice of terminal engine:
```bash
python main.py
```

🎮 **Game Controls**
* Use the **Up Arrow** key to travel upward.
* Use the **Down Arrow** key to drop downward.
* Use the **Left Arrow** key to turn left.
* Use the **Right Arrow** key to turn right.

📸 **Visual Representation**
```text
[A black canvas loads displaying a live white segmented snake, a blue circle food item, and a top-centered score dashboard metrics track]
```

📚 **Concepts Practiced**
* Stream Processing and Persistent System Local File Writes
* Segment Collection Subscriptions and Positional Coordinate Mapping
* List Array Slicing Mechanics to Evaluate Tail Collision Overlaps (`snake.segments[1:]`)
* Double-Buffer Synchronization Pipelines (`screen.tracer(0)` and `screen.update()`)
