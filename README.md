# Blackjack Game
## Description
This is a simple text-based implementation of a Blackjack game where you play against a dealer. The goal is to get a hand value closer to 21 than the dealer without exceeding it. The deck of cards is shuffled, and the game allows the player to choose to "hit" (draw a card) or "stay" (end the turn). The dealer also follows specific rules for their actions.

## Features
Deck: A deck of cards is created, shuffled, and dealt to both the player and the dealer.
Player and Dealer Hands: The player can see their own hand, while the dealer's hand is partially hidden until the game concludes.
Game Logic: The game handles player choices (hit or stay) and dealer actions according to standard Blackjack rules.
Victory Check: After each round of actions, the game will check for a winner based on the hand values.
## Dependencies
This script assumes you have a deck module, which contains the following classes and methods:

Deck(): A class representing the deck of cards.
make_deck(): Method to create a new deck of cards.
shuffle_deck(): Method to shuffle the deck.
deal_cards(hand, num): Method to deal cards to a specified hand.
get_card(): Method to return a string representation of a card.
vaule: The numeric value of the card.
## How to Run
Ensure you have the necessary deck module in your project directory with the required methods.
Run the script using Python 3.x:
```
python blackjack_game.py
```

The player is prompted to either "hit" or "stay" during the game.
Game Flow
The game starts by dealing two cards to both the player and the dealer.
The player can choose to either:
Hit: Draw an additional card.
Stay: End their turn.
The dealer automatically follows certain rules:
If the dealer's hand value is 16 or less, they must hit.
If the dealer's hand value is 17 or more, they must stay.
The game will check who has won based on the final hand values:
The player wins if their hand value is closer to 21 than the dealer's, without busting.
The dealer wins if their hand value is closer to 21 or the player busts (goes over 21).
A tie occurs if both hands are equal, or the dealer busts.
## Example Output
```
_____________________𝖕𝖑𝖆𝖞𝖊𝖗_𝖍𝖆𝖓𝖉__________________________________________________
Your card ♠ 7
Your card ♣ 9
_____________________𝖉𝖊𝖆𝖑𝖊𝖗_𝖍𝖆𝖓𝖉__________________________________________________
Dealers card ♦ 5 dealers face down card |♠|
_________________________________________________________________________________
|Hit or stay?| hit
_________________________________________________________________________________
Your card ♠ 3
Your card ♣ 9
Your card ♠ 7
Your card ♣ 9
|Black Jack!|
_________________________________________________________________________________
```
## How the Game Works:
### Player’s Turn:

The player starts with two cards.
The player can choose to "hit" (draw a card) or "stay" (end their turn).
If the player exceeds 21 points, they lose automatically.
If the player hits and gets exactly 21 points, they win with a Blackjack.
### Dealer’s Turn:

The dealer reveals one card and plays automatically.
The dealer must draw if their hand value is less than or equal to 16 and must stand if their hand is 17 or higher.
End of Game:

The game checks who has the higher hand value. If the player has a higher value without exceeding 21, the player wins. If the dealer has the higher value, the dealer wins. If either busts, the other wins automatically.
## License
Feel free to modify and distribute this code under the MIT License.
