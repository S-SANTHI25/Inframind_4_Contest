!pip install googletrans #installation of googletrans

import googletrans #importing googletrans
print(googletrans.LANGUAGES) #languages available in googletrans

from googletrans import Translator

translator = Translator() #translator object is created
result = translator.translate('How are you?', src='en', dest='ta') #translation is stored in result

print(result.src) #source language is printed
print(result.dest) #destination language is printed
print(result.text) #result text is printed
