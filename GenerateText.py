import random

nouns = ("darkness", "light", "passion", "time", "power", "strength", "vengeance", "tragedy", "mercy", "doom", "space", "evil", "good", "sky", "space", "stars", "galaxy", "universe", "domain")
verbs = ("runs", "falls", "divides", "unleashes", "destroys", "manifests", "chooses", "rises", "grows", "breathes", "watches", "rages", "oozes", "laughs", "wrecks", "salvages", "climactic")
adv = ("mightily.", "dutifully.", "foolishly.", "with strength.", "with rage.", "with pride.", "absolutely.", "with an unsteady rhythm.", "curiously.", "with unblinking eyes.", "aimlessly.")
adj = ("Strong", "Weak", "Zealous", "Brave", "Fearsome", "Malevolent", "Tyrannical", "Furious", "Angry", "Wicked", "Judgemental", "Ancient", "Shimmering", "Vengeful", "Sleeping", "Chaotic", "Grim")

#Generate random text as adj + noun + verb + adverb
def getRandText():
    return '"' + adj[random.randrange(0,len(adj))] + ' ' + nouns[random.randrange(0,len(nouns))] + ' ' + verbs[random.randrange(0,len(verbs))] + ' ' + adv[random.randrange(0,len(adv))] + '"'
