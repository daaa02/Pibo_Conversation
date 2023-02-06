# -*- coding: utf-8 -*-

# 동화-가난뱅이와 부자

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
                
        
    def Poor(self):
        
        # 1. 동화 줄거리 대화        
        cm.tts(bhv="do_joy_A", string=f"정말 재미있는 이야기였어! {wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?")
        answer = cm.responses_proc(re_bhv="do_joy_A", re_q=f"{wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?",
                                   neu_bhv="do_agree", neu=f"그럴 수 있지~")
        
        cm.tts(bhv="question_S", string=f"{wm.word(self.user_name, 0)}도 친구를 도와준 적이 있으면 말해줄래?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}도 친구를 도와준 적이 있으면 말해줄래?", 
                                   pos_bhv="do_question_S", pos=f"도와준 뒤에 {wm.word(self.user_name, 0)} 마음은 어땠니?", 
                                   neu_bhv="do_agree", neu=f"모를 수있지~", 
                                   act_bhv="do_question_S", act=f"도와준 뒤에 {wm.word(self.user_name, 0)} 마음은 어땠니?")
        
        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"도와준 뒤에 {wm.word(self.user_name, 0)} 마음은 어땠니?", 
                                       pos_bhv="do_agree", pos=f"그렇게 생각했었구나!", 
                                       neu_bhv="do_agree", neu=f"모를 수 있지~", 
                                       act_bhv="do_agree", act=f"그렇게 생각했었구나!")
        
        cm.tts(bhv="question_S", string=f"{wm.word(self.user_name, 0)}는 부자가 되면 어떤 소원을 빌 것 같아?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}는 부자가 되면 어떤 소원을 빌 것 같아?", 
                                   pos_bhv="do_question_S", pos=f"또 다른 소원도 말해봐!", 
                                   neu_bhv="do_agree", neu=f"몰라도 괜찮아~", 
                                   act_bhv="do_question_S", act=f"또 다른 소원도 말해봐!")

        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"또 다른 소원도 말해봐!", 
                                       pos_bhv="do_joy_A", pos=f"소원이 다 이루어지면 좋겠다!", 
                                       act_bhv="do_joy_A", act=f"소원이 다 이루어지면 좋겠다!")
        
        cm.tts(bhv="suggestion_S", string=f"하느님이 선물로 준 새 집은 어떻게 생겼을 것 같아?")
        answer = cm.responses_proc(re_bhv="do_suggestion_S", re_q=f"하느님이 선물로 준 새 집은 어떻게 생겼을 것 같아?", 
                                   pos_bhv="do_agree", pos=f"진짜 멋지겠지?", 
                                   act_bhv="do_agree", act=f"진짜 멋지겠지?")
        
        # 2. 등장인물 공감 대화
        cm.tts(bhv="question_S", string=f"부자가 도와주지 않았을 때 하느님은 슬펐겠지?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"부자가 도와주지 않았을 때 하느님은 슬펐겠지?", 
                                   pos_bhv="do_question_L", pos=f"누군가 {wm.word(self.user_name, 0)}를 도와주지 않아서 슬펐던 적 있다면 말해줄래?", 
                                   neu_bhv="do_agree", neu=f"괜찮아~ 대답하기 어려울 수 있어~", 
                                   act_bhv="do_question_L", act=f"누군가 {wm.word(self.user_name, 0)}를 도와주지 않아서 슬펐던 적 있다면 말해줄래?")

        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"누군가 {wm.word(self.user_name, 0)}를 도와주지 않아서 슬펐던 적 있다면 말해줄래?")
                
        cm.tts(bhv="question_S", string=f"가난뱅이가 도와줬을을 때 하느님은 기뻤을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"가난뱅이가 도와줬을을 때 하느님은 기뻤을까?", 
                                   pos_bhv="do_question_S", pos=f"{wm.word(self.user_name, 0)}도 도움을 받고 기뻤던 적 있다면 말해줄래?", 
                                   act_bhv="do_question_S", act=f"{wm.word(self.user_name, 0)}도 도움을 받고 기뻤던 적 있다면 말해줄래?")
        
        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}도 도움을 받고 기뻤던 적 있다면 말해줄래?", 
                                       pos_bhv="do_joy_B", pos=f"그런 일이 있었구나! 정말 기분 좋았겠다!", 
                                       act_bhv="do_joy_B", act=f"그런 일이 있었구나! 정말 기분 좋았겠다!")
        
        # 3. 마무리 대화        
        cm.tts(bhv="do_question_L", string=f"만약 {wm.word(self.user_name, 0)}가 동화 속 다른 사람을 도와주는 착한 가난뱅이를 만난다면 뭐라고 해줄 수 있을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", string=f"만약 동화 속 다른 사람을 도와주는 착한 가난뱅이를 만난다면 뭐라고 해줄 수 있을까?",  
                                   pos_bhv="do_agree", pos=f"그렇구나!",
                                   neu_bhv="do_agree", neu=f"괜찮아~ 모를 수 있지~ ",
                                   neg_bhv="do_agree", neg=f"그렇구나!",
                                   act_bhv="do_agree", act=f"그렇구나!")
        
        cm.tts(bhv="do_explain_C", string=f"오늘 동화 재미있었지? 다음에 또 재미있는 동화를 들려줄게~")
        
        
        
if __name__ == "__main__":    
    
    fat = Fairytale()
    fat.Poor()