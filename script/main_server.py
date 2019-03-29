#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tts_server.srv import *
from aip import AipSpeech
import rospy
from playsound import playsound
import os

path =os.path.dirname(os.path.realpath(__file__))+'/mp3/'

def handle_tts(req):

    APP_ID = '15844718'
    API_KEY = 'OOGuG62OAlu63CBfpKa8NLr7'
    SECRET_KEY = 'SYC2Gk63myGcHXMv3vg46o212FtjK7ZT'

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result = client.synthesis(req.text, 'zh', 1, {'vol': 5,})

    # 识别正确返回语音二进制 错误则返回dict 
    if not isinstance(result, dict):

	if not os.path.exists(path):
	     os.makedirs(path)
        print(path+req.text+'.mp3')
        with open(path+req.text+'.mp3', 'wb') as f:
            f.write(result)
        
        playsound(path+req.text+'.mp3')
        print "Transform %s succesfully" % (req.text)
        return 0
    else:
        print(result)
        return 1


def tts_server():

    rospy.init_node('TTS_server')
    s = rospy.Service('TTS', TTSsrv, handle_tts)
    print "Ready to do TTS work"
    rospy.spin()

if __name__ == "__main__":
    tts_server()
