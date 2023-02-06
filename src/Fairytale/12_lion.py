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
        self.user_name = '가영'
                
        
    def Lion(self):
        
        # 1. 동화 줄거리 대화        
        cm.tts(bhv="do_joy_A", string=f"정말 재미있는 이야기였어! {wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?")
        answer = cm.responses_proc(re_bhv="do_joy_A", re_q=f"{wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?",
                                   neu_bhv="do_agree", neu=f"그럴 수 있지~")

        cm.tts(bhv="question_S", string=f"{wm.word(self.user_name, 0)}는 사자를 본 적이 있니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}는 사자를 본 적이 있니?", 
                                   pos_bhv="do_question_S", pos=f"어디서 봤어?", 
                                   neu_bhv="do_agree", neu=f"모를 수 있지~", 
                                   act_bhv="do_question_S", act=f"어디서 봤어?")
        
        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"어디서 봤어?", 
                                       neu_bhv="do_agree", neu=f"괜찮아~ 생각 나지 않을 수 있어~")
        
        cm.tts(bhv="question_S", string=f"세상에서 가장 힘 센 동물은 뭐라고 생각해?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"세상에서 가장 힘 센 동물은 뭐라고 생각해?", 
                                   pos_bhv="do_question_S", pos=f"그 동물이라고 생각한 이유는 뭐니?", 
                                   neu_bhv="do_agree", neu=f"모를 수 있지~", 
                                   act_bhv="do_question_S", act=f"그 동물이라고 생각한 이유는 뭐니?")
        
        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"그 동물이라고 생각한 이유는 뭐니?", 
                                       pos_bhv="do_agree", pos=f"그렇게 생각하는구나!",
                                       act_bhv="do_agree", act=f"그렇게 생각하는구나!")
        
        cm.tts(bhv="question_L", string=f"동화 속 양치기가 가시에 찔린 사자를 도와주지 않았다면 사자는 어떻게 됐을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"동화 속 양치기가 가시에 찔린 사자를 도와주지 않았다면 사자는 어떻게 됐을까?", 
                                   neu_bhv="do_agree", neu=f"괜찮아~ 모를 수 있지~")
            
        # 2. 등장인물 공감 대화
        cm.tts(bhv="question_S", string=f"가시에 찔렸을 때 사자는 매우 아팠겠지?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"가시에 찔렸을 때 사자는 매우 아팠겠지?", 
                                   pos_bhv="do_question_L", pos=f"{wm.word(self.user_name, 0)}도 최근에 다친 적 있다면 말해줄래?", 
                                   act_bhv="do_question_L", act=f"{wm.word(self.user_name, 0)}도 최근에 다친 적 있다면 말해줄래?")
        
        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}도 최근에 다친 적 있다면 말해줄래?",
                                       act_bhv="do_sad", act=f"그랬구나! 정말 아팠겠다!")
            
        cm.tts(bhv="question_L", string=f"사자가 은혜를 갚으려고 도움을 주었을 때 양치기는 정말 고마웠겠지?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"사자가 은혜를 갚으려고 도움을 주었을 때 양치기는 정말 고마웠겠지?", 
                                   pos_bhv="do_question_S", pos=f"{wm.word(self.user_name, 0)}도 도움을 받고 기뻤던 적이 있다면 이야기 해줄래?", 
                                   neu_bhv="do_agree", neu=f"괜찮아~ 대답하기 어려울 수 있어~", 
                                   act_bhv="do_question_S", act=f"{wm.word(self.user_name, 0)}도 도움을 받고 기뻤던 적이 있다면 이야기 해줄래?")
        
        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}도 도움을 받고 기뻤던 적이 있다면 이야기 해줄래?", 
                                       pos_bhv="do_agree", pos=f"그런 일이 있었구나! 정말 기분이 좋았겠다~!", 
                                       act_bhv="do_agree", act=f"그런 일이 있었구나! 정말 기분이 좋았겠다~!")
            
        # 3. 마무리 대화
        cm.tts(bhv="do_question_L", string=f"만약 {wm.word(self.user_name, 0)}가 동화 속 은혜 갚은 사자를 만난다면 어떤 선물을 주고 싶니?")
        answer = cm.responses_proc(re_bhv="do_question_L", string=f"만약 동화 속 은혜 갚은 사자를 만난다면 어떤 선물을 주고 싶니?",  
                                   pos_bhv="do_agree", pos=f"그렇구나!",
                                   neu_bhv="do_agree", neu=f"괜찮아~ 모를 수 있지~ ",
                                   neg_bhv="do_agree", neg=f"그렇구나!",
                                   act_bhv="do_agree", act=f"그렇구나!")
        
        cm.tts(bhv="do_explain_C", string=f"오늘 동화 재미있었지? 다음에 또 재미있는 동화를 들려줄게~")
            
        


if __name__ == "__main__":    
    
    fat = Fairytale()
    fat.Lion()