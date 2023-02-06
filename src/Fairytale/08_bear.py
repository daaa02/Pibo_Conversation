# -*- coding: utf-8 -*-

# 동화-곰과 두 여행자

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
                
        
    def Bear(self):
        
        # 1. 동화 줄거리 대화
        cm.tts(bhv="do_joy_A", string=f"정말 재미있는 이야기였어! {wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?")
        answer = cm.responses_proc(re_bhv="do_joy_A", re_q=f"{wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?",
                                   neu_bhv="do_agree", neu=f"그럴 수 있지~")

        cm.tts(bhv="do_question_S", string=f"두 여행자는 어디를 여행하는 중이었을것 같니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"두 여행자는 어디를 여행하는 중이었을것 같니?", 
                                   pos_bhv="do_question_S", pos=f"여행지에서 무엇을 했을까?", 
                                   act_bhv="do_question_S", act=f"여행지에서 무엇을 했을까?")

        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", string=f"여행지에서 무엇을 했을까?", 
                                       pos_bhv="do_agree", pos=f"그렇게 생각하는구나!", 
                                       neu_bhv="do_agree", neu=f"모를 수 있지~", 
                                       act_bhv="do_agree", act=f"그렇게 생각하는구나!")

        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}도 최근에 가족들이랑 여행 간 적이 있다면 이야기해줄래?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}도 최근에 가족들이랑 여행 간 적이 있다면 이야기해줄래?", 
                                   pos_bhv="do_question_L", pos=f"{wm.word(self.user_name, 0)}가 너무 좋았을 것 같아! 그 여행은 어땠어?", 
                                   act_bhv="do_question_L", act=f"{wm.word(self.user_name, 0)}가 너무 좋았을 것 같아! 그 여행은 어땠어?") 

        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", strre_qing=f"그 여행은 어땠어?", 
                                       pos_bhv="do_agree", pos=f"그랬구나!", 
                                       neu_bhv="do_agree", neu=f"괜찮아~ 모를 수 있지~", 
                                       act_bhv="do_agree", act=f"그랬구나!")

        cm.tts(bhv="do_question_L", string=f"여행자들처럼 실제로 곰을 본다면 {wm.word(self.user_name, 0)}는 어떻게 할 것 같니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"여행자들처럼 실제로 곰을 본다면 {wm.word(self.user_name, 0)}는 어떻게 할 것 같니?")
                
        # 2. 등장인물 공감 대화
        cm.tts(bhv="do_question_S", string=f"두 여행자가 곰을 만났을 때 놀라고 두려웠을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"두 여행자가 곰을 만났을 때 놀라고 두려웠을까?", 
                                   pos_bhv="do_question_L", pos=f"{wm.word(self.user_name, 0)}는 최근에 놀라고 두려웠던 적이 있니?", 
                                   act_bhv="do_question_L", act=f"{wm.word(self.user_name, 0)}는 최근에 놀라고 두려웠던 적이 있니?")

        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}는 최근에 놀라고 두려웠던 적이 있니?", 
                                       pos_bhv="do_agree", pos=f"그랬구나! 정말 무서웠겠다!", 
                                       act_bhv="do_agree", act=f"그랬구나! 정말 무서웠겠다!")

        cm.tts(bhv="do_question_L", string=f"곰을 만나 자신을 버려두고 도망가는 걸 본 친구의 마음은 속상했을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"곰을 만나 자신을 버려두고 도망가는 걸 본 친구의 마음은 속상했을까?", 
                                   pos_bhv="do_question_L", pos=f"{wm.word(self.user_name, 0)}도 속상했던 적이 있다면 이야기해 줄래?", 
                                   neu_bhv="do_agree", neu=f"몰라도 괜찮아~", 
                                   act_bhv="do_question_L", act=f"{wm.word(self.user_name, 0)}도 속상했던 적이 있다면 이야기해 줄래?")

        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}도 속상했던 적이 있다면 이야기해 줄래?", 
                                       pos_bhv="do_agree", pos=f"그런 일이 있었구나!", 
                                       act_bhv="do_agree", act=f"그런 일이 있었구나!")

        # 3. 마무리 대화
        cm.tts(bhv="do_question_L", string=f"만약 {wm.word(self.user_name, 0)}가 도망간 친구를 만난다면 뭐라고 해줄 수 있을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", string=f"만약 {wm.word(self.user_name, 0)}가 도망간 친구를 만난다면 뭐라고 해줄 수 있을까?",  
                                   pos_bhv="do_agree", pos=f"그렇구나!",
                                   neu_bhv="do_agree", neu=f"괜찮아~ 모를 수 있지~",
                                   neg_bhv="do_agree", neg=f"그렇구나!",
                                   act_bhv="do_agree", act=f"그렇구나!")
        
        cm.tts(bhv="do_explain_C", string=f"다음에 또 재미있는 동화를 들려줄게~")
            
        


if __name__ == "__main__":    
    
    fat = Fairytale()
    fat.Bear()