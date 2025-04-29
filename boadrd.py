class Ship(object):
    """
    Represents a ship in the Battleship game.
    """

    def __init__(self, length, position, orientation, hit_count=0, is_sunk=False):
        """
        Initializes a Ship object.
        :param length: The length of the ship.
        :param position: Tuple representing the starting position of the ship.
        :param orientation: String representing the orientation of the ship ('h' for horizontal, 'v' for vertical).
        :param hit_count: Number of times the ship has been hit.
        :param is_sunk: Boolean indicating if the ship is sunk.
        """
        self.length = length
        self.position = tuple(position)
        self.orientation = str(orientation)
        self.hit_count = hit_count
        self.is_sunk = is_sunk

    def get_positions(self):
        """
        Gets the positions occupied by the ship on the board.
        :return: List of tuples representing the ship's positions.
        """
        positions = []
        if self.orientation == "h":
            for i in range(self.length):
                positions.append((self.position[0], self.position[1] + i))
        elif self.orientation == "v":
            for i in range(self.length):
                positions.append((self.position[0] + i, self.position[1]))
        return positions

    def get_orientation(self):
        """
        Gets the orientation of the ship.
        :return: String representing the orientation ('h' for horizontal, 'v' for vertical).
        """
        return self.orientation

    def apply_hit(self):
        """
        Updates the hit count of the ship and checks if the ship is sunk.
        :return: Boolean indicating if the ship is sunk.
        """
        self.hit_count += 1
        if self.hit_count == self.length:
            self.is_sunk = True
        return self.is_sunk


class Board(object):
    """
    Represents the game board in the Battleship game.
    """

    def __init__(self, size):
        """
        Initializes a Board object.
        :param size: The size of the board (assumed to be a square).
        """
        self.size = size
        self.board = [[" "] * size for _ in range(size)]  # Create an empty board.
        self.ships = []  # List to store placed ships.

    def place_ship(self, ship):
        """
        Places a ship on the board.
        :param ship: Ship object to be placed on the board.
        """
        self.validate_ship_coordinates(ship)  # Check if ship placement is valid.
        self.ships.append(ship)  # Add the ship to the list of ships.
        for position in ship.get_positions():
            self.board[position[0]][position[1]] = "S"  # Mark ship positions on the board.

    def validate_ship_coordinates(self, ship):
        """
        Validates the coordinates of a ship to ensure it fits on the board and does not overlap with other ships.
        :param ship: Ship object to be validated.
        :raises RuntimeError: If the ship is out of bounds or overlaps with another ship.
        """
        i = 0
        for position in ship.get_positions():
            if i != 0:
                break
            try:
                if position[0] < 0 or position[0] >= self.size or position[1] < 0 or position[1] >= self.size:
                    i += 1
                    raise RuntimeError("Ship is out of bounds!")
                if self.board[position[0]][position[1]] == "S":
                    i += 1
                    raise RuntimeError("Ship coordinates are already taken!")
            except RuntimeError as error_message:
                print(error_message)

    def apply_guess(self, guess):
        """
        Applies a player's guess to the board, updating the board and ships accordingly.
        :param guess: Tuple representing the guessed coordinates.
        """
        if self.board[guess[0]][guess[1]] == "S":
            self.board[guess[0]][guess[1]] = "H"  # Mark the hit on the board.
            for ship in self.ships:
                for position in ship.get_positions():
                    if position == guess:
                        ship.apply_hit()  # Apply the hit to the corresponding ship.
            print("Hit!")
        else:
            self.board[guess[0]][guess[1]] = "M"  # Mark the miss on the board.
            print("Miss!")

    def __str__(self):
        """
        Returns a string representation of the board for display purposes.
        :return: String representing the current state of the board.
        """
        board_str = ""
        for row in self.board:
            for column in row:
                board_str += "[" + column + "]"
            board_str += "\n"
        return board_str
