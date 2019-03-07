import random as r
#Markov chain program by JukSnider
r.seed()
#
inputfile = open("input.txt","r")
text = inputfile.read()
dumlist = text.split()
fulltextlist = []
unique = []
for x in dumlist:
    fulltextlist.append(x)
    if x not in unique:
        unique.append(x)
numwords = len(unique)
markov = []
dumlisttwo = fulltextlist
for x in unique:
    markov.insert(0, [])
#Test
for x in fulltextlist:
    ind = unique.index(x)
    if fulltextlist.index(x)+1 < len(fulltextlist):
        markov[ind].insert(1, fulltextlist[fulltextlist.index(x)+1])
    fulltextlist[fulltextlist.index(x)] = "okaythisisepic"
words = input("How many words do you want to have? >>>")
words = int(words)-1
startingwordone = markov[r.randint(0,len(markov))-1]
startingwordtwo = startingwordone[r.randint(0,len(startingwordone))-1]
while startingwordtwo == "." or startingwordtwo == "?" or startingwordtwo == "," or startingwordtwo == ":":
    startingwordone = markov[r.randint(0,len(markov))]
    startingwordtwo = startingwordone[r.randint(0,len(startingwordone))-1]
print(startingwordtwo, end = " ")
prevword = startingwordtwo
for x in range(words):
    nextwordsetup = markov[unique.index(prevword)]
    rando = r.randint(0,len(nextwordsetup)-1)
    nextword = nextwordsetup[rando]
    print(nextword, end = " ")
    prevword = nextword
print("")
print("COMPLETE")
