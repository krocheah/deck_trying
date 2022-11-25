from api import DeckOfCardsgApi

# DECKID = DeckOfCardsgApi.get_deck_id()
PLAYERS = []

class ShowCards:

    @staticmethod
    def set_game_up():
        deck_id = (DeckOfCardsgApi.get_deck_id()).get("deck_id")

        iter = int(52/13)

        for i in range(iter):
            cards = ''
            one_set_of_cards = DeckOfCardsgApi.get_cards(deck_id, 13)
            
            PLAYERS += [
                {
                    "player_name": f"Player{i+1}",
                    "player_cards": one_set_of_cards
                }
            ]

            for x in range(13):
                cards += one_set_of_cards.get("cards")[x].get("code")+","

            response = DeckOfCardsgApi.set_pile(deck_id, cards, f"Player{i+1}")

            if response.get("success") != True:
                return "Error!"
            
        return deck_id

    def get_player_hands(deck_id):
        # response = DeckOfCardsgApi.get_pile(deck_id, players="Player1")
        return PLAYERS