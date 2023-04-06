import os, sys
import re
import time
import random
import socket
from threading import Thread

# sys.path.append('/home/kiro/workspace/Conversation_Scenarios/data')
sys.path.append('/home/pi/Pibo_Conversation')

import google
from data.speech_to_text import speech_to_text
from data.text_to_speech import text_to_speech, TextToSpeech


from openpibo.oled import Oled
from openpibo.device import Device
import data.behavior.behavior_list as behavior

device = Device()

for i in range(0, 2):
    device.eye_off(); time.sleep(0.5); 
    device.eye_on(0,0,255); time.sleep(0.5)

    
def aa():
    for i in range(0, 2):
        device.eye_off(); time.sleep(0.5); 
        device.eye_on(0,0,255); time.sleep(0.5)
    