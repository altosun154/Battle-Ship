Battleship Game 🛥️🎯
A simple console-based Battleship game implemented in Python for two players. Players take turns guessing coordinates to sink each other's fleet. The game features customizable board sizes and ship configurations, and includes modular design with separate classes for gameplay logic and board management.

🎮 Features
Two-player turn-based gameplay

Customizable board size and ship list

Interactive ship placement

Clear text-based interface

Modular codebase for easy maintenance and expansion

🧩 Project Structure
bash
Copy
Edit
.
├── board.py            # Contains Ship and Board classes
├── game.py             # Contains Player and BattleshipGame classes
├── main.py             # Main script to run the game
└── README.md           # Project documentation
🛠 Dependencies
Python 3.x

No external libraries required

🚀 Getting Started
Clone the Repository

bash
Copy
Edit
git clone https://github.com/yourusername/battleship-game.git
cd battleship-game
Run the Game

bash
Copy
Edit
python3 main.py
Follow the Prompts

Each player will be prompted to place their ships and take turns attacking.

⚙️ Configuration
Modify the main() function in main.py to adjust game settings:

python
Copy
Edit
board_size = 5                      # Adjust board dimensions (NxN)
ship_list = [5, 4, 3, 3, 2]         # Define ship lengths
📁 File Descriptions
main.py – The main entry point. Initializes the game and starts play.

board.py – Defines the Ship and Board classes, handling placement, attacks, and game state.

game.py – Contains the Player and BattleshipGame classes that manage player turns and the overall flow of the game.
