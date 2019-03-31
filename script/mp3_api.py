#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from playsound import playsound
# playsound('/home/dl/catkin_ws/src/tts_server/mp3/谢谢.mp3')



# from pygame import mixer # Load the required library
# mixer.init()
# mixer.music.load('/home/dl/catkin_ws/src/tts_server/mp3/谢谢.mp3')
# mixer.music.play()



# import os
# os.system('/home/dl/catkin_ws/src/tts_server/mp3/谢谢.mp3')


# from pydub import AudioSegment
# from pydub.playback import play
# song = AudioSegment.from_mp3("谢谢.mp3")
# play(song)




# sudo apt-get install mpg123
import subprocess
subprocess.Popen(['mpg123', '-q', '/home/dl/catkin_ws/src/tts_server/mp3/谢谢.mp3']).wait()
