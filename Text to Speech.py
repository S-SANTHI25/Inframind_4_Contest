!pip install gTTS #installation of gTTS google text to speech library

from gtts import gTTS  #import gTTS

import os
intext = "How are you?" #getting the text input

language = 'en' #language is given

the_object = gTTS(text=intext, lang=language, slow=False) #object is created

the_object.save("how.mp3") #saving the file
os.system("mpg321 how.mp3") #playing the file
