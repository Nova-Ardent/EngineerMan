# Name:      hangman.py
# Date:      Aug 27th
# Author:    Sr Duckie
# Version:   1.0.0
# Purpose:   to set up all of the required functionalities for a hangman game
#            for discord.

import random as rand
import os
import json
import numpy as np

words = open('/usr/share/dict/words').read().split()
hangmanval = {}
playerdata = {}

ERRORNOGAME = -1        # no active game.
ERRORGAMECOMP = -2      # current game complete.
ERRORINVALID = -3       # invalid character
ERRORDUP = -4           # duplicate letter. (already played)
LOSTGAME = -5           # game lost
WONGAME = 1             # game won.
NOERROR = 0             # no 'error'


# hangman
# args:    serverid, chat/channel
# purpose: sets up a new hangman game
# notes:   hangman games are channel depended. If you want them user dependent
#          give it the value of a unique user ID.
def hangman(sid, channel):
    if not sid in playerdata:
        playerdata[sid] = {}
        savedata(playerdata, sid)
    global hangmanval
    gameid = "%s%s" % (sid, channel)

    hangmanval[gameid] = {}
    hangmanval[gameid]["word"] = rand.choice(words).lower()
    hangmanval[gameid]["guess"] = ("\_ " * len(hangmanval[gameid]["word"])).split(" ")
    hangmanval[gameid]["guessesw"] = ""
    hangmanval[gameid]["guessesr"] = ""
    hangmanval[gameid]["tries"] = 6
    hangmanval[gameid]["potpoints"] = len(hangmanval[gameid]["word"]) * 2 + 6
    print(hangmanval[gameid]["word"])

    return hangmanval[gameid]["guess"]

def getGuess(sid, channel):
    gameid = "%s%s" % (sid, channel)
    return hangmanval[gameid]["guess"]

def getWord(sid, channel):
    gameid = "%s%s" % (sid, channel)
    return hangmanval[gameid]["word"]

def getRightLetters(sid, channel):
    gameid = "%s%s" % (sid, channel)
    return hangmanval[gameid]["guessesr"]

def getWrongLetters(sid, channel):
    gameid = "%s%s" % (sid, channel)
    return hangmanval[gameid]["guessesw"]

def getTries(sid, channel):
    gameid = "%s%s" % (sid, channel)
    return hangmanval[gameid]["tries"]

def getPotPoints(sid, channel):
    gameid = "%s%s" % (sid, channel)
    return hangmanval[gameid]["potpoints"]

def getUserScore(sid, user):
    return playerdata[sid][user]

# play
# args:     serverid, channelID, letter given, user, userid (discriminator)
# purpose:  to play a letter in the current game from the server+channel.
def play(sid, channel, letter, user, id):
    global hangmanval
    gameid = "%s%s" % (sid, channel)
    uid = "%s#%s" % (user, id)
    if not uid in playerdata[sid]:
        playerdata[sid][uid] = 0

    if not gameid in hangmanval:
        return ERRORNOGAME
    if not "\\_" in hangmanval[gameid]["guess"]:
        return ERRORGAMECOMP
    if not letter.isalpha() and letter != "-":
        return ERRORINVALID
    if letter in hangmanval[gameid]["guessesw"] or letter in hangmanval[gameid]["guessesr"]:
        return ERRORDUP
    if hangmanval[gameid]["tries"] == 0:
        return LOSTGAME
    elif letter in hangmanval[gameid]["word"]:
        index = 0
        found = 0
        for i in hangmanval[gameid]["word"]:
            if i == letter:
                hangmanval[gameid]["guess"][index] = i
                playerdata[sid][uid] = playerdata[sid][uid] + 2
                found = 1
            index = index + 1
        if found == 1:
            hangmanval[gameid]["guessesr"] = hangmanval[gameid]["guessesr"] + " " + letter
        if not "\\_" in hangmanval[gameid]["guess"]:
            playerdata[sid][uid] = playerdata[sid][uid] + 6
            savedata(playerdata, sid)
            return WONGAME
    else:
        hangmanval[gameid]["guessesw"] = hangmanval[gameid]["guessesw"] + " " + letter
        hangmanval[gameid]["tries"] = hangmanval[gameid]["tries"] - 1
        playerdata[sid][uid] = playerdata[sid][uid] - 2
        if hangmanval[gameid]["tries"] == 0:
            playerdata[sid][uid] = playerdata[sid][uid] - 6
            return LOSTGAME
    return NOERROR

# savedata
# args:     the json var to save, and the serverid.
# purpose:  to save a json variable related to the highscores of a server.
def savedata(jsonvar, sid):
    if not os.path.exists("./hangman/data/" + sid):
        os.makedirs("./hangman/data/" + sid);
    with open("./hangman/data/" + sid + "/scores.json", "w") as f:
        json.dump(jsonvar[sid], f)

# loaddata
# args:    --
# purpose: loads and sets the latest save data
def loaddata():
    if not os.path.exists("./hangman/data/"):
        return
    for folders in os.listdir("./hangman/data/"):
        with open("./hangman/data/" + folders + "/scores.json", "r") as f:
            playerdata[folders] = json.load(f)
    print(playerdata)

# topten
# args:    server id.
# purpose: gets the top ten scores of that server.
def topten(sid):
    if not sid in playerdata:
        playerdata[sid] = {}
    tten = sorted(playerdata[sid].items(), key=lambda x:x[1])
    size = len(tten)
    return tten[-10:]
