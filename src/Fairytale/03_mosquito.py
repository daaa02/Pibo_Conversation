# -*- coding: utf-8 -*-

# 동화-모기와 사자

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
                

class FairyTale():
        
    def __init__(self): 
        self.user_name = '다영'
        
    
    def Mosqutio(self):      
        # 1. 동화 줄거리 대화  
        cm.tts(bhv="do_joy_A", string=f"정말 재미있는 이야기였어! {wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?")
        answer = cm.responses_proc(re_bhv="do_joy_A", re_q=f"{wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?",
                                   neu_bhv="do_agree", neu=f"그럴 수 있지~")
        
        # 2. 등장인물 공감 대화        
        cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}는 언제 모기에 물렸었니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}는 언제 모기에 물렸었니?", 
                                   neu_bhv="do_agree", neu=f"모를 수 있지~")
        
        cm.tts(bhv="do_question_S", string=f"모기한테 물린 사자 얼굴은 어떻게 변했을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"모기한테 물린 사자 얼굴은 어떻게 변했을까?", 
                                   neu_bhv="do_agree", neu=f"몰라도 괜찮아~")
        
        cm.tts(bhv="do_question_S", string=f"만약 사자가 거미줄에 걸린 모기를 본다면 구해줄까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"만약 사자가 거미줄에 걸린 모기를 본다면 구해줄까?", 
                                   pos_bhv="do_agree", pos=f"사자는 그럴 수 있겠구나~.",
                                   neg_bhv="do_agree", neg=f"사자는 그럴 수 있겠구나~.",
                                   act_bhv="do_agree", act=f"사자는 그럴 수 있겠구나~.")
            
        cm.tts(bhv="do_question_L", string=f"거미줄에 걸린 모기는 움직일 수 없었을 때 무서웠을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"거미줄에 걸린 모기는 움직일 수 없었을 때 무서웠을까?", 
                                   pos_bhv="do_question_L", pos=f"최근에 무섭다고 느낀 일이 있다면 말해줄래?")
        
        if answer[0] == "positive": 
            answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"최근에 무섭 느낀 일이 있다면 말해줄래?", 
                                       pos_bhv="do_agree", pos=f"정말 무서웠겠는걸?", 
                                       act_bhv="do_agree", act=f"정말 무서웠겠는걸?")
            
        cm.tts(bhv="do_question_S", string=f"모기가 큰 사자랑 싸워서 이겼을 때는 기뻤을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"모기가 큰 사자랑 싸워서 이겼을 때는 기뻤을까?", 
                                   pos_bhv="do_question_L", pos=f"최근에 놀이에서 이겨 기뻤던 적이 있으면 이야기해 줄래?")
        
        if answer[0] == "positive": 
            answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"최근에 놀이에서 이겨 기뻤던 적이 있으면 이야기해 줄래?", 
                                       pos_bhv="do_agree", pos=f"그런 일이 있었구나!", 
                                       act_bhv="do_agree", act=f"그런 일이 있었구나!")

        # 3. 마무리 대화
        cm.tts(bhv="do_suggestion_L", string=f"만약 {wm.word(self.user_name, 0)}가 자신만만한 모기를 만난다면 뭐라고 해줄 수 있을까?")
        answer = cm.responses_proc(re_bhv="do_suggestion_L", re_q=f"{wm.word(self.user_name, 0)}가 자신만만한 모기를 만난다면 뭐라고 해줄 수 있을까?", 
                                   pos_bhv="do_agree", pos=f"{wm.word(self.user_name, 0)}는 그렇게 말해주고 싶구나!", 
                                   neu_bhv="do_agree", neu=f"괜찮아~ 모를 수 있지~", 
                                   act_bhv="do_agree", act=f"{wm.word(self.user_name, 0)}는 그렇게 말해주고 싶구나!")
        
        cm.tts(bhv="do_explain_C", string=f"다음에 또 재미있는 동화 들려줄게~")
            

if __name__ == "__main__":
    fat = FairyTale()
    fat.Mosqutio()
