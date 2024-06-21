import pytest
from modules.cards import CardsModule
from modules.boards import BoardsModule
from entities.card import Card

class TestCards:
    @classmethod
    def setup_class(cls):
        cls.cards_module = CardsModule()
        cls.boards_module = BoardsModule()
        cls.test_board = cls.boards_module.create_board('Card-Test-Board')
        cls.test_list_id = cls.boards_module.get_first_list_id_from_board_id(cls.test_board.id)
        

    def setup_method(self, method):
        if method.__name__ == 'test_create_card':
            self.test_card = self.cards_module.create_card(self.test_list_id, 'Temporary-Card')

    def teardown_method(self, method):
        if method.__name__ == 'test_create_card' and self.test_card:
            pass  # Implement card deletion if needed

    @classmethod
    def teardown_class(cls):
        cls.boards_module.delete_board(cls.test_board.id)

    def test_create_card(self):
        card = self.test_card
        assert card.name == 'Temporary-Card'
        assert card.id_list == self.test_list_id
