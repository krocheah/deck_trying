from api import DeckOfCardsgApi

# DECKID = DeckOfCardsgApi.get_deck_id()

class ShowCards:
    def show_all_cards(deck_id, remaining):

        iter = int(remaining/13)

        for i in range(iter):
            cards = ''
            one_set_of_cards = DeckOfCardsgApi.get_cards(deck_id, 13)

            for x in range(13):
                cards += one_set_of_cards.get("cards")[x].get("code")+","

            response = DeckOfCardsgApi.set_player_hands(deck_id, cards, f"Player{i+1}")

            if response.get("success") != True:
                return "Error!"

        return response