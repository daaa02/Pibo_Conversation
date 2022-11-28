#!/usr/bin/python3

# behavior = motion + eye + oled + sound

# python module
import os
import sys
import time
import json
from threading import Thread

# openpibo module
import openpibo
from openpibo.motion import Motion
from openpibo.device import Device
from openpibo.oled import Oled

# my module
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append('/home/pi/Conversation_Scenarios')
import eye_list as eye
import oled_list as oled


disp = Oled()
motion = Motion()

from conversation_manage import ConversationManage
from text_to_speech import TextToSpeech, text_to_speech
    
"""
Motion 하는 동안 (효과음 -> TTS & EYE & OLED)
"""

def aaa(text, behav):
    
    a = Thread(target=behav, args=())
    a.daemon = True 
    a.start()
    
    def do_question_L():
        audio_play(filename="/home/pi/Pibo_Conversation/data/audio/물음표소리1.wav", out='local', volume=-1500, background=False)

        t = Thread(target=text_to_speech, args=(text))
        o = Thread(target=oled.o_question, args=())
        # e = Thread(target=eye.e_question, args=())

        t.daemon = True
        o.daemon = True
        # e.daemon = True   

        t.start()
        o.start()
        # e.start()
        
        while True:
            motion.set_motion(name="m_question_L", cycle=1)
            break
    
if __name__ == "__main__":
    aaa("안녕하세요 안녕하세요", behav=do_question_L)