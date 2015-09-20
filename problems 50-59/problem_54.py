# Problem 54
# Poker hands
"""
...
See https://projecteuler.net/problem=54 for details
...
...
The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space):
the first five are Player 1's cards and the last five are Player 2's cards.
You can assume that all hands are valid (no invalid characters or
repeated cards),
each player's hand is in no specific order,
and in each hand there is a clear winner.

How many hands does Player 1 win?
"""

def findWinner(hand):
    hand = hand.replace(" ", "")
    player1Hand = hand[:10]
    player2Hand = hand[10:]

    isWinner = False

    print player1Hand + " " + player2Hand

    w1 = hasRoyalFlush(player1Hand)
    w2 = hasRoyalFlush(player2Hand)

    if w1 and not w2:
        return 1
    if w2 and not w1:
        return 0

    # SI AMBOS GANAN, VER QUIEN TIENE SIGUIENTE MAS GRANDE
    # SI NADIE GANA, VER SIGUIENTE JUEGO POSIBLE (straight flush)

    return 0

def hasRoyalFlush(hand):
    # Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

    for suit in SUITS:
        hasHand = True
        for royal in CARDS[8:]:
            if (royal+suit) not in hand:
                hasHand = False

    return hasHand

# Hearth, Diamond, Club, Spade
SUITS = ['H', 'D', 'C', 'S']

CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


def main():
    playerOneWins = 0

    with open("problem_54_poker.txt") as f:
        hands = f.read().splitlines()

    for hand in hands:
        playerOneWins += findWinner(hand)

    print playerOneWins

if __name__ == "__main__":
    main()
