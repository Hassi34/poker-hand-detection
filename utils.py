
pokerhandRanks = {10: "Royal Flush", 9: "Straight Flush", 8: "Four of a kind", 7: "Full House", 6: "Flush", 5: "Straight" , 4: "Three of a kind", 3: "Two Pair", 2: "Pair", 1: "High Card"}

def findPokerHand(hand):

    ranks = []
    suits = []
    possibleRanks = []

    for card in hand:
        if len(card) == 2:
            rank = card[0]
            suit = card[1]
        else:
            rank = card[0:2]
            suit = card[2]

        if rank == "A" : rank = 14
        elif rank == "K" : rank = 13
        elif rank == "Q" : rank = 12
        elif rank == "J" : rank = 11 

        ranks.append(int(rank))
        suits.append(suit)
        sortedRanks = sorted(ranks)
    # Royal Flush, straight flush and flush
    if suits.count(suits[0]) == 5: # Check for flush
        if 14 in sortedRanks and 13 in sortedRanks and 12 in sortedRanks and 11 in sortedRanks and 10 in sortedRanks:
            possibleRanks.append(10) # Royal Flush

        # Straight flush
        elif all(sortedRanks[i] == sortedRanks[i-1] + 1 for i in  range(1, len(sortedRanks))):
            possibleRanks.append(9) # straight flush

        else:
            possibleRanks.append(6) # flush

    # Straight
    if all(sortedRanks[i] == sortedRanks[i-1] + 1 for i in  range(1, len(sortedRanks))):
        possibleRanks.append(5) # straight
    
    handUniqueVals = list(set(sortedRanks))
    # Four of a kind and full house
    if len(handUniqueVals) == 2:
        for val in handUniqueVals:
            if sortedRanks.count(val) == 4: # Four of a kind
                possibleRanks.append(8)
            if sortedRanks.count(val) == 2: # Full House
                possibleRanks.append(7)
    # Three of a kind and pair
    if len(handUniqueVals) == 3:
        for val in handUniqueVals:
            if sortedRanks.count(val) == 3: # Three of a kind
                possibleRanks.append(4)
            if sortedRanks.count(val) == 2: # Two pair
                possibleRanks.append(3)
    # Pair
    if len(handUniqueVals) == 4:
        possibleRanks.append(2)

    if not possibleRanks:
        possibleRanks.append(1)


    output = pokerhandRanks[max(possibleRanks)]
    print(hand, output)
    return  output

if __name__ == '__main__':
    findPokerHand(['AH', 'KH', 'QH', 'JH', '10H']) #Royal Flush
    findPokerHand(['QC', 'JC', '10C', '9C', '8C']) # Straight Flush 
    findPokerHand(['5C', '5S', '5H', '5D', 'QH']) # Four of a kind 
    findPokerHand(['2H', '2D', '2S', '10H', '10C']) # Full House
    findPokerHand(['2D', 'KD', '7D', '6D', '5D']) # Flush
    findPokerHand(['JC', '10H', '9C', '8C', '7D']) # Straight
    findPokerHand(['10H', '10C', '10D', '2D', '5S']) # Three of a kind
    findPokerHand(['KD', 'KH', '5C', '5S', '6D']) # Two Pair
    findPokerHand(['2D', '2S', '9C', 'KD', '10C']) # Pair
    findPokerHand(['KD', '5H', '2D', '10C', 'JH']) # Hight Card