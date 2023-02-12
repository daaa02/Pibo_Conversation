# -*- coding: utf-8 -*-

# 동화-카네이션

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
                
        
    def Carnation(self):
        
        # 1. 동화 줄거리 대화        
        cm.tts(bhv="do_joy_A", string=f"정말 재미있는 이야기였어! {wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?")
        answer = cm.responses_proc(re_bhv="do_joy_A", re_q=f"{wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?",
                                   neu_bhv="do_agree", neu=f"그럴 수 있지~")
        
        cm.tts(bhv="question_S", string=f"{wm.word(self.user_name, 0)}는 어떤 소원이 있니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}는 어떤 소원이 있니?", 
                                   pos_bhv="do_question_S", pos=f"{wm.word(self.user_name, 0)}의 소원은 어떻게 하면 이루어질까?", 
                                   neu_bhv="do_agree", neu=f"모를 수 있어~", 
                                   act_bhv="do_question_S", act=f"{wm.word(self.user_name, 0)}의 소원은 어떻게 하면 이루어질까?")
        
        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}의 소원은 어떻게 하면 이루어질까?", 
                                       pos_bhv="do_agree", pos=f"{wm.word(self.user_name, 0)}의 소원이 꼭 이루어졌으면 좋겠다~", 
                                       act_bhv="do_agree", act=f"{wm.word(self.user_name, 0)}의 소원이 꼭 이루어졌으면 좋겠다~")
            
        cm.tts(bhv="question_S", string=f"{wm.word(self.user_name, 0)}가 좋아하는 꽃이 있다면 말해줄래?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}가 좋아하는 꽃이 있다면 말해줄래?", 
                                   pos_bhv="do_question_S", pos=f"그 꽃을 좋아하는 이유는 뭐니?", 
                                   act_bhv="do_question_S", act=f"그 꽃을 좋아하는 이유는 뭐니?")
        
        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"그 꽃을 좋아하는 이유는 뭐니?", 
                                       neu_bhv="do_agree", neu=f"괜찮아~ 생각 나지 않을 수 있어~")
                                       
        cm.tts(bhv="question_S", string=f"소년과 소녀는 행복하게 살았을 것 같니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"소년과 소녀는 행복하게 살았을 것 같니?", 
                                   pos_bhv="do_joy_A", pos=f"소년과 소녀가 행복했으면 좋겠다~", 
                                   act_bhv="do_joy_A", act=f"소년과 소녀가 행복했으면 좋겠다~")

        # 2. 등장인물 공감 대화        
        cm.tts(bhv="question_S", string=f"요리사의 거짓말 때문에 왕비가 탑에 갇혔을 때 왕비는 속상했을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"요리사의 거짓말 때문에 왕비가 탑에 갇혔을 때 왕비는 속상했을까?", 
                                   pos_bhv="do_question_S", pos=f"{wm.word(self.user_name, 0)}도 누군가가 거짓말을 해서 속상했던 적이 있었다면 말해줄래?", 
                                   neu_bhv="do_agree", neu=f"몰라도 괜찮아~", 
                                   act_bhv="do_question_S", act=f"{wm.word(self.user_name, 0)}도 누군가가 거짓말을 해서 속상했던 적이 있었다면 말해줄래?")

        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}도 누군가가 거짓말을 해서 속상했던 적이 있었다면 말해줄래?",
                                       neg_bhv="do_agree", neg=f"정말 기분이 안 좋았을 것 같아!",
                                       neu_bhv="do_agree", neu=f"모를 수 있지~", 
                                       act_bhv="do_sad", act=f"정말 기분이 안 좋았을 것 같아!")
            
        cm.tts(bhv="question_S", string=f"소녀가 왕자을 구해줬을 때 왕자는 고마웠을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"소녀가 왕자을 구해줬을 때 왕자는 고마웠을까?", 
                                   pos_bhv="do_question_S", pos=f"{wm.word(self.user_name, 0)}도 최근에 도움을 받고 고마움을 느낀 적이 있니?", 
                                   neu_bhv="do_agree", neu=f"괜찮아~ 대답하기 어려울 수 있어~", 
                                   act_bhv="do_question_S", act=f"{wm.word(self.user_name, 0)}도 최근에 도움을 받고 고마움을 느낀 적이 있니?")

        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}도 최근에 도움을 받고 고마움을 느낀 적이 있니?",
                                       pos_bhv="do_sad", pos=f"정말 고마웠겠다!",
                                       act_bhv="do_sad", act=f"정말 고마웠겠다!")
        
            
        # 3. 마무리 대화    
        cm.tts(bhv="do_question_L", string=f"만약 {wm.word(self.user_name, 0)}가 동화 속 막내 왕자를 만난다면 어떤 말을 해주고 싶니?")
        answer = cm.responses_proc(re_bhv="do_question_L", string=f"만약 동화 속 막내 왕자를 만난다면 어떤 말을 해주고 싶니?",  
                                   pos_bhv="do_agree", pos=f"그렇구나!",
                                   neu_bhv="do_agree", neu=f"괜찮아~ 모를 수 있지~ ",
                                   neg_bhv="do_agree", neg=f"그렇구나!",
                                   act_bhv="do_agree", act=f"그렇구나!")
        
        cm.tts(bhv="do_explain_C", string=f"오늘 동화 재미있었지? 다음에 또 재미있는 동화를 들려줄게~")
        
        
        
        
if __name__ == "__main__":    
    
    fat = Fairytale()
    fat.Carnation()
