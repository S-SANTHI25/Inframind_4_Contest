!sudo apt install tesseract-ocr 
!pip install pytesseract #installation of pytesseract

import pytesseract #importing required libraries
import cv2
import matplotlib.pyplot as plt

from google.colab.patches import cv2_imshow 
img=cv2.imread('3.jpeg') #reading image, change image name with extension
cv2_imshow(img) #to display image
cv2.waitKey(0)
cv2.destroyAllWindows()

text = pytesseract.image_to_string(img) #text is extracted from image
print(text)  #extracted text is printed

#the upcoming section is for sentimental analysis
from textblob import TextBlob #importing textblob library
 
def sentiment(polarity):
    if blob.sentiment.polarity < 0:
        print("Negative") #negative mood
    elif blob.sentiment.polarity > 0:
        print("Positive")  #positive mood
    else:
        print("Neutral") #neutral mood
 
 
blob = TextBlob(text) #text is taken as blob
print(blob.sentiment) #to print the sentiment
sentiment(blob.sentiment.polarity) #polarity value
