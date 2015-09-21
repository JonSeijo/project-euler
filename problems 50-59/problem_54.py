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

    # ROYAL FLUSH
    w1 = hasRoyalFlush(player1Hand)
    w2 = hasRoyalFlush(player2Hand)

    if w1 and not w2: return 1
    if w2 and not w1: return 0


    # STRAIGH FLUSH
    w1 = hasStraighFlush(player1Hand)
    w2 = hasStraighFlush(player2Hand)

    if w1 and not w2: return 1
    if w2 and not w1: return 0
    if w1 and w2:
        if sum(player1Hand[::2]) > sum(player2Hand[::2]): return 1
        else: return 0

    # FOUR OF A KIND
    w1, n1_4 = hasFourOfAKind(player1Hand)
    w2, n2_4 = hasFourOfAKind(player2Hand)
    if w1 and not w2: return 1
    if w2 and not w1: return 0
    if w1 and w2:
        if isGreater(n1_4, n2_4): return 1
        else: return 0

    # FULL HOUSE
    w1, n1_3, n1_2 = hasFullHouse(player1Hand)
    w2, n2_3, n2_2 = hasFullHouse(player2Hand)
    if w1 and not w2: return 1
    if w2 and not w1: return 0
    if w1 and w2:
        if isGreater(n1_3, n2_3): return 1
        if isGreater(n2_3, n1_3): return 0
        else: # are equal
            if isGreater(n1_2, n2_2): return 1
            if isGreater(n2_2, n1_2): return 0


    # FLUSH
    w1, h1 = hasFlush(player1Hand)
    w2, h2 = hasFlush(player2Hand)
    if w1 and not w2: return 1
    if w2 and not w1: return 0
    if w1 and w2:
        for i in range(0, 4):
            if isGreater(h1[i], h2[i]): return 1
            if isGreater(h2[i], h1[i]): return 0


    # STRAIGHT
    w1, h1 = hasStraight(player1Hand)
    w1, h2 = hasStraight(player2Hand)
    if w1 and not w2: return 1
    if w2 and not w1: return 0
    if w1 and w2:
        for i in range(0, 4):
            if isGreater(h1[i], h2[i]): return 1
            if isGreater(h2[i], h1[i]): return 0


    # THREE OF A KIND
    w1, n1 = hasThreeOfAKind(player1Hand)
    w2, n2 = hasThreeOfAKind(player2Hand)
    if w1 and not w2: return 1
    if w2 and not w1: return 0
    if w1 and w2:
        if isGreater(n1, n2): return 1
        else: return 0



    # SI AMBOS GANAN, VER QUIEN TIENE SIGUIENTE MAS GRANDE
    # SI NADIE GANA, VER SIGUIENTE JUEGO POSIBLE (straight flush)

    return 0

def hasThreeOfAKind(hand):
    return hasNequals(hand, 3)


def hasStraight(hand):
    # Straight: All cards are consecutive values.
    counter = 0
    for card in CARDS:
        if card in hand:
            counter += 1
            if counter == 5:
                return True, sorted(hand[::2])[::-1]
        else:
            counter = 0

    return False, [0,0,0,0,0]


def hasFlush(hand):
    # Flush: All cards of the same suit.
    for suit in SUITS:
        counter = 0
        for s in hand[1::2]:
            if suit == s:
                counter += 1
                if counter == 5:
                    # It does not have royals, or it would be royal flush
                    return True, cardSort(hand[::2])[::-1]

    return False, [0,0,0,0,0]


def cardSort(unsortedCards):
    """ Need to implement because of J, K, A etc"""

    cards = [unsortedCards[0], unsortedCards[1], unsortedCards[2],
        unsortedCards[3], unsortedCards[4]]

    # USING SELECTION SORT
    iMin = 0
    for j in range(0, len(cards)-1):
        iMin = j

        for i in range(j+1, len(cards)):

            if isGreater(cards[iMin], cards[i]):
                iMin = i

        if iMin != j:
            swapper = cards[iMin]
            cards[iMin] = cards[j]
            cards[j] = swapper

    return cards


def hasFullHouse(hand):
    # Full House: Three of a kind and a pair.
    w3, n3 = hasNequals(hand, 3)
    w2, n2 = hasNequals(hand, 2)

    if w3 and w2:
        return True, n3, n2
    else:
        return False, 0, 0


def isGreater(n1, n2):
    i1 = 0
    i2 = 0
    for i in range(0, len(CARDS)):
        if n1 == CARDS[i]:
            i1 = i
        if n2 == CARDS[i]:
            i2 = i

    return (i1 > i2)


def hasFourOfAKind(hand):
    return hasNequals(hand, 4)


def hasNequals(hand, n):
    for value in CARDS:
        counter = 0
        for numberHand in hand[::2]:
            if value == numberHand:
                counter += 1
                if counter == n:
                    return True, value

    return False, 0


def hasStraighFlush(hand):
    # Straight Flush: All cards are consecutive values of same suit.
    count = 0
    for suit in SUITS:
        for number in CARDS:
            if(number+suit) in hand:
                count += 1
                if count == 5:
                    return True
            else:
                count = 0

    return False


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

   # hands = ["4C 4C 4C 4C AC 3C 3C 3C 3C AC"]

    for hand in hands:
        playerOneWins += findWinner(hand)

    print playerOneWins

    print hasThreeOfAKind("TCTHTC4CAC")


if __name__ == "__main__":
    main()
