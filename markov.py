#Importing random library
import random as r
#Markov chain program by Jack Snyder (JukSnider)
r.seed()
#Opens text file, creates list of all words split at spaces
inputfile = open("input.txt","r")
text = inputfile.read()
#List of all text
fulltextlist = text.split()
#List of unique words
unique = []
#Fulltextlist and unique ar intiallized
for x in fulltextlist:
    if x not in unique:
        unique.append(x)
#Markov[] is a list of lists that forms an array of probability for words
#Each list in markov directly coresponds to the word of the same index in unique[]. Each word in that list is a word that came after the corresponding word in unique
markov = []
for x in unique:
    markov.insert(0, [])
#Initalizing Markov and making fulltextlist into
for x in fulltextlist:
    ind = unique.index(x)
    if fulltextlist.index(x)+1 < len(fulltextlist):
        markov[ind].insert(1, fulltextlist[fulltextlist.index(x)+1])
    fulltextlist[fulltextlist.index(x)] = "okaythisisepic"
#Prompt for how many words to be generated
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
