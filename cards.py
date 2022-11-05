import requests
from api import DeckOfCardsgApi

# DECKID = DeckOfCardsgApi.get_deck_id()

class ShowCards:
    def show_all_cards(deck_id, remaining):

        cards = []

        for i in range(remaining):
            response = requests.get(f"https://www.deckofcardsapi.com/api/deck/{deck_id}/draw/?count=1")

            cards.append(response.json().get("cards")[0].get("images").get("png"))
        return cards