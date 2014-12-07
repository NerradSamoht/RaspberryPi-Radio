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

#Set variables
pause = False
radio = False

#Clear mpc, load and play
os.system("mpc clear")
os.system("mpc load songs")
os.system("mpc play")

#Buttons
while True:
	
	#Assign buttons to GPIO input pins
	pauseButton = GPIO.input(18)
	prevButton = GPIO.input(11)
	nextButton = GPIO.input(12)

	#Previous button, if paused switch to radio stations else skip to previous song/station
	if prevButton == False:
		if pause == True:
			if radio == True:
				pause = False
				radio = False
				os.system("mpc clear")
				os.system("mpc load songs")
				os.system("mpc random")
				os.system("mpc play")
				time.sleep(.2)
			elif pause == False:
				pause = False
				radio = True
				os.system("mpc clear")
				os.system("mpc random")
				os.system("mpc load radio")
				os.system("mpc play")
				time.sleep(.2)
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
