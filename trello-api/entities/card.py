"""
Este módulo define la clase Card, que representa una tarjeta de Trello.
"""

class Card:
    """
    Representa una tarjeta de Trello.
    """
    def __init__(self, card_id, name, id_list):
        """
        Constructor de la clase Card.
        Args:
            card_id (str): El ID de la tarjeta.
            name (str): El nombre de la tarjeta.
            id_list (str): El ID de la lista a la que pertenece la tarjeta.
        """
        self.id = card_id
        self.name = name
        self.id_list = id_list

    def __repr__(self):
        """
        Representación en string de la clase Card.
        Returns:
            str: Una representación en string del objeto Card.
        """
        return f"Card(id={self.id}, name='{self.name}', id_list='{self.id_list}')"

    def move_to_list(self, new_list_id):
        """
        Mueve la tarjeta a una lista diferente.
        Args:
            new_list_id (str): El ID de la nueva lista a la que mover la tarjeta.
        """
        print(f"Moviendo tarjeta '{self.name}' a la lista con ID '{new_list_id}'")
        self.id_list = new_list_id
