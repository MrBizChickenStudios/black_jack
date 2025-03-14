import deck

deck = deck.Deck()
player_hand = []

deck.make_deck()
deck.shuffle_deck()
deck.deal_cards(player_hand, 2)

def show_cards():
    for card in player_hand:
        print(card.get_card())
show_cards()
def game_logic():
    card_sum = 0

    for card in player_hand:
        card_sum += card.vaule
        if card_sum > 21:
            print(f"You busted {card_sum} Game Over")
        if card_sum == 21:
            print("Black Jack!")

    hit_or_stay = input("Hit or stay?")
    if hit_or_stay == "hit":
        deck.deal_cards(player_hand, 1)
        show_cards()
        game_logic()
    if hit_or_stay == "stay":
        print("stay")

        game_logic()


game_logic()
