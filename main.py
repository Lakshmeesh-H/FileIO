# my_file = open('test.txt')
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# print(my_file.readline())
# print(my_file.readlines())
# my_file.close()

# with open('test.txt', mode='a') as my_file:
#     text = my_file.write('Hi Its Me again!')

# Python Text Translator 

from translate import Translator
translator = Translator(to_lang='ja')
try: 
    with open('intro.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
        with open('introtranslate.txt', mode='w') as my_file2:
            my_file2.write(translation)

except FileNotFoundError as err:
    print('Check the file path')

