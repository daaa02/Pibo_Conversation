# -*- coding: utf-8 -*-

# 동화-헤르메스 신과 나무꾼

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
                
        
    def Hermes(self):
        
        # 1. 동화 줄거리 대화        
        cm.tts(bhv="do_joy_A", string=f"정말 재미있는 이야기였어! {wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?")
        answer = cm.responses_proc(re_bhv="do_joy_A", re_q=f"{wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?",
                                   neu_bhv="do_agree", neu=f"그럴 수 있지~")
        
        cm.tts(bhv="question_S", string=f"물건을 잃어버렸을 때는 어떻게 찾아야할까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"물건을 잃어버렸을 때는 어떻게 찾아야할까?", 
                                   pos_bhv="do_question_S", pos=f"다영이도 물건을 물 속에 빠뜨린 적 있니?", 
                                   neu_bhv="do_agree", neu=f"어려울 수 있어~", 
                                   act_bhv="do_question_S", act=f"다영이도 물건을 물 속에 빠뜨린 적 있니?")

        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"다영이도 물건을 물 속에 빠뜨린 적 있니?", 
                                       pos_bhv="do_sad", pos=f"정말 속상했을 것 같아", 
                                       neu_bhv="do_agree", neu=f"괜찮아~ 생각나지 않을 수 있어~", 
                                       act_bhv="do_sad", act=f"정말 속상했을 것 같아")

        cm.tts(bhv="question_S", string=f"연못에는 도끼말고 어떤 물건들이 빠져있었을지 상상해볼까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"연못에는 도끼말고 어떤 물건들이 빠져있었을지 상상해볼까?", 
                                   neu_bhv="do_agree", neu=f"괜찮아~ 생각나지 않을 수 있어~")

        cm.tts(bhv="question_S", string=f"나무꾼은 금 도끼로 뭘 했을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"나무꾼은 금 도끼로 뭘 했을까?")
        

        # 2. 등장인물 공감 대화
        cm.tts(bhv="question_S", string=f"욕심쟁이 친구가 황금도끼를 얻으려고 거짓말을 했을 때 헤르메스 신은 화가 났을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"욕심쟁이 친구가 황금도끼를 얻으려고 거짓말을 했을 때 헤르메스 신은화가 났을까?", 
                                   pos_bhv="do_question_S", pos=f"다영이도 누군가 거짓말을 해서 화가 난 적이 있니?", 
                                   neu_bhv="do_agree", neu=f"몰라도 괜찮아~", 
                                   act_bhv="do_question_S", act=f"다영이도 누군가 거짓말을 해서 화가 난 적이 있니?")
        
        if answer[0] == "positive":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"다영이도 누군가 거짓말을 해서 화가 난 적이 있니?", 
                                       pos_bhv="do_agree", pos=f"헤르메스 신이랑 비슷한 기분을 느꼈겠다!")
        
        cm.tts(bhv="question_L", string=f"헤르메스 신이 나무꾼에게 세 가지 도끼를 상으로 주었을 때 나무꾼은 기뻤을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"헤르메스 신이 나무꾼에게 세 가지 도끼를 상으로 주었을 때 나무꾼은 기뻤을까?", 
                                   pos_bhv="do_question_S", pos=f"다영이도 최근에 상을 받고 기뻤던 적이 있으면 이야기 해줄래?", 
                                   act_bhv="do_question_S", act=f"다영이도 최근에 상을 받고 기뻤던 적이 있으면 이야기 해줄래?") 
        
        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"다영이도 최근에 상을 받고 기뻤던 적이 있으면 이야기해줄래?", 
                                       pos_bhv="do_agree", pos=f"그런 일이 있었구나! 정말 기분 좋았겠다~!", 
                                       act_bhv="do_agree", act=f"그런 일이 있었구나! 정말 기분 좋았겠다~!")
            
        # 3. 마무리 대화    
        cm.tts(bhv="do_question_L", string=f"만약 {wm.word(self.user_name, 0)}가 착한 나무꾼을 만난다면 뭐라고 해줄 수 있을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", string=f"만약 동화 속 착한 나무꾼을 만난다면 뭐라고 해줄 수 있을까?",  
                                   pos_bhv="do_agree", pos=f"그렇구나!",
                                   neu_bhv="do_agree", neu=f"괜찮아~ 모를 수 있지~ ",
                                   neg_bhv="do_agree", neg=f"그렇구나!",
                                   act_bhv="do_agree", act=f"그렇구나!")
        
        cm.tts(bhv="do_explain_C", string=f"오늘 동화 재미있었지? 다음에 또 재미있는 동화를 들려줄게~")
        
        
        
        
if __name__ == "__main__":    
    
    fat = Fairytale()
    fat.Hermes()
