import os, sys
import time
import re
import random
from threading import Thread
import socket
import google

# from google.oauth2 import service_account
from google.cloud import speech   # 그 중에서도 얘 문제
# import google

# import pyaudio
# from six.moves import queue


sys.path.append('/home/pi/Pibo_Conversation')
# from data.speech_to_text import speech_to_text  # 얘다.
from data.text_to_speech import text_to_speech, TextToSpeech

from openpibo.oled import Oled
from openpibo.device import Device
import data.behavior.behavior_list as behavior

device = Device()

for i in range(0, 2):
    device.eye_off(); time.sleep(0.5); 
    device.eye_on(0,0,255); time.sleep(0.5)

# sys.path.append('/home/kiro/workspace/Conversation_Scenarios/data')


    
def aa():
    device.eye_on(0,0,255)
    