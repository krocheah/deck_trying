from flask import Flask, render_template
from api import DeckOfCardsgApi
from game import ShowCards

app = Flask(__name__)

@app.route('/')
def index():

    deck_id = ShowCards.set_game_up()

    response = ShowCards.get_player_hands(deck_id)
    print(response)
    
    return render_template("index.html", cards=response)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080, debug = True)
