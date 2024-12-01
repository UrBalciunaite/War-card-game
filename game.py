class Card:
    def __init__(self, XXX):
        ...
    
    rank = {
        "Ace": 13,
        "King": 12,
        "Queen": 11,
        "Jack": 10,
        "Ten": 9,
        "Nine": 8,
        "Eight": 7,
        "Seven": 6,
        "Six": 5,
        "Five": 4,
        "Four": 3,
        "Three": 2,
        "Two": 1
    }
    
    suits = ["clubs", "diamonds", "hearts", "spades"]

    def compare_cards():
        ...

class Deck:
    def __init__(self, XXX):
        ...

    # list of cards

    def shuffle():
        ...

    def deal():
        ...

class Player:
    def __init__(self, XXX):
        ...

    # name
    # deck (a list of "Card" objects)

    def play_cards():
        ...

    def add_cards():
        ...

    def has_cards():
        ...

class Game:
    def __init__(self, XXX):
        ...
        
    # 2 players
    # round counter

    def play_round():
        ...

    def play():
        ...

    def handle_war():
        ...

def main():
    ...

if __name__=="__main__":
    main()