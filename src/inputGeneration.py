from src.IPAGeneration import getIPA
from src.utilityFunctions import loadConfig, pathJoiner, getFileBaseName
import csv
import re
import copy

def getWordListSimple():

    wordlist = []

    with open(pathJoiner(loadConfig("wordlist_path"), "wordlist.txt"), encoding="utf-8-sig") as a:
        for line in a.readlines():
            wordlist.append(line.strip())

    return wordlist

def generateWordList():

    with open(pathJoiner(loadConfig("wordlist_path"), "wordlistbasic.csv"), encoding="utf-8-sig") as file:
        basicwordlist = csv.DictReader(file, restval='')
        # word_list_total = {}

        for counter, word_dict in enumerate(basicwordlist):
            if 1 <= len(word_dict) <= 2 and word_dict['word']:
                word = word_dict['word']
                gender =  word_dict['gender']
                wordlist = {
                    'word': word,
                    'gender': gender,
                    'id': 0,
                    'image_mediadb': [],
                    'sound_mediadb': ''
                }
                yield wordlist

            else:
                print(f"Bad data on line {counter + 2}  in basicwordlist, please check there are 1-2 fields for this word, skipping.")
                yield False

    with open(pathJoiner(loadConfig("wordlist_path"), "wordlistadvanced.csv"), encoding="utf-8-sig") as file:
        advancedwordlist = csv.DictReader(file, restval='')
        
        for counter, word_dict in enumerate(advancedwordlist):
            if len(word_dict) == 2 and word_dict['word']:
                word = word_dict['word']
                sentence = word_dict['sentence']
                wordlist = {
                    'word': word,
                    'sentence': sentence,
                    'id': 1,
                    'image_mediadb': [],
                    'sound_mediadb': ''
                }
                yield wordlist

            else:
                print(f"Bad data on line {counter + 2}  in advancedwordlist, please check there are exactly 2 fields for this word, skipping.")
                yield False

def getWordModel(word_info, modelDB):
    modelID = word_info['id']
    if modelID == 0:
        return modelDB[0]
    elif modelID == 1:
        return modelDB[1]

# Field  Element Template: ['<img src="ciao.jpg">', 'ciao', '[sound:ciao.mp3]', 'SentencePlaceholder', 'IPAPlaceholder']

def createField(word_info):
    word = word_info['word']
    image_paths = word_info['image_mediadb']

    # TODO Split paths into pronunciation and image paths and create functions to read from each.
    # TODO Work out how to add gender gracefully to basic cards.
    # TODO Turn into switch statement.
    if word_info['id'] == 0:
        field = [getImageHTML(image_paths), word, f'[sound:{word}.mp3]', f'Genere: {getGenderField(word_info)}', getIPA(word)]
    
    elif word_info['id'] == 1:
        field = [getImageHTML(image_paths), word, f'[sound:{word}.mp3]', getClozeSentence(word_info['sentence'], word), getIPA(word)]
    return field

def getImageHTML(image_db):
    image_fields = []

    for path in image_db:
        fileName = getFileBaseName(path)
        image_fields.append(f'<img src="{fileName}">')
    return ''.join(image_fields)

def getGenderField(word_info):
    try:
        if word_info['gender']:
            return word_info['gender']
        return 'n/a'
    except KeyError:
        return 'n/a'

def getClozeSentence(sentence, word):
    return re.sub(rf'\b{word}\b', f'{{{{c1::{word}}}}}', sentence)

def addWordToMediaDB(word_info, mediaDB):
    # image_paths points to a mutable list and so has to be deepcopied to avoid modifying the original list value.
    image_paths = copy.deepcopy(word_info['image_mediadb'])
    sound_paths = word_info['sound_mediadb']
    image_paths.append(sound_paths)
    mediaDB.extend(image_paths)
    
    return True

def verifyField():
    pass

def verifyMediaDB():
    pass

def verifyWordList():
    pass
