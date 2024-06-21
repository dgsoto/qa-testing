"""
Board class
A class to store board information
"""
class Board:
    """
    Board class
    """
    def __init__(self, board_id, name, closed):
        """
        Constructor de la clase Board.
        Args:
            board_id (str): El ID del tablero.
            name (str): El nombre del tablero.
            closed (bool): Indica si el tablero está cerrado o no.
        """
        self.id = board_id
        self.name = name
        self.closed = closed

    def __repr__(self):
        """
        Representación en string de la clase Board.
        Returns:
            str: Una representación en string del objeto Board.
        """
        return f"Board(id={self.id}, name='{self.name}', closed={self.closed})"

    def is_open(self):  # Added a public method
        """
        Verifica si el tablero está abierto.
        Returns:
            bool: True si el tablero está abierto, False si está cerrado.
        """
        return not self.closed
