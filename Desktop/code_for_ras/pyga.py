
'''
import pygame as pg 
def play_music(music_file):
	pg.mixer.init()
	clock = pg.time.Clock()
	try:
		pg.mixer.music.load(music_file)
		print("Music file {} loaded!".format(music_file))
	except pg.error:
		print("File {} not found! ({})".format(music_file, pg.get_error()))
	return
	pg.mixer.music.play()
	while pg.mixer.music.get_busy():
        # check if playback has finished
		clock.tick(30)

music_file ="Vibe.mp3"



play_music(music_file)'''


