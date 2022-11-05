from flask import Flask, render_template
from api import DeckOfCardsgApi
from game import ShowCards

app = Flask(__name__)

@app.route('/')
def index():
    data = DeckOfCardsgApi.get_deck_id()

    response = ShowCards.show_all_cards(data.get("deck_id"), data.get("remaining"))
    print(response)
    return render_template("index.html", cards=response)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080, debug = True)
