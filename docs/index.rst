RaspberryPi-Radio
=================

Python script to control mpc using GPIO pins on Raspberry Pi

The script allows for setup of 3 tactile switches and two playlists:

1. songs
2. radio

The idea being songs contains your music and radio contains internet streams. These can then be toggled between via a switch. The 3 switches have slightly different functions depending if in Music or Radio mode. 

Music mode: 

Button 1 - previous track 
Button 2 - next track 
Button 3 - pause/play 
Button 3 and then button 1 switch to radio mode
Button 3 and then button 2 shutdown Pi 

Radio mode: 

Button 1 - previous station 
Button 2 - next station
Button 3 - pause/play
Button 3 and then button 1 switch to music player mode
Button 3 and then button 2 shutdown Pi
