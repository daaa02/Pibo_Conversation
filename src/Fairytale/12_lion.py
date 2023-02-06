# -*- coding: utf-8 -*-

# 동화-사자와 양치기

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
        self.user_name = '다영'
                
        
    def Lion(self):
        
        # 1. 동화 줄거리 대화        
        cm.tts(bhv="do_joy_A", string=f"정말 재미있는 이야기였어! {wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?")
        answer = cm.responses_proc(re_bhv="do_joy_A", re_q=f"{wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?",
                                   neu_bhv="do_agree", neu=f"그럴 수 있지~")
        

        # 2. 등장인물 공감 대화
        

        # 3. 마무리 대화
        cm.tts(bhv="do_question_L", string=f"만약 {wm.word(self.user_name, 0)}가 동화 속 독수리를 만난다면 어떤 선물을 주고 싶니?")
        answer = cm.responses_proc(re_bhv="do_question_L", string=f"만약 {wm.word(self.user_name, 0)}가 동화 속 독수리를 만난다면 어떤 선물을 주고 싶니?",  
                                   pos_bhv="do_agree", pos=f"그렇구나!",
                                   neu_bhv="do_agree", neu=f"괜찮아~ 대답하기 어려울 수 있어~ ",
                                   neg_bhv="do_agree", neg=f"그렇구나!",
                                   act_bhv="do_agree", act=f"그렇구나!")
        
        cm.tts(bhv="do_explain_C", string=f"오늘 동화 재미있었지? 다음에 또 재미있는 동화를 들려줄게~")
            
        


if __name__ == "__main__":    
    
    fat = Fairytale()
    fat.Lion()