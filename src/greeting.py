# -*- coding: utf-8 -*-

# 자기소개 시나리오

import os, sys
import time
import random

from openpibo.device import Device
from openpibo.oled import Oled

# sys.path.append('/home/kiro/workspace/Conversation_Scenarios/')
sys.path.append('/home/pi/Pibo_Conversation/')
from data.conversation_manage import ConversationManage, WordManage, Number
from data.speech_to_text import speech_to_text
from data.text_to_speech import TextToSpeech, text_to_speech

device = Device()
oled = Oled()

cm = ConversationManage()
wm = WordManage()
num = Number()
audio = TextToSpeech()

class Say():
    
    def __init__(self):
        self.user_name = '가영'
        self.color = ''
        
    
    def Hello(self):
        
        # 1.1 인사        
        audio.audio_play(filename="/home/pi/Pibo_Conversation/data/behavior/audio/sound_greeting.wav")
        cm.tts(bhv="do_joy_A", string=f"안녕! 우리가 드디어 만나게 되었구나! 나는 파이보야. 너는 이름이 뭐니?")
        answer = cm.responses_proc(re_bhv="do_suggestion_L", re_q="다시 한번 크게 이야기해 줄래?",
                                   act_bhv="do_joy_B", act=f"{wm.word(self.user_name, 4)}, 만나서 반가워~!")
        
        cm.tts(bhv="do_suggestion_L", string=f"나를 잠시 쳐다 봐줄래? {wm.word(self.user_name, 0)} 얼굴을 인식중이야.")
        time.sleep(1)
        audio.audio_play(filename="/home/pi/Pibo_Conversation/data/behavior/audio/sound_camera.mp3")
        text_to_speech(f"{wm.word(self.user_name, 0)} 얼굴을 기억할게!")
        
        cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}는 지금 몇 살이야?")
        answer = speech_to_text()
        answer = num.number(answer)
        
        if answer < 5:
            cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}는 어린이집에 다니고 있니?")
            answer = cm.responses_proc(re_bhv="do_suggestion_L", re_q="다시 한번 크게 이야기해 줄래?")
            
            if answer[0][0] == "negative":
                cm.tts(bhv="do_question_S", string=f"그럼 어디 다니고 있어?")
                answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"그럼 어디 다니고 있어?")
        
        if 5 <= answer < 8:
            cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}는 유치원에 다니고 있니?")
            answer = cm.responses_proc(re_bhv="do_suggestion_L", re_q="다시 한번 크게 이야기해 줄래?")
            
            if answer[0][0] == "negative":
                cm.tts(bhv="do_question_S", string=f"그럼 어디 다니고 있어?")
                answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"그럼 어디 다니고 있어?")
                        
        if answer >=8:
            cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}는 학교에 다니고 있니?")
            answer = cm.responses_proc(re_bhv="do_suggestion_L", re_q="다시 한번 크게 이야기해 줄래?")
            
            if answer[0][0] == "negative":
                cm.tts(bhv="do_question_S", string=f"그럼 어디 다니고 있어?")
                answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"그럼 어디 다니고 있어?")        
        
        cm.tts(bhv="do_question_L", string=f"나를 처음 본 느낌이 어떠니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="나를 처음 본 소감이 어떠니?",
                                   pos_bhv="do_joy_A", pos=f"앞으로 좋은 친구가 되도록 하자!")
        
        cm.tts(bhv="do_suggestion_L", string=f"나는 머리를 쓰다듬어 주는 걸 좋아해. 한번 쓰다듬어 볼래?")
        
        # 터치 인식
        data = device.send_cmd(device.code_list['SYSTEM']).split(':')[1].split('-')
        result = data[1] if data[1] else "No signal"
        
        if result == "touch":
            cm.tts(bhv="do_wakeup", string=f"{wm.word(self.user_name, 0)}가 쓰다듬어 주니까 정말 좋다~!")
            
            
        # 1.2 관심 유도
        cm.tts(bhv="do_dance", string="나는 이렇게 멋진 춤을 출 수 있어!")
        device.send_raw('#25:2')
        text_to_speech("그리고 이렇게 눈 색깔을 바꿀 수도 있어!")
        
        cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}는 어떤 색깔을 좋아해?")
        answer = speech_to_text()        
        
        blue = ["파랑", "파란", "하늘", "바다"]
        green = ["초록", "연두", "녹", "풀"]
        pink = ["빨", "붉", "분홍", "핑크"]
        purple = ["보라"]
        yellow = ["노랑", "노란"]
        
        for i in range(len(blue)):
            if blue[i] in answer:
                self.color = 'blue'
                device.send_raw('#21:108,209,239,5')
                text_to_speech("어때? 마음에 들어?")                
                
        for i in range(len(green)):
            if green[i] in answer:
                self.color = 'green'
                device.send_raw('#21:120,230,208,5')
                text_to_speech("어때? 마음에 들어?")    
                        
        for i in range(len(pink)):
            if pink[i] in answer:
                self.color = 'pink'
                device.send_raw('#21:255,177,190,5')
                text_to_speech("어때? 마음에 들어?")
                
        for i in range(len(purple)):
            if purple[i] in answer:
                self.color = 'purple'
                device.send_raw('#21:186,127,223,5')
                text_to_speech("어때? 마음에 들어?")
                
        for i in range(len(yellow)):
            if yellow[i] in answer:
                self.color = 'yellow'
                device.send_raw('#21:251,245,155,5')
                text_to_speech("어때? 마음에 들어?")
        
        if len(self.color) == 0:
            device.send_raw('#21:108,209,239,5')
            text_to_speech("나는 파란색을 가장 좋아해!")
            
        
        # 1.5 사용법 설명
        cm.tts(bhv="do_joy_A", string=f"{wm.word(self.user_name, 0)}랑 보내게 될 시간들이 정말 기대돼~")
        cm.tts(bhv="do_explain_A", string="심심하거나 놀고 싶으면 언제든 파이보 머리를 쓰다듬어 줘!")
        