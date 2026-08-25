# 🔏 Caesar Cipher Tool

📌 **Project Overview**
This project is an interactive, command-line cryptography application built with Python. It implements the classic Caesar Cipher algorithm, allowing users to encrypt (encode) or decrypt (decode) alphabetical messages by shifting characters by a user-defined numeric offset.

🚀 **Features**
* **Bidirectional Processing:** Supports both message encryption and decryption via a unified shifting function.
* **Character Protection:** Preserves spaces, numbers, and unique symbols exactly as typed without altering them during shifting.
* **Cyclic Shifting Wraparound:** Implements modulo arithmetic to handle shift numbers gracefully, even if the shift value exceeds the alphabet length.
* **Continuous Execution Loop:** Offers an interactive prompt allowing users to run multiple cryptographic operations without restarting the script manually.

🛠 **Technologies Used**
* Python 3
* External/Custom assets module (`art`)
* Mathematical indexing adjustments (`%` modulo operator)

📂 **Module Structure Details**
* `main.py`: Contains the core application loops, console inputs, and shifting calculation engine.
* `art.py`: Holds the stylized ASCII art configuration graphic printed upon startup.

▶️ **Running the Project**

### Prerequisites
Make sure Python 3 is installed on your operating system and both `main.py` and `art.py` exist in the same workspace directory.

### Execution
Run the script file via your terminal window:
```bash
python main.py
```

📸 **Example Output Execution**
```bash

 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88

Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world!
Type the shift number:
5
Here is the encoded result: mjqqt btwqi!
Type 'yes' if you want to go again. Otherwise, type 'no'.
no
Goodbye
```

📚 **Concepts Practiced**
* Dynamic Function Parameter Arguments (`def caesar(original_text...)`)
* Positional Indexing Configurations (`list.index()`)
* Mathematical Wrapping via Arithmetic Modulo Options
* Input Text Normalization Methods (`.lower()`)
