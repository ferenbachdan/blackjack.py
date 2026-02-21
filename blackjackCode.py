import random

# Create Deck and Shoe

def create_shoe(num_decks=6):
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
        "7": 7, "8": 8, "9": 9,
        "10": 10, "Jack": 10, "Queen": 10, "King": 10,
        "Ace": 11
    }

    single_deck = []

    for suit in suits:
        for rank, value in ranks.items():
            single_deck.append((rank, suit, value))

    shoe = single_deck * num_decks
    random.shuffle(shoe)

    return(shoe)

# Hand Value calculation

def calculate_hand_value(hand):
    total = sum(card[2] for card in hand)
    ace_count = sum(1 for card in hand if card[0] == "Ace")

    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1

    return(total)

# Deal Card

def deal_card(shoe):
    return shoe.pop()

# Starting hand

def starting_hand(shoe):
    player_hand = []
    dealer_hand = []

    for _ in range(2):
        player_hand.append(deal_card(shoe))
        dealer_hand.append(deal_card(shoe))

    return(player_hand, dealer_hand)

# Print Hand

def print_hand(owner, hand, hide_first=False):
    print(f"\n{owner}'s hand:")

    for i, card in enumerate(hand):
        if hide_first and i == 0:
            print("Hidden card")
        else:
            rank, suit, value = card
            print(f"{rank} of {suit} (Value: {value})")

    if not hide_first:
        print(f"Total value: {calculate_hand_value(hand)}")

# Player Turn

def player_turn(shoe, player_hand):
    while True:
        value = calculate_hand_value(player_hand)

        if value >= 21:
            break

        choice = input("\nHit or Stand? ").lower()

        if choice == "hit":
            card = deal_card(shoe)
            player_hand.append(card)
            print(f"You drew {card[0]} of {card[1]}")
        elif choice == "stand":
            break
        else:
            print("Invalid input.")

    return player_hand

# Dealer Turn

def dealer_turn(shoe, dealer_hand):
    while calculate_hand_value(dealer_hand) < 17:
        card = deal_card(shoe)
        dealer_hand.append(card)
        print(f"Dealer draws {card[0]} of {card[1]}")

    return(dealer_hand)

# Win Logic

def determine_winner(player_hand, dealer_hand):
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    print(f"\nFinal Player Total: {player_value}")
    print(f"Final Dealer Total: {dealer_value}")

    if player_value > 21:
        print("You bust. Dealer wins.")
    elif dealer_value > 21:
        print("Dealer busts. You win!")
    elif player_value > dealer_value:
        print("You win!")
    elif dealer_value > player_value:
        print("Dealer wins.")
    else:
        print("Push (Tie).")

# Main 

def main():
    shoe = create_shoe(6)

    player_hand, dealer_hand = starting_hand(shoe)

    print_hand("Dealer", dealer_hand, hide_first=True)
    print_hand("Player", player_hand)

    player_hand = player_turn(shoe, player_hand)

    if calculate_hand_value(player_hand) <= 21:
        print("\nDealer reveals hidden card:")
        print_hand("Dealer", dealer_hand)

        dealer_hand = dealer_turn(shoe, dealer_hand)

    determine_winner(player_hand, dealer_hand)


main()