from core.game_logik import run_full_game
from core.deck import *


if __name__ == "__main__":
    deck = shuffle_by_suit(build_standard_deck())
    player = {'hand':[]}
    dealer = {'hand':[]}
    run_full_game(deck,player,dealer)