from board import Ship, Board  # Importing Ship and Board classes from the 'board' module.

## Uncomment the following lines when you are ready to do input/output tests!
## Make sure to uncomment when submitting to Codio.
import sys


def input(prompt=None):
    """
    Custom input function to handle user input.
    :param prompt: Optional prompt to display to the user.
    :return: User input as a string.
    """
    if prompt is not None:
        # If a prompt is provided, display it without a newline.
        print(prompt, end="")
    aaa_str = sys.stdin.readline()  # Read a line of input from the user.
    aaa_str = aaa_str.rstrip("\n")  # Remove the trailing newline character from the input.
    print(aaa_str)  # Print the cleaned input (useful for debugging).
    return aaa_str  # Return the cleaned input as a string.


class Player(object):
    """
    Represents a player in the Battleship game.
    """

    def __init__(self, name, board, ship_list):
        """
        Initializes a Player object.
        :param name: The name of the player.
        :param board: The player's game board.
        :param ship_list: List of ship sizes for the player.
        """
        self.name = name
        self.board = board
        self.ship_list = ship_list
        self.guesses = []  # Initialize an empty list to store the player's guesses.

    def validate_guess(self, guess):
        """
        Validates if the given guess is valid.
        :param guess: Tuple representing the guessed coordinates.
        :raises RuntimeError: If the guess is not a valid location or has already been made.
        """
        if guess[0] < 0 or guess[0] >= self.board.size or guess[1] < 0 or guess[1] >= self.board.size:
            # Check if the guess is within the valid range of the board.
            raise RuntimeError("Guess is not a valid location!")
        if guess in self.guesses:
            # Check if the guess has already been made.
            raise RuntimeError("This guess has already been made!")

    def get_player_guess(self):
        """
        Gets a valid guess from the player.
        :return: Tuple representing the guessed coordinates.
        """
        guess = input("Enter your guess: ")  # Prompt the player to enter a guess.
        guess = guess.split(",")  # Split the input string to get coordinates.
        guess = (int(guess[0]), int(guess[1]))  # Convert the coordinates to integers.
        self.validate_guess(guess)  # Validate the guessed coordinates.
        self.guesses.append(guess)  # Add the guess to the list of guesses.
        return guess

    def set_all_ships(self):
        """
        Sets all the ships on the player's board based on user input.
        """
        check = {}  # Initialize a dictionary to keep track of ship positions and orientations.
        for s in self.ship_list:
            t = True
            while t:
                position = input("Enter the coordinates of the ship of size {}: ".format(s))  # Prompt for ship coordinates.
                position = position.split(",")  # Split the input string to get coordinates.
                position = (int(position[0]), int(position[1]))  # Convert the coordinates to integers.
                while True:
                    orientation = input("Enter the orientation of the ship of size {}: ".format(s))  # Prompt for ship orientation.
                    orientation = orientation.lower()  # Convert the orientation to lowercase.
                    if orientation == "h" or orientation == "v":
                        break
                if position not in check or check[position] != orientation:
                    # Check if the chosen position is valid and the orientation is not conflicting.
                    check[position] = orientation
                    self.ship = Ship(s, position, orientation)  # Create a Ship object.
                    self.board.place_ship(self.ship)  # Place the ship on the board.
                    t = False
                elif check[position] == orientation:
                    self.board.validate_ship_coordinates(self.ship)  # Validate ship coordinates.

class BattleshipGame(object):
    """
    Represents the Battleship game.
    """

    def __init__(self, player1, player2):
        """
        Initializes a BattleshipGame object.
        :param player1: The first player.
        :param player2: The second player.
        """
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.other_player = player2
        self.game_over = False  # Initialize the game_over flag.

    def check_game_over(self):
        """
        Checks if the game is over and returns the winner's name.
        :return: The name of the winner or an empty string if the game is not over.
        """
        player1_ships = 0
        player2_ships = 0
        ship_sunk = False
        for i in self.current_player.board.board:
            for j in i:
                if j == "S":
                    player1_ships += 1
        for i in self.other_player.board.board:
            for j in i:
                if j == "S":
                    player2_ships += 1
        if player2_ships == 0:
            return self.other_player.name
        elif player1_ships == 0:
            return self.current_player.name
        else:
            return ""

    def display(self):
        """
        Displays the current state of the game boards.
        """
        print(self.current_player.name + "'s board:")
        print(self.current_player.board)
        print(self.other_player.name + "'s board:")
        print(self.other_player.board)

    def play(self):
        """
        Initiates and manages the gameplay loop.
        """
        self.display()
        game = "c"
        while game == "c":

            print("{}'s turn.".format(self.current_player.name))
            guess = self.current_player.get_player_guess()
            self.current_player.board.apply_guess(guess)
            winner = self.check_game_over()
            if winner == self.current_player.name:
                print("{} wins!".format(winner))
                return
            print("{}'s turn.".format(self.other_player.name))
            guess = self.other_player.get_player_guess()
            self.other_player.board.apply_guess(guess)
            winner = self.check_game_over()
            if winner == self.other_player.name:
                print("{} wins!".format(winner))
                return
            game = input("Continue playing?: ")  # Prompt for continuing the game.
            self.display()
