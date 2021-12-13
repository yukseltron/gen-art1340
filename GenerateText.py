import random

nouns = ("darkness", "light", "passion", "time", "power", "strength", "vengeance", "tragedy", "mercy", "doom", "space", "evil")
verbs = ("runs", "falls", "divides", "unleashes", "destroys", "manifests", "chooses", "rises", "grows", "breathes", "watches", "rages", "oozes", "laughs")
adv = ("mightily.", "dutifully.", "foolishly.", "with strength.", "with rage.", "with pride.", "absolutely.", "with an unsteady rhythm.", "curiously.", "with unblinking eyes.", "aimlessly.")
adj = ("Strong", "Weak", "Zealous", "Brave", "Fearsome", "Malevolent", "Tyrannical", "Furious", "Angry", "Wicked", "Judgemental", "Ancient", "Shimmering", "Vengeful", "Sleeping", "Chaotic", "Grim")

def getRandText():
    return '"' + adj[random.randrange(0,5)] + ' ' + nouns[random.randrange(0,5)] + ' ' + verbs[random.randrange(0,5)] + ' ' + adv[random.randrange(0,5)] + '"'
