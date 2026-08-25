# 🐢 Turtle Crossing Game

📌 **Project Overview**
This project is an object-oriented, 2D arcade crossing game built with Python's Turtle graphics framework, heavily inspired by Frogger. The player controls a turtle attempting to cross a busy highway filled with randomized, multi-coloured cars. Reaching the top finish line advances the game level, resetting the turtle's position.

🚀 **Features**
* **Object-Oriented Architecture:** Decouples game components cleanly into dedicated modules for player character physics, obstacle generation mechanics, and text dashboard tracking.
* **Randomized Traffic Generation:** Spawns rectangular car obstacles using geometric scale dimensions (`stretch_len=2`) at completely randomized vertical positions with a 1-in-6 chance loop filter.
* **Level Progression Metrics:** Automatically registers score advances, updates the scoreboard view, and resets the character to the starting line whenever the player clears the map area.
* **Proximity Collision Detection:** Utilizes geometric coordinate evaluations to actively scan radial distances between objects, safely triggering game over sequences upon impact.

🛠 **Technologies Used**
* Python 3
* Native `turtle` vector graphics canvas engine
* Time synchronization pipelines (`time.sleep`)

📂 **Module Structure Details**
* `main.py`: Synchronizes execution cycles, binds entry listening keys, loops through active segments, and triggers reset events.
* `player.py`: Defines class characteristics handling turtle coordinate tracking, standard step vectors, and finish line boundary triggers.
* `car_manager.py`: Instantiates, recolours, and scales geometric block traffic vectors while tracking speed scaling constraints.
* `scoreboard.py`: Draws and updates left-aligned text strings matching the current level or drops centered exit flags.

▶️ **Running the Project**

### Prerequisites
Make sure Python 3 is installed on your operating system and all 4 custom modules sit together inside the same folder directory level.

### Execution
Boot the master execution routine using your terminal workspace prompt:
```bash
python main.py
```

🎮 **Game Controls**
* Press the **Up Arrow** key to move your turtle character forward toward the finish line.

📸 **Visual Representation**
```text
[A white window launches displaying a black controllable turtle character climbing past scrolling multi-coloured square cars under a top-left level dashboard track]
```

📚 **Concepts Practiced**
* OOP Multi-Module File Separation Patterns
* Independent Instance Generation Arrays (`self.all_cars.append()`)
* Asynchronous Key Binding Triggers (`screen.onkey()`)
* Double-Buffer Performance Controls (`screen.tracer(0)` and `screen.update()`)
