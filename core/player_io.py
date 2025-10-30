def ask_player_action() -> str:
    choice = str(input('HIT OR STAND? H/S '))
    if choice != 'H' and choice != 'S':
        return ask_player_action()
    return choice