class Deck:
    def __init__(self, idnumber):
        self.idNo = idnumber
        self.deckList = []
        self.cardCount = 0

    def getdeck(self):
        return self.deckList

    def getid(self):
        return self.idNo

    def addcard(self, card):
        self.cardCount += card.getcount()
        self.deckList.append(card)

    def getcount(self):
        return self.cardCount


class Card:
    def __init__(self, name, count):
        self.cardName = name

        if isinstance(count, int):
            self.cardCount = count
        else:
            self.cardCount = int(count)

    def updatecount(self, count):
        if isinstance(count, int):
            self.cardCount = count
        else:
            self.cardCount = int(count)

    def getcardaslist(self):
        return [self.cardCount, self.cardName]

    def getcardaslib(self):
        return {'count': self.cardCount, 'name': self.cardName}

    def getname(self):
        return self.cardName

    def getcount(self):
        return self.cardCount


class Matrix:
    def __init__(self):
        self.marray = []

    def addrow(self, row):
        self.marray.append(row)

    def getmatrix(self):
        return self.marray
