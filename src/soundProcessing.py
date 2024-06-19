import requests
from src.utilityFunctions import findFile, pathJoiner, loadConfig

# Constants
API_BASE_URL = 'https://api.soundoftext.com'

def createSound(text, voice):
    endpoint = f'{API_BASE_URL}/sounds'
    headers = {'Content-Type': 'application/json'}
    payload = {
        'engine': 'Google',
        'data': {
            'text': text,
            'voice': voice
        }
    }

    response = requests.post(endpoint, json=payload, headers=headers)
    return response.json()

def getSoundUrl(soundId):
    endpoint = f'{API_BASE_URL}/sounds/{soundId}'
    response = requests.get(endpoint)
    soundInfo = response.json()
    
    if soundInfo['status'] == 'Done':
        return soundInfo['location']
    else:
        return None
    
def downloadSound(word, soundUrl):

    request = requests.get(soundUrl)
    outputPath = loadConfig("sound_path")
    file = pathJoiner(outputPath, f"{word}.mp3")

    with open(file, 'wb') as soundFile:
        soundFile.write(request.content)
    return file

def verifySoundFile(word):
    path = loadConfig("sound_path")
    file = findFile(word, path)
    if file:
        return file
    return False
    

def addSound(word_info):
    word = word_info['word']

# Example word
    italianWord = word
    italianVoice = "it-IT"
    soundFileExists = verifySoundFile(word)

    if not soundFileExists:
        # Create sound
        soundResponse = createSound(italianWord, italianVoice)
        if soundResponse['success']:
            soundId = soundResponse['id']
            # Retrieve sound URL
            soundUrl = getSoundUrl(soundId)
            if soundUrl:
                soundLocation = downloadSound(word, soundUrl)
                print("Sound downloaded to:", soundLocation)

                # Add file to word_info for mediaDB
                word_info['sound_mediadb'] = soundLocation
                
            else:
                print("Failed to retrieve sound URL.")

        else:
            print("Failed to create sound:", soundResponse['message'])

    else:
        soundLocation = soundFileExists[0]
        print(f"Sound already present for {word}, skipping.")
        word_info['sound_mediadb'] = soundLocation
    
    return True
