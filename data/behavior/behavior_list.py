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
sys.path.append('/home/pi/AI_pibo2')
import eye_list as eye
import display_list as oled
from text_to_speech import TextToSpeech, text_to_speech

disp = Oled()
motion = Motion()
audio = TextToSpeech()


def do_question_L():
    eye.e_question()
    t = Thread(target=oled.o_question, args=(), daemon=True)
    t.start()
    while True: 
        audio.audio_play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav", out='local', volume=-1200, background=True)
        motion.set_motion(name="m_question_L", cycle=1)
        break
    
    
def do_question_S():
    eye.e_question()
    while True:
        audio.audio_play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav", out='local', volume=-1200, background=True)
        motion.set_motion(name="m_question_S", cycle=1)
        break
    

def do_suggestion_L():
    eye.e_suggestion()
    t = Thread(target=oled.o_suggestion, args=(), daemon=True)
    t.start()
    while True:
        motion.set_motion(name="m_suggestion_L", cycle=1)
        break
    
    
def do_suggestion_S():
    eye.e_suggestion()
    t = Thread(target=oled.o_suggestion, args=(), daemon=True)
    t.start()
    while True:
        motion.set_motion(name="m_suggestion_S", cycle=1)
        break
    
    
def do_explain_A():
    eye.e_explain()
    t = Thread(target=oled.o_explain, args=(), daemon=True)
    t.start()
    while True:
        motion.set_motion(name="m_explain_A", cycle=1)
        break
    
    
def do_explain_B():
    eye.e_explain()
    t = Thread(target=oled.o_explain, args=(), daemon=True)
    t.start()
    while True:
        motion.set_motion(name="m_explain_B", cycle=1)
        break


def do_photo():
    eye.e_photo()
    t = Thread(target=oled.o_photo, args=(), daemon=True)
    t.start()
    while True:
        motion.set_motion(name="m_photo-1", cycle=1)
        break
    audio.audio_play(filename="/home/pi/AI_pibo2/src/data/audio/사진기소리.mp3", out='local', volume=-1000, background=True)
    while True:
        motion.set_motion(name="m_photo-2", cycle=1)
        break


def do_stamp():
    eye.e_stamp()
    t = Thread(target=oled.o_stamp, args=(), daemon=True)
    t.start()
    while True:
        motion.set_motion(name="m_stamp-1", cycle=1)        
        break
    audio.audio_play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1500, background=True)
    while True:
        motion.set_motion(name="m_stamp-2", cycle=1)        
        break


def do_waiting_A():
    eye.e_waiting()
    t = Thread(target=oled.o_waiting, args=(), daemon=True)
    t.start()
    while True:
        motion.set_motion(name="m_waiting_A", cycle=1)
        break
    

def do_waiting_B():
    eye.e_waiting()
    t = Thread(target=oled.o_waiting, args=(), daemon=True)
    t.start()
    while True:
        motion.set_motion(name="m_waiting_B", cycle=1)
        break
    
 
def do_waiting_C():
    eye.e_waiting()
    t = Thread(target=oled.o_waiting, args=(), daemon=True)
    t.start()  
    while True:
        motion.set_motion(name="m_waiting_C", cycle=1)
        break
    
def do_wakeup():
    oled.o_wakeup()
    eye.e_compliment()
    t = Thread(target=oled.o_wakeup, args=(), daemon=True)
    t.start()
    while True:
        audio.audio_play(filename="/home/pi/AI_pibo2/src/data/audio/경쾌한음악.wav", out='local', volume=-1500, background=True)
        motion.set_motion(name="m_wakeup", cycle=1)
        break
    
    
def do_compliment_L():
    oled.o_compliment()
    eye.e_compliment()
    while True:
        audio.audio_play(filename="/home/pi/AI_pibo2/src/data/audio/경쾌한음악.wav", out='local', volume=-1200, background=True)
        motion.set_motion(name="m_compliment_L", cycle=1)
        break
    
    
def do_compliment_S():    
    oled.o_compliment()
    eye.e_compliment()
    while True:
        audio.audio_play(filename="/home/pi/AI_pibo2/src/data/audio/경쾌한음악.wav", out='local', volume=-1200, background=True)
        motion.set_motion(name="m_compliment_S", cycle=1)
        break


def do_agree():
    eye.e_agree()
    t = Thread(target=oled.o_agree, args=(), daemon=True)
    t.start()
    while True:
        audio.audio_play(filename="/home/pi/AI_pibo2/src/data/audio/딩동댕3.wav", out='local', volume=-1200, background=True)
        motion.set_motion(name="m_agree", cycle=1)
        break

def do_joy_A():
    eye.e_joy()
    t = Thread(target=oled.o_joy, args=(), daemon=True)
    t.start()
    while True:
        audio.audio_play(filename="/home/pi/AI_pibo2/src/data/audio/기분좋음.wav", out='local', volume=-1200, background=True)
        motion.set_motion(name="m_joy_A", cycle=1)
        break


def do_joy_A():
    eye.e_joy()
    t = Thread(target=oled.o_joy, args=(), daemon=True)
    t.start()
    while True:
        audio.audio_play(filename="/home/pi/AI_pibo2/src/data/audio/기분좋음.wav", out='local', volume=-1200, background=True)
        motion.set_motion(name="m_joy_B", cycle=1)
        break
    
    
def do_sad():
    eye.e_sad()
    t = Thread(target=oled.o_sad, args=(), daemon=True)
    t.start()
    while True:
        audio.audio_play(filename="/home/pi/AI_pibo2/src/data/audio/슬픈소리.wav", out='local', volume=-1500, background=True)
        motion.set_motion(name="m_sad", cycle=1)
        break
    
if __name__ == "__main__":
    do_explain_A()