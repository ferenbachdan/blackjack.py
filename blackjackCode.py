import random


def initialise_variables():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    player_cards = []
    dealer_cards = []
    return(cards, player_cards, dealer_cards)


def deal_card(cards):
    return random.choice(cards)


def calculate_hand_value(hand):
    total = sum(hand)
    ace_count = hand.count(11)

    # Adjust aces if bust
    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1

    return total


def starting_hand(cards, player_cards, dealer_cards):
    for _ in range(2):
        player_cards.append(deal_card(cards))
        dealer_cards.append(deal_card(cards))

    print(f"Your cards: {player_cards}")
    print(f"Dealer shows: {dealer_cards[0]}")

    return player_cards, dealer_cards


def player_turn(cards, player_cards):
    while True:
        player_value = calculate_hand_value(player_cards)

        if player_value > 21:
            print(f"You are on {player_value}. You are bust.")
            break

        choice = input(f"You are on {player_value}. Hit or stand? ").lower()

        if choice == "hit":
            new_card = deal_card(cards)
            player_cards.append(new_card)
            print(f"You drew: {new_card}")
        elif choice == "stand":
            break
        else:
            print("Invalid input. Please type 'hit' or 'stand'.")

    return calculate_hand_value(player_cards)


def dealer_turn(cards, dealer_cards):
    print(f"\nDealer's full hand: {dealer_cards}")

    while calculate_hand_value(dealer_cards) < 17:
        new_card = deal_card(cards)
        dealer_cards.append(new_card)
        print(f"Dealer draws: {new_card}")

    dealer_value = calculate_hand_value(dealer_cards)
    print(f"Dealer ends on {dealer_value}")

    return dealer_value


def determine_winner(player_value, dealer_value):
    print("\nFinal Results:")
    print(f"Your total: {player_value}")
    print(f"Dealer total: {dealer_value}")

    if player_value > 21:
        print("You lost! (Bust)")
    elif dealer_value > 21:
        print("You won! (Dealer bust)")
    elif player_value > dealer_value:
        print("You won!")
    elif player_value < dealer_value:
        print("You lost!")
    else:
        print("Tie!")

#organise dataflow
def play_game():
    cards, player_cards, dealer_cards = initialise_variables()

    player_cards, dealer_cards = starting_hand(cards, player_cards, dealer_cards)

    player_value = player_turn(cards, player_cards)

    if player_value <= 21:
        dealer_value = dealer_turn(cards, dealer_cards)
    else:
        dealer_value = calculate_hand_value(dealer_cards)

    determine_winner(player_value, dealer_value)


# Run the game
play_game()