import random

def create_card(rank:str,suite:str):
    ranks = {'2' : 2 , '3' : 3 , '4' : 4 , '5' : 5 , '6' : 6 , '7' : 7 ,   '8' : 8 , '9' : 9 , '10' : 10 ,  'J' : 11 , 'Q' : 12 , 'K' : 13 , 'A' : 14}
    suites = ['H', 'C', 'D', 'S']
    if rank in ranks.keys() and suite in suites:
        return ({'rank': rank, 'suite': suite})
    else:
        return ('Incorrect suite or rank input')
    
def build_standard_deck() -> list[dict]:
    ranks = {'2' : '2' , '3' : '3' , '4' : '4' , '5' : '5' , '6' : '6' , '7' : '7' , '8' : '8' , '9' : '9' , '10' : '10' , 'J' : 11 , 'Q' : 12 , 'K' : 13 , 'A' : 14}
    suites = ['H', 'C', 'D', 'S']
    deck = []
    for rank in ranks:
        for suite in suites:
            deck.append(create_card(rank, suite))
    return deck

def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    for run in range(swaps):
        index1 = random.randrange(len(deck))
        index2 = random.randrange(len(deck))
        while (index1 == index2) or (deck[index1]['suite'] == 'H' and index2 % 5 != 0) or (deck[index1]['suite'] == 'C' and index2 % 3 != 0) or (deck[index1]['suite'] == 'D' and index2 % 2 != 0) or (deck[index1]['suite'] == 'S' and index2 % 7 != 0):
            index2 = random.randrange(len(deck))
        deck[index1], deck[index2] = deck[index2], deck[index1]
    return deck





