# File: hmai.py
# By: Senior Duckie.
# Date: Sep 9.
# Purpose: hangman AI, a bot build to solve hangman games. if it has 5 or more
#          letters, it'll probably get it no problem. 


dict = open('/usr/share/dict/words').read().split()
dict = [x.lower() for x in dict]
print(type(dict))

POSSIBLELETTER = 'abcdefghijklmnopqrstuvwxyz-'


class Hangman:
    word = []
    wordlen = 0
    probability = []
    listofposs = []

    lastguess = ""
    guesses = ""
    wrongs = 0

    def __init__(self, newword):
        self.word = newword
        self.wordlen = len(self.word)
        self.listofposs = list(filter(lambda x: len(x) == self.wordlen, dict))

    def nextData(self, word):
        self.word = word
        found = 0
        pos = 0
        for l in word:
            if self.lastguess in l:
                found = 1
                self.listofposs = list(filter(lambda x: self.lastguess == x[pos], self.listofposs))
            else:
                self.listofposs = list(filter(lambda x: self.lastguess != x[pos], self.listofposs))
            pos = pos + 1
        if found == 0:
            self.wrongs = self.wrongs + 1
            self.listofposs = list(filter(lambda x: self.lastguess not in x, self.listofposs))

    def calcProb(self):
        probdict = {}
        for l in POSSIBLELETTER:
            if l not in self.guesses:
                probdict[l] = 0
                for w in self.listofposs:
                    if l in w:
                        probdict[l] = probdict[l] + 1
        self.probability = list(reversed(sorted(probdict.items(), key=lambda x:x[1])))

    def getRecommended(self):
        pos = 0
        listlen = len(self.listofposs)
        bestguess = ""
        percentage = 2.0
        for i in self.probability:
            if abs(i[1] / listlen - 0.5) < percentage:
                percentage = abs(i[1] / listlen - 0.5)
                bestguess = i[0]

        selecting = ""
        if percentage < 0.075 and self.wrongs < 4 and self.probability[0][1] / listlen < 0.99:
            selecting = "MID"
            self.lastguess = bestguess
        else:
            selecting = "MAX"
            self.lastguess = self.probability[0][0]

        self.lastguess = self.probability[0][0]
        self.guesses = self.guesses + self.lastguess
        return self.lastguess

    def printData(self):
        print("current word:", self.word)
        print("length", self.wordlen)
        print("words", len(self.listofposs))
        print(self.listofposs[0])
        print("highest letter", self.probability[0][0])
        print(self.probability)

    def lightprint(self):
        listlen = len(self.listofposs)
        print("current word:", self.listofposs[0], "words left", listlen, "%%%.1f" % (100 * self.probability[0][1] * 1. / listlen) )
