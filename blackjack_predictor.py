from collections import defaultdict

class BlackjackPredictor:
    def __init__(self):
        self.cards_dealt = defaultdict(int)
        self.remaining_decks = 6
    
    def update_cards_dealt(self, cards):
        for card in cards:
            self.cards_dealt[card] += 1
    
    def calculate_next_card_outcome(self):
        remaining_cards = self.remaining_decks * 52 - sum(self.cards_dealt.values())
        
        # Calculate the probability of each card
        card_probabilities = {card: (4 * self.remaining_decks - self.cards_dealt.get(card, 0)) / remaining_cards for card in range(1, 11)}
        
        # Calculate the expected value of the next card
        expected_value = sum(card * probability for card, probability in card_probabilities.items())
        
        return expected_value
