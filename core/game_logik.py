def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    player = {"hand": [] }
    dealer = {"hand": [] }
    player['hand'].append(deck.pop(0))
    player['hand'].append(deck.pop(0))
    dealer['hand'].append(deck.pop(0))
    dealer['hand'].append(deck.pop(0))
    print (player)
    return player, dealer