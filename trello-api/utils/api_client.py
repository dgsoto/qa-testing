import requests
from utils.config import BASE_URL, API_KEY, TOKEN

class TrelloClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.auth_params = {
            'key': API_KEY,
            'token': TOKEN
        }

    def get_boards(self):
        url = f'{self.base_url}/members/me/boards'
        response = requests.get(url, params=self.auth_params)
        response.raise_for_status()
        return response.json()

    def create_board(self, name):
        url = f'{self.base_url}/boards/'
        params = {
            'name': name,
            **self.auth_params
        }
        response = requests.post(url, params=params)
        response.raise_for_status()
        return response.json()

    def delete_board(self, board_id):
        url = f'{self.base_url}/boards/{board_id}'
        response = requests.delete(url, params=self.auth_params)
        response.raise_for_status()
        return response.json()

    def get_first_list_id_from_board_by_id(self, board_id):
        url = f'{self.base_url}/boards/{board_id}/lists'
        response = requests.get(url, params=self.auth_params)
        response.raise_for_status()
        lists = response.json()
        if lists:
            print(lists)
            return lists[0]['id']
        else:
            raise ValueError("No lists found in the newly created board")

    def create_card(self, list_id, name):
        url = f'{self.base_url}/cards'
        params = {
            'idList': list_id,
            'name': name,
            **self.auth_params
        }
        response = requests.post(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_cards_in_list(self, list_id):
        url = f'{self.base_url}/lists/{list_id}/cards'
        response = requests.get(url, params=self.auth_params)
        response.raise_for_status()
        return response.json()

    def delete_card(self, card_id):
        url = f'{self.base_url}/cards/{card_id}'
        response = requests.delete(url, params=self.auth_params)
        response.raise_for_status()
        return response.json()
