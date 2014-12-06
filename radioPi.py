#!/usr/bin/python
import time
import os
import RPi.GPIO as GPIO
GPIO.setmode (GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(18, GPIO.IN)

#Start mpd
#os.system("mpd") #Already running on startup

#Scan for bbc radio & add stations to playlist
os.system("./bbcRadio")

#Start mpc
os.system("mpc play")

#Set variables
pause = False

#Buttons
while True:

	#Assign buttons to GPIO input pins

	pauseButton = GPIO.input(18)
	prevButton = GPIO.input(11)
	nextButton = GPIO.input(12)

	#Prevous button, if paused scan for radio stations else skip to prevous song/station

	if prevButton == False:
		if pause == True:
			pause = False
			os.system("./bbcRadio")
			os.system("mpc play")
		elif pause == False:
			os.system("mpc prev")
			time.sleep(.2)

	#Next button, if paused stop player and shutdown else skip to next song/station

	elif nextButton == False:
		if pause == True:
			os.system("mpc stop")
			os.system("sudo halt")
		elif pause == False:
			os.system("mpc next")
			time.sleep(.2)

	#Pause button, toggle pause on off

	elif pauseButton == False:
		os.system("mpc toggle")
		if pause == False:
			pause = True
		elif pause == True:
			pause = False
		time.sleep(.2)
