import unittest
from src.deckGeneration import createBasicModel
import genanki

def createBasicModelTest(template):

    # with open("resources/configs/basictemplate.yaml", "r") as f:
    #     template = f.read()

    #with open(loadConfig("styling_path"), "r") as f:
    #    templatecss = f.read()

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

    #css=templatecss

    )

    return myModel

class TestcreateModel(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.yamltest = ""
        with open("resources/configs/basictemplate.yaml", "r") as f:
            self.yamltest = f.read()
          
    
    def test_yamlRead(self):
        print(self.yamltest)
        yamlModel = createBasicModelTest(self.yamltest).templates
        testModel = createBasicModel().templates
        self.assertEqual(yamlModel, testModel)

if __name__ == '__main__':
    unittest.main()