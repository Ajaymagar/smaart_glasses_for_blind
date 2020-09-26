import cv2
#from PIL import Image
#import playsound

from pygame import mixer
from gtts import gTTS
import time
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier('haarcade_eye.xml')

cv2.waitKey(1)

cap = cv2.VideoCapture(1)
while True:

	ret ,frame = cap.read()
	cv2.imshow('captured_image',frame)
	key = cv2.waitKey(1)
	if key==ord('s'): #press s for click the photo
		cv2.imwrite(filename='saved_img_1.jpg',img=frame) #create the saved_img.jpg and save in the same folder
		cap.release() # close the camera
		cv2.destroyAllWindows()
		break

#img = Image.open('saved_img_1.jpg') #clicked photo open here for processing
img_1 = cv2.imread('saved_img_1.jpg')
gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,1.3,5)
print('Faces found',len(faces))

#loop over the the cordinates
#for (x,y,w,z) in faces:
	#cv2.rectangle(img_1,(x,y),(x+w,y+z),(0,255,0),2)
	


#cv2.imshow('image',img_1)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#break



ajay='There are {} people'.format(len(faces))
text_file = open(r'text1.txt','w') #create text file here
text_file.writelines(ajay) #process text save in text file
text_file.close() #text file close


def speak(text):
	tts = gTTS(text=text,lang='en') #google text to speech
	filename = 'voice1.mp3'
	tts.save(filename) # voice file created and save in same folder
	#playsound.playsound(filename)
	#mixer.init()
	#mixer.music.load('voice1.mp3')
	#mixer.music.play()
speak(ajay)

mixer.init()

mixer.music.load('voice1.mp3')

time.sleep(0.2)

mixer.music.play()
#mixer.music.fadeout(4000)
while mixer.music.get_busy() == True: # imp line without this audio is not working 
    continue






