import langanki

#TODO input that needs to be verified:
# Wordlist
# Fields
# Files in correct location
# MediaDB element
# MediaDB

# Get word list to read from
wordlist = langanki.generateWordList()
mediaDB = []
myModel = langanki.createBasicModel()
myClozeModel = langanki.createClozeModel()
modelDB = [myModel, myClozeModel]
myDeck = langanki.createDeck(2059400190, 'ItalianVocabTest')

# Deck IDs:
# 2059400190: ItalianVocabTest
# 

for word in wordlist:
    # Set the model for the current word
    model = langanki.getWordModel(word, modelDB)
    
    # Verify existence and process raw image for word.
    langanki.processImage(word)

    # Add pronunciation of word to correct location.
    langanki.addSound(word)

    # Create field to feed into note.
    field = langanki.createField(word)

    # Add note to the specified deck with the given fields using the structure specified in the current model.
    langanki.addNote(model, myDeck, field)

    # Add the resources to the mediaDB for creating the package.
    langanki.addWordToMediaDB(word, mediaDB)

# Create the package with the updated deck and mediaDB.

langanki.createPackage(myDeck, mediaDB)
