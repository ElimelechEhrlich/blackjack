from deck import *
from player_io import *

def calculate_hand_value(hand: list[dict]) -> int:
    hand_value = 0
    for i in hand:
        try:
            i['rank'] = int(i['rank'])
            hand_value += i['rank']
        except:
            if i['rank'] != 'A':
                hand_value += 10
            elif i['rank'] == 'A':
                hand_value += 1       
    return hand_value

def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    player = player['hand']
    dealer = dealer['hand']
    for i in range(2):
        player.append(deck.pop(0))
        dealer.append(deck.pop(0))
    player_hand_value = calculate_hand_value(player)
    dealer_hand_value = calculate_hand_value(dealer)
    print (f'player: {player_hand_value}\ndealer: {dealer_hand_value}')
    print (len(deck))
    return 

def dealer_play(deck: list[dict], dealer: dict) -> bool:
    dealer_hand_value = 0
    while dealer_hand_value > 17:
        dealer.append(deck.pop(0))
        dealer_hand_value = calculate_hand_value(dealer)
    if dealer_hand_value > 21:
        print ('Value greater than 21. dealer loses.')
        return False
    elif dealer_hand_value < 17:
        return True
    
    
def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deck = shuffle_by_suit(build_standard_deck())
    player = player['hand']
    dealer = dealer['hand']
    deal_two_each(deck,player,dealer)
    while player_hand_value < 21:
        choice = ask_player_action()
        if choice == 'H':
            player.append(deck.pop(0))
            player_hand_value = calculate_hand_value(player)
        if choice == 'S':
            if dealer_play(deck,player,dealer):
                player_hand_value = calculate_hand_value(player)
                dealer_hand_value = calculate_hand_value(dealer)
                if player_hand_value > dealer_hand_value: 
                    print ('player winn')
                elif player_hand_value < dealer_hand_value: 
                    print ('dealer winn')
                else:
                    print ('draw!')
    return False
        
        
        


