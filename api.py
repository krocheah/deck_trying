import requests

BASE_URL = "https://www.deckofcardsapi.com/api/deck/"
COUNT = "1"
# USERNAME = "merchant@test.com"
# PASSWORD = "123456"

class DeckOfCardsgApi:

    @staticmethod
    def get_deck_id():
        url = BASE_URL + "new/shuffle/"
        data = {
            "deck_count" : COUNT
        }

        response = requests.post(url=url, data=data)
        json =  response.json()

        # return {
        #     "deck": json.get("deck_id"),
        #     "remaining": json.get("remaining")
        # }

        return json