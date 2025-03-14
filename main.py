import deck
import random

deck = deck.Deck()
player_hand = []
dealer_hand = []


player_hand.clear()
deck.make_deck()
deck.shuffle_deck()


deck.deal_cards(player_hand, 2)
deck.deal_cards(dealer_hand, 2)


def show_player_cards():
    for card in player_hand:
        print(f"Your card {card.get_card()}")

def show_dealer_cards():
    suites = ["♠","♥","♦","♣"]
    for card in dealer_hand:


        print(f"Dealers card {card.get_card()} dealers face down card |{suites[random.randint(0,3)]}|")
        break
def line_breaker():
    print("_________________________________________________________________________________")

print("_____________________𝖕𝖑𝖆𝖞𝖊𝖗_𝖍𝖆𝖓𝖉__________________________________________________")
show_player_cards()
print("_____________________𝖉𝖊𝖆𝖑𝖊𝖗_𝖍𝖆𝖓𝖉__________________________________________________")
show_dealer_cards()
line_breaker()

def game_logic():
    dealer_hand_sum = 0
    player_hand_sum = 0
    playing = True
    while playing:


        hit_or_stay = input("|Hit or stay?| ")
        line_breaker()

        if hit_or_stay == "hit":

            deck.deal_cards(player_hand, 1)
            show_player_cards()
            for card in player_hand:
                player_hand_sum += card.vaule
                if player_hand_sum > 21:
                    print(f"You busted {player_hand_sum} Game Over")
                    line_breaker()
                    playing = False
                if player_hand_sum == 21:
                    print("|Black Jack!|")
                    line_breaker()
                    playing = False

            hit_or_stay = input("|Hit or stay?| ")


        if hit_or_stay == "stay":
            for card in dealer_hand:
                dealer_hand_sum += card.vaule
                if dealer_hand_sum <= 16:
                    deck.deal_cards(dealer_hand, 1)
                    print("|Dealer has chose to hit|")
                    line_breaker()
                    break
                if dealer_hand_sum >= 17:
                    print("|Dealer has choose to stand|")
                    line_breaker()
                    break
            check_victory(dealer_hand_sum, player_hand_sum)



def check_victory(dealer_hand_sum, player_hand_sum):
    if dealer_hand_sum > player_hand_sum:
        print("|Dealer has won!|")
        line_breaker()
        for card in dealer_hand:
            print(f"|Dealers cards {card.get_card()}|")
        line_breaker()
        quit()
    if player_hand_sum > dealer_hand_sum:
        print("|Player has won!|")
        line_breaker()
        print("Dealers cards")
        line_breaker()
        for card in dealer_hand:
            print(f"|Dealers cards {card.get_card()}|")
        line_breaker()
        print("Players cards")
        show_player_cards()
        line_breaker()
        quit()
    if dealer_hand_sum > 21:
        print("|Dealer has busted|")
        line_breaker()
        for card in dealer_hand:
            print(f"|Dealers cards {card.get_card()}|")
        line_breaker()
        quit()








game_logic()
