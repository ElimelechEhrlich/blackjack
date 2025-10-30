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