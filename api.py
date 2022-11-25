import requests

BASE_URL = "https://www.deckofcardsapi.com/api/deck/"
COUNT = "1"
# USERNAME = "merchant@test.com"
# PASSWORD = "123456"

class DeckOfCardsgApi:

    @staticmethod
    def get_deck_id():
        url = BASE_URL + f"new/shuffle/?deck_count={COUNT}"

        response = requests.get(url=url)
        return response.json()

    def get_cards(deck_id, card_count):
        url = BASE_URL + f"{deck_id}/draw/?count={card_count}"

        response = requests.get(url=url)
        return response.json()

    def set_pile(deck_id, cards, player_name):
        url = BASE_URL + f"{deck_id}/pile/{player_name}/add/?cards={cards}"

        response = requests.get(url=url)
        return response.json()
    
    def get_pile(deck_id, players):
        url = BASE_URL + f"{deck_id}/pile/Player1/list"

        response = requests.get(url=url)
        return response.json()