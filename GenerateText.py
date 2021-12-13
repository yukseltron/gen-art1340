import random

nouns = ("darkness", "light", "passion", "time", "power", "strength", "vengeance", "tragedy", "mercy", "doom")
verbs = ("runs", "falls", "divides", "unleashes", "destroys", "manifests", "chooses", "rises", "grows")
adv = ("mightily.", "dutifully.", "foolishly.", "with strength.", "with rage.", "with pride.", "absolutely")
adj = ("Strong", "Weak", "Zealous", "Brave", "Fearsome", "Malevolent", "Tyrannical", "Furious")

def getRandText():
    return '"' + adj[random.randrange(0,5)] + ' ' + nouns[random.randrange(0,5)] + ' ' + verbs[random.randrange(0,5)] + ' ' + adv[random.randrange(0,5)] + '"'
