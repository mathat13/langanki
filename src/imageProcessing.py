from PIL import Image
from src.utilityFunctions import findFile, pathJoiner, loadConfig, getFileName

def convertToJPG(image):

    rgbImage = image.convert("RGB")
    return rgbImage

def resizeImage(image):

    if image.width > 400 or image.height > 400:
        resizedImage = image.resize((400, 400))
        return resizedImage
    
    return image

def verifyRawImageFile(word):
    path = loadConfig("raw_image_path")
    file = findFile(word, path)
    if file:
        return file
    return False

def verifyImageFile(word):
    path = loadConfig("processed_image_path")
    file = findFile(word, path)
    if file:
        return file
    return False

def processImage(word_info):
    word = word_info['word']
    image_mediadb = word_info['image_mediadb']

    outputPath = loadConfig("processed_image_path")
    outputFile = verifyImageFile(word)
    inputFiles = verifyRawImageFile(word)
    
    if inputFiles:
        if not outputFile:
            # TODO turn this into a for loop to accommodate multiple images, os.path.basename can be used to add the file name to the path variable of word_info.
            for index, file in enumerate(inputFiles):
                fileName = getFileName(file)
                outFile = pathJoiner(outputPath, f"{fileName}.jpg")

                with Image.open(file) as image:
                    convertedImage = convertToJPG(image)
                    resizedImage = resizeImage(convertedImage)
                    resizedImage.save(outFile)
                    print("Image saved to:", outFile)

                    # Add file to word_info mediadb.
                    image_mediadb.append(outFile)
        else:
            print(f"Image file for {word} already present, skipping.")
            for file in outputFile:
                image_mediadb.append(file)
    else:
        print(f"Image file for {word} not found at correct location, skipping.")
    return True
   