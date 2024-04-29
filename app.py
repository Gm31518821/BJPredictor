pip install Flask
from flask import Flask, render_template, request
from blackjack_predictor import BlackjackPredictor

app = Flask(__name__)
predictor = BlackjackPredictor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/update_cards', methods=['POST'])
def update_cards():
    if request.method == 'POST':
        selected_cards = request.form.getlist('selected_cards')
        selected_cards = [int(card) for card in selected_cards]
        predictor.update_cards_dealt(selected_cards)
        return "Cards updated successfully!"

@app.route('/calculate_next_card', methods=['GET'])
def calculate_next_card():
    if request.method == 'GET':
        next_card_outcome = predictor.calculate_next_card_outcome()
        return str(next_card_outcome)

if __name__ == '__main__':
    app.run(debug=True)
