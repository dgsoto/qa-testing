from utils.api_client import TrelloClient
from entities.board import Board

class BoardsModule:
    def __init__(self):
        self.client = TrelloClient()

    def get_boards(self):
        boards_data = self.client.get_boards()
        return [Board(b['id'], b['name'], b['closed']) for b in boards_data]

    def create_board(self, name):
        board_data = self.client.create_board(name)
        return Board(board_data['id'], board_data['name'], board_data['closed'])

    def delete_board(self, board_id):
        board_data = self.client.delete_board(board_id)
        return board_data

    def get_first_list_id_from_board_id(self, board_id):
        return self.client.get_first_list_id_from_board_by_id(board_id)
