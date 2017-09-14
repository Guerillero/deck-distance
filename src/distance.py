import os
import csv
import basics as mtgBasics
import matplotlib.pyplot as plt
from sklearn import manifold
import numpy as np
from bs4 import BeautifulSoup
import urllib


dataDir = 'C://Users//tfish//PycharmProjects//DeckDistance//data//'
outputDir = 'C://Users//tfish//PycharmProjects//DeckDistance//'

dataLst = os.listdir(dataDir)

decks = []
names = []

for fi in dataLst:
    fin = open(dataDir + fi, 'r')
    fi.split('.')
    a = mtgBasics.Deck(fi.split('.')[0])
    names.append(fi.split('.')[0])
    for line in fin:
        if line <> "\n":
            a.addcard(mtgBasics.Card(line.split(' ', 1)[1].strip('/n'), line.split(' ', 1)[0]))

    decks.append(a)

ma = mtgBasics.Matrix()

for deck1 in decks:
    line = []
    for deck2 in decks:  # you now have both decks open
        cardsSame = 0
        cards1 = deck1.getdeck()
        cards2 = deck2.getdeck()
        for card1 in cards1:
            for card2 in cards2:  # you now have both cards from both decks open
                if card1.getname() == card2.getname():
                    if card1.getcount() > card2.getcount():
                        cardsSame += card2.getcount()
                        break
                    elif card1.getcount() < card2.getcount():
                        cardsSame += card1.getcount()
                        break
                    else:
                        cardsSame += card1.getcount()
                        break
        line.append(int((1 - float(cardsSame) / float(deck1.getcount()))*100))
    ma.addrow(line)

fout = csv.writer(open(outputDir + "output.csv", 'wb'), dialect='excel')
names.insert(0, "")
fout.writerow(names)
q = 1
for row in ma.getmatrix():
    row.insert(0, names[q])
    fout.writerow(row)
    q += 1


mds = manifold.MDS(n_components=2, metric=True, random_state=6)

results = mds.fit(np.array(ma.getmatrix()))
coords = results.embedding_

names_t = []

for item in names:
    if item <> "":
        r = urllib.urlopen("https://www.mtggoldfish.com/deck/" + item + "#paper")
        s = BeautifulSoup(r.read(), "html.parser")
        g = s.find("title")
        if g is not None:
            f = str(g).split(">")[1]
            names_t.append(f.split("  ")[0])



plt.subplots_adjust(bottom = 0.1)
plt.scatter(coords[:,0], coords[:,1], marker='.')
for label, x, y in zip(names_t, coords[:, 0], coords[:, 1]):
    plt.annotate(
        label,
        xy = (x, y), xytext = (-5, 5),
        textcoords = 'offset points', ha = 'right', va = 'bottom')
plt.show()