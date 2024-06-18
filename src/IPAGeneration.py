import epitran

def getIPA(word):

    italian_epitran = epitran.Epitran('ita-Latn')

    italian_word = word  # Example Italian word
    ipa_representation = italian_epitran.transliterate(italian_word)
    ipa_final = f'/{ipa_representation}/'
    print(f'IPA Produced: {ipa_final}')
    return ipa_final

def validateIPA():
    pass