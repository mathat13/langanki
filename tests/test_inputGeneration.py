import unittest
from unittest.mock import mock_open, patch
import csv

def getWordList2Test(basicwordlist, advancedwordlist):

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
            print(f"Bad data on line {counter + 2} in advancedwordlist, please check there are exactly 2 fields for this word, skipping.")
            yield False

def getWordList2TestWithCSV(csv1, csv2):
    wordlist = {}

    with open(csv1) as file:
        basicwordlist = csv.DictReader(file)

        for word_dict in basicwordlist:
            if 1 <= len(word_dict) <= 2:
                word = word_dict['word']
                wordlist[word] = {
                    'gender': word_dict['gender'],
                    'id': 0,
                    'image_mediadb': [],
                    'sound_mediadb': ''
                }

            else:
                print(f"Data not formatted correctly for {word_dict[0]}, please check there are 1-2 fields for this word in basicwordlist.")
                return False
        

    with open(csv2) as file:
        advancedwordlist = csv.DictReader(file)
        
        for word_dict in advancedwordlist:
            if len(word_dict) == 2:            
                word = word_dict['word']
                wordlist[word] = {
                    'sentence': word_dict['sentence'],
                    'id': 1,
                    'image_mediadb': [],
                    'sound_mediadb': ''
                    }

            else:
                print(f"Data not formatted correctly for {word_dict[0]}, please check there are 2 fields for this word in advancedwordlist.")
                return False
            return wordlist
    
class TestgetWordList2(unittest.TestCase):

    def testDictToJSONExpectedValues(self):
        test_data1 = [
            {'word': 'gabbiano', 'gender': 'maschile'},
            {'word': 'condurre', 'gender': ''}
            ]
        test_data2 = [
            {'word': 'troppo', 'sentence': 'Sono troppo semplici.'},
            {'word': 'cambio', 'sentence': 'Al cambio afuore.'}
            ]
        expected_result1 = {'word': 'gabbiano', 'gender': 'maschile', 'id': 0, 'image_mediadb': [], 'sound_mediadb': ''}
        expected_result2 = {'word': 'condurre','gender': '', 'id': 0, 'image_mediadb': [], 'sound_mediadb': ''}
        expected_result3 = {'word': 'troppo','sentence': 'Sono troppo semplici.', 'id': 1, 'image_mediadb': [], 'sound_mediadb': ''}
        expected_result4 = {'word': 'cambio','sentence': 'Al cambio afuore.', 'id': 1, 'image_mediadb': [], 'sound_mediadb': ''}
        '''
        expected_final_result = {
            {'word': 'gabbiano', 'gender': 'maschile', 'id': 0, 'mediadb
': []},
            {'word': 'condurre','gender': '', 'id': 0, 'mediadb
': []},
            {'word': 'troppo','sentence': 'Sono troppo semplici.', 'id': 1, 'mediadb
': []},
            {'word': 'cambio','sentence': 'Al cambio afuore.', 'id': 1, 'mediadb
': []}
        }
        '''
        expected_result_list = [expected_result1, expected_result2, expected_result3, expected_result4]

        result = getWordList2Test(test_data1, test_data2)

        for expected_result in expected_result_list:
            self.assertEqual(next(result), expected_result)
       
    def testDictToJSONNoValues(self):
        test_data1 = [
            {'word': '', 'gender': ''},
            {'word': '', 'gender': ''}
            ]
        test_data2 = [
            {'word': '', 'sentence': ''},
            {'word': '', 'sentence': ''}
            ]
        expected_result1 = False
        expected_result2 = False
        expected_result3 = False
        expected_result4 = False
        # expected_final_result = {}

        expected_result_list = [expected_result1, expected_result2, expected_result3, expected_result4] # expected_final_result]

        result = getWordList2Test(test_data1, test_data2)

        for expected_result in expected_result_list:
            self.assertEqual(next(result), expected_result)

    '''
    @patch('builtins.open')
    def test_correctOutput(self, mock_open):
        mockfile1 = mock_open(read_data='word,gender\nword1,gender1\nword2,gender2').return_value
        mockfile2 = mock_open(read_data='word,sentence\nwordA,sentenceA\nwordB,sentenceB').return_value

        # Set the side effect for open to handle multiple files
        mock_open.side_effect = [mockfile1, mockfile2]

        # Call the function with dummy file paths
        a = getWordList2TestWithCSV('dummy_path1.csv', 'dummy_path2.csv')
        
        expected_result = {'gabbiano': {'gender': 'maschile', 'id': 0, 'mediadb': []}, 'condurre': {'gender': None, 'id': 0, 'mediadb': []}, 'troppo': {'sentence': 'Sono troppo semplici, troppo melodiche e troppo ottimiste.', 'id': 1, 'mediadb': []}}
        
        self.assertEqual(a, expected_result)
    '''

if __name__ == '__main__':
    unittest.main()
