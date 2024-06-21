import pytest
from modules.boards import BoardsModule
from entities.board import Board

class TestBoards:
    @classmethod
    def setup_class(cls):
        cls.boards_module = BoardsModule()
        cls.test_board = None

    def setup_method(self, method):
        if method.__name__ == 'test_create_board':
            self.test_board = self.boards_module.create_board('Temporary Board')

    def teardown_method(self, method):
        if method.__name__ == 'test_create_board' and self.test_board:
            self.boards_module.delete_board(self.test_board.id)

    @classmethod
    def teardown_class(cls):
        pass

    def test_get_boards(self):
        boards = self.boards_module.get_boards()
        assert isinstance(boards, list)
        assert all(isinstance(board, Board) for board in boards)

    def test_create_board(self):
        board = self.test_board
        assert board.name == 'Temporary Board'
