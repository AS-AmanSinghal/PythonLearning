from translate import Translator

translator = Translator(to_lang='ja')
try:
    with open('translatorFile.txt',mode='r') as myFile:
        while True:
            text = myFile.readline()
            print(translator.translate(text))
            if len(text) == 0:
                break
        # print(trans)



except(FileNotFoundError,IOError):
    print('Something Wents Wrong')
