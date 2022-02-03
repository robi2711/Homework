import random


used_cards = {
    'diamonds': [],
    'clubs': [],
    'hearts': [],
    'spades': [],
}
# Creates empty lists that can be appended for data processing
v = 'placeholder'
counter = 0
my_list = []
for i in range(1, 14):
    my_list.append(i)
# Makes a list with 10 numbers
num = 5
# int(input("How many cards to deal? > "))
# Tried to add user input but didn't work. Might come back at later stage
dictionary = {
    'diamonds':  my_list,
    'clubs': my_list,
    'hearts':  my_list,
    'spades':  my_list,
}
# After i did most of this i actually realized that this dictionary is kind of useless but its still cool to have
while counter != num:
    card_family = random.randint(0, 3)
    if card_family == 0:
        v = 'diamonds'
    elif card_family == 1:
        v = 'clubs'
    elif card_family == 2:
        v = 'hearts'
    elif card_family == 3:
        v = 'spades'
    # Chooses a random card suit
    """
    while len(used_cards[v]) == 10:
        card_family = random.randint(0, 3)
        if card_family == 0:
            v = 'diamonds'
        elif card_family == 1:
            v = 'clubs'
        elif card_family == 2:
            v = 'hearts'
        elif card_family == 3:
            v = 'spades'
    """
    # Again, for user input
    card_num = random.randint(1, 13)
    card_check = used_cards[v].count(card_num)
    while card_check != 0:
        card_num = random.randint(1, 13)
        card_check = used_cards[v].count(card_num)
    # Checks if card is already used
    used_cards[v].append(card_num)
    # Appends used cards to the empty lists at the top
    if card_num == 11:
        print(f"Jack of {v}")
    elif card_num == 12:
        print(f"Queen of {v}")
    elif card_num == 13:
        print(f"King of {v}")
    else:
        print(f"{dictionary[v][card_num-1]} of {v}")
    # Prints the card name and suit
    counter += 1
exit(1)
