import os, fnmatch
import json

with open("config.json") as json_conf: 
    CONF = json.load(json_conf)

def findFile(word, path):

    result = []
    pattern = f'{word}.*'
    number_pattern = f'{word}[0-9].*'

    for root, _, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern) or fnmatch.fnmatch(name, number_pattern):
                result.append(pathJoiner(root, name))
    return result

def pathJoiner(root, file):
     return os.path.join(os.path.normpath(root), os.path.normpath(file))

def loadConfig(path):
    return os.path.normpath(CONF[path])

def getFileBaseName(path):
    return os.path.basename(path)

def getFileName(path):
    return os.path.splitext(os.path.basename(path))[0]
