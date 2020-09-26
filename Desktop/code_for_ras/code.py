
#from pygame import mixer
#import pygame
#import pytesseract
from PIL import Image
import cv2
import pytesseract
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import pygame

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
key = cv2.waitKey(1) 
cap = cv2.VideoCapture(0) #open the camera 
while True:

	ret , frame = cap.read()  # 2 parameter ret for matrix and frame is frames of camera 
	cv2.imshow('Captured image',frame) #show the gui and camera op
	key = cv2.waitKey(1)
	if key==ord('s'): #press s for click the photo
		cv2.imwrite(filename='saved_img.jpg',img=frame) #create the saved_img.jpg and save in the same folder
		cap.release() # close the camera
		cv2.destroyAllWindows()
		break
		
#time.sleep(0.2)
#img = Image.open('Capture.jpg') #clicked photo open here for processing
img = cv2.imread('Capture.jpg')

img= cv2.medianBlur(img,1)
#cv2.imshow('show',img)
#cv2.imwrite(filename='saved_img_2.jpg',img=img)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
text_1 = pytesseract.image_to_string(gray) #here img to text conversion happen
print(text_1) #processed text print here

#text = str(text)
text_file = open(r'text.txt','w') #create text file here
text_file.writelines(text_1) #process text save in text file
text_file.close() #text file close

#time.sleep(0.2)

def speak(text):
	tts = gTTS(text=text,lang='en') #google text to speech
	filename = 'voice.mp3'
	tts.save(filename) # voice file created and save in same folder
	#playsound.playsound(filename) #not supported in raspibery  use pygame.mixer 
	
speak(text_1)



pygame.mixer.init()

pygame.mixer.music.load('voice.mp3')
#time.sleep(0)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy() == True: # imp line without this audio is not working
    continue








 
		




