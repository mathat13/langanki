import genanki
from src.utilityFunctions import pathJoiner, loadConfig

class MyNote(genanki.Note):
        @property
        def guid(self):
            return genanki.guid_for(self.fields[1])

def createBasicModel():

    with open("resources/configs/basictemplate.yaml", "r") as f:
        template = f.read()

    with open(loadConfig("styling_path"), "r") as f:
        templatecss = f.read()

    myModel = genanki.Model(
    1380120063,
    'Simple Model',
    fields=[
        {'name': 'Immagine'},
        {'name': 'Parola'},
        {'name': 'Pronuncia'},
        {'name': 'Genere'},
        {'name': 'IPA'},
    ],

    templates=template,

    css=templatecss

    )

    return myModel

def createClozeModel():

    with open("resources/configs/clozetemplate.yaml", "r") as f:
        template = f.read()

    with open(loadConfig("styling_path"), "r") as f:
        templatecss = f.read()

    myModel = genanki.Model(
    1380120164,
    'Cloze Model',
    model_type=genanki.Model.CLOZE,
    fields=[
        {'name': 'Immagine'},
        {'name': 'Parola'},
        {'name': 'Pronuncia'},
        {'name': 'Frase'},
        {'name': 'IPA'},
    ],

    templates=template,

    css=templatecss

    )

    return myModel

# Define deck for notes to be added to.

def createDeck(deckID, deckName):
    myDeck = genanki.Deck(
      deckID,
      deckName)
    return myDeck

def addNote(model, deck, fields):
    # Creates a note that uses the myModel template for each fieldList generated by the fieldGenerator function.

    note = MyNote(
    model=model,

    fields=fields
    )
    deck.add_note(note)

    return deck

def createPackage(deck, mediaDB):
    # Create package for import to Anki.
    myPackage = genanki.Package(deck)
    # Generate MediaDB of images and sound files with createMediaDB.
    outputPackage = f"{deck.name}.apkg"
    myPackage.media_files = mediaDB
    myPackage.write_to_file(pathJoiner(loadConfig("package_path"), outputPackage))
    return True
