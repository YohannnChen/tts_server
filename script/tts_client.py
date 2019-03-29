#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import rospy
from tts_server.srv import *

def tts_client(text):
    rospy.wait_for_service('TTS')
    try:
        tts_result = rospy.ServiceProxy('TTS', TTSsrv)
        resp1 = tts_result(text)
        return resp1.result
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "wrong input"

if __name__ == "__main__":
    if len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        print usage()
        sys.exit(1)
    print "Requesting %s to speech"%(text)
    result=tts_client(text)
    if result==0:
        print "Succeed"
    else:
        print "Fail"

