from utils.api_client import TrelloClient
from entities.card import Card

class CardsModule:
    def __init__(self):
        self.client = TrelloClient()

    def create_card(self, list_id, name):
        card_data = self.client.create_card(list_id, name)
        return Card(card_data['id'], card_data['name'], card_data['idList'])

    def get_cards_in_list(self, list_id):
        cards_data = self.client.get_cards_in_list(list_id)
        return [Card(c['id'], c['name'], c['idList']) for c in cards_data]

    def delete_card(self, card_id):
        self.client.delete_card(card_id)
