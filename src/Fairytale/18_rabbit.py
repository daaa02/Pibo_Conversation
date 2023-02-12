# -*- coding: utf-8 -*-

# 동화-토끼와 거북이

import os, sys
import re
import random

# sys.path.append('/home/kiro/workspace/Conversation_Scenarios/')
sys.path.append('/home/pi/Pibo_Conversation/')
from data.conversation_manage import ConversationManage, WordManage
from data.speech_to_text import speech_to_text
from data.text_to_speech import TextToSpeech, text_to_speech

cm = ConversationManage()
wm = WordManage()
audio = TextToSpeech()


class Fairytale():    
    
    def __init__(self): 
        self.user_name = '가영'
                
        
    def Rabbit(self):
        
        # 1. 동화 줄거리 대화        
        cm.tts(bhv="do_joy_A", string=f"정말 재미있는 이야기였어! {wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?")
        answer = cm.responses_proc(re_bhv="do_joy_A", re_q=f"{wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?",
                                   neu_bhv="do_agree", neu=f"그럴 수 있지~")
        
        cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}도 달리기 시합을 한 적이 있니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}도 달리기 시합을 한 적이 있니?", 
                                   pos_bhv="do_question_S", pos=f"언제 해봤니?", 
                                   neu_bhv="do_agree", neu=f"몰라도 괜찮아~", 
                                   act_bhv="do_question_S", act=f"언제 해봤니?")
        
        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"언제 해봤니?")
            
        cm.tts(bhv="do_question_S", string=f"토끼와 {wm.word(self.user_name, 0)}가 달리기 경주를 하면 누가 이길까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"토끼와 {wm.word(self.user_name, 0)}가 달리기 경주를 하면 누가 이길까?",
                                   act_bhv="do_agree", act=f"그렇게 생각하는 구나!")
        
        cm.tts(bhv="do_question_S", string=f"거북이와 토끼가 바다 속 에서 헤엄치기 경주를 했다면 누가 이겼을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"거북이와 토끼가 바다 속 에서 헤엄치기 경주를 했다면 누가 이겼을까?",
                                   neu_bhv="do_question_S", neu=f"괜찮아~ 대답하기 어려울 수 있어~")

        # 2. 등장인물 공감 대화        
        cm.tts(bhv="question_S", string=f"다른 동물들은 경기 시작 전 어떤 동물이 이길 것 같다고 예상했을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"다른 동물들은 경기 시작 전 어떤 동물이 이길 것 같다고 예상했을까?", 
                                   pos_bhv="do_question_S", pos=f"{wm.word(self.user_name, 0)}는 누가 이길 것 같다고 생각했니?", 
                                   neu_bhv="do_agree", neu=f"괜찮아~ 생각 나지 않을 수 있어~", 
                                   act_bhv="do_question_S", act=f"{wm.word(self.user_name, 0)}는 누가 이길 것 같다고 생각했니?")

        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}는 누가 이길 것 같다고 생각했니?",
                                       neu_bhv="do_agree", neu=f"몰라도 괜찮아~", 
                                       act_bhv="do_sad", act=f"그렇게 생각했구나!")
            
        cm.tts(bhv="question_S", string=f"결승선에 먼저 도착한 거북이는 기뻤을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"결승선에 먼저 도착한 거북이는 기뻤을까?", 
                                   pos_bhv="do_question_S", pos=f"{wm.word(self.user_name, 0)}도 최근에 기쁜 일이 있었다면 이야기 해줄래?", 
                                   neu_bhv="do_agree", neu=f"괜찮아~ 대답하기 어려울 수 있어~", 
                                   act_bhv="do_question_S", act=f"{wm.word(self.user_name, 0)}도 최근에 기쁜 일이 있었다면 이야기 해줄래?")

        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}도 최근에 기쁜 일이 있었다면 이야기 해줄래?",
                                       pos_bhv="do_sad", pos=f"정말 기분이 좋았겠다!",
                                       act_bhv="do_sad", act=f"정말 기분이 좋았겠다!")        
            
        # 3. 마무리 대화    
        cm.tts(bhv="do_question_L", string=f"만약 {wm.word(self.user_name, 0)}가 동화 속 거북이를 만난다면 어떤 칭찬을 해주고 싶니?")
        answer = cm.responses_proc(re_bhv="do_question_L", string=f"동화 속 거북이를 만난다면 어떤 칭찬을 해주고 싶니?",  
                                   pos_bhv="do_agree", pos=f"그렇구나!",
                                   neu_bhv="do_agree", neu=f"괜찮아~ 생각이 안날 수 있지~ ",
                                   neg_bhv="do_agree", neg=f"그렇구나!",
                                   act_bhv="do_agree", act=f"그렇구나!")
        
        cm.tts(bhv="do_explain_C", string=f"오늘 동화 재미있었지? 다음에 또 재미있는 동화를 들려줄게~")
        
        
        
        
if __name__ == "__main__":    
    
    fat = Fairytale()
    fat.Rabbit()
