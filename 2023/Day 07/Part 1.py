#this is innefficient as hell but its only 1000 cards who cares
def sortCards(card : list, cards : list):
    scale = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"] 
    score = 0
    for i, c in enumerate(card[0]):
        score += (scale.index(c)+2)*100**(4-i)
    card.append(score)
    cards.append(card)
    scores = []
    if len(cards) > 0:
        for card in cards:
            scores.append(card[2])
        scores.sort()
        newCards = []
        for score in scores:
            for card in cards:
                if card[2] == score:
                    newCards.append(card)
        return newCards
    else:
        return cards    

def scoreCards(card, scores):
    cardDict = {}
    for c in card[0]:
        if c in cardDict.keys():
            cardDict[c] += 1
        else:
            cardDict[c] = 1
    match len(cardDict):
        case 1:
            index = 6
        case 2:
            if 4 in cardDict.values():
                index = 5
            else:
                index = 4
        case 3:
            if 3 in cardDict.values():
                index = 3
            else:
                index = 2
        case 4:
            index = 1
        case _:
            index = 0
    scores[index] = sortCards(card, scores[index])
    return scores

scores = [[],[],[],[],[],[],[]]
f = open("2023\\Day 07\\input.txt", "r")
cards = [x.strip().split(" ") for x in f.readlines()]
for card in cards:
    scores = scoreCards(card, scores)

rank = 1
winnings = 0
for group in scores:
    for card in group:
        winnings += int(card[1]) * rank
        rank += 1
print(winnings)