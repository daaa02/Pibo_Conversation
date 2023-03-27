# -*- coding: utf-8 -*-

# 동화-여왕벌

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
                
        
    def Queenbee(self):
        
        # 1. 동화 줄거리 대화        
        cm.tts(bhv="do_joy_A", string=f"정말 재미있는 이야기였어! {wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?")
        answer = cm.responses_proc(re_bhv="do_joy_A", re_q=f"{wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?",
                                   neu_bhv="do_agree", neu=f"그럴 수 있지~")
        
        cm.tts(bhv="do_question_S", string=f"개미들이 찾아준 천 개의 진주로 무엇을 만들었을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"물건을 잃어버렸을 때는 어떻게 찾아야할까?", 
                                   neu_bhv="do_agree", neu=f"괜찮아~ 대답하기 어려울 수 있어~")

        cm.tts(bhv="do_question_S", string=f"만약 막내 왕자도 개미를 괴롭혔다면 개미들은 막내를 도와줬을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}도 물건을 물 속에 빠뜨린 적 있니?", 
                                   neu_bhv="do_agree", neu=f"괜찮아~ 생각나지 않을 수 있어~")   
        
        cm.tts(bhv="do_question_S", string=f"돌이 된 형들은 무슨 생각을 했을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"돌이 된 형들은 무슨 생각을 했을까?", 
                                   neu_bhv="do_agree", neu=f"모를 수 있어~")  

        # 2. 등장인물 공감 대화        
        cm.tts(bhv="do_question_S", string=f"난쟁이에게 어려운 임무를 받았을 때 막내 왕자는 실패할까봐 걱정했겠지?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"물건을 잃어버렸을 때는 어떻게 찾아야할까?", 
                                   pos_bhv="do_question_S", pos=f"{wm.word(self.user_name, 0)}도 최근에 걱정이 되는 일이 있었다면 말해 줄래?", 
                                   neu_bhv="do_agree", neu=f"몰라도 괜찮아~", 
                                   act_bhv="do_question_S", act=f"{wm.word(self.user_name, 0)}도 최근에 걱정이 되는 일이 있었다면 말해 줄래?")

        if answer[0][0] == "positive" or answer[0][0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}도 최근에 걱정이 되는 일이 있었다면 말해 줄래?",
                                       act_bhv="do_sad", act=f"걱정됐겠구나!")
            
        cm.tts(bhv="do_question_S", string=f"개미랑 여왕벌이 도와주었을 때 막내 왕자는 감동 받았을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"개미랑 여왕벌이 도와주었을 때 막내 왕자는 감동 받았을까?", 
                                   pos_bhv="do_question_S", pos=f"{wm.word(self.user_name, 0)}도 최근에 감동 받은 적이 있다면 말해 줄래?", 
                                   neu_bhv="do_agree", neu=f"괜찮아~ 대답하기 어려울 수 있어~", 
                                   act_bhv="do_question_S", act=f"{wm.word(self.user_name, 0)}도 최근에 감동 받은 적이 있다면 말해 줄래?")

        if answer[0][0] == "positive" or answer[0][0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}도 최근에 감동 받은 적이 있다면 말해 줄래?",
                                       pos_bhv="do_sad", pos=f"그런 일이 있었구나! 정말 기분이 좋았겠다!",
                                       act_bhv="do_sad", act=f"그런 일이 있었구나! 정말 기분이 좋았겠다!")
        
            
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
    fat.Queenbee()
