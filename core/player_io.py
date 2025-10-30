def ask_player_action() -> str:
    choice = str(input('HIT OR STAND? H/S '))
    choice = choice.upper()
    if choice != 'H' and choice != 'S':
        ask_player_action()
    return choice
