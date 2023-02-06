# -*- coding: utf-8 -*-

# 동화-농부와 독수리

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
                
        
    def Farmer(self):
        
        # 1. 동화 줄거리 대화        
        cm.tts(bhv="do_joy_A", string=f"정말 재미있는 이야기였어! {wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?")
        answer = cm.responses_proc(re_bhv="do_joy_A", re_q=f"{wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?",
                                   neu_bhv="do_agree", neu=f"그럴 수 있지~")
        
        cm.tts(bhv="do_question_S", string=f"OO이는 독수리를 본 적이 있다면 말해 줄래?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}는 독수리를 본 적이 있다면 말해 줄래?", 
                                   pos_bhv="do_question_S", pos=f"멋지다! 얼마나 큰 독수리 였어?", 
                                   neu_bhv="do_agree", neu=f"괜찮아~ 생각나지 않을 수 있어~", 
                                   act_bhv="do_question_S", act=f"멋지다! 얼마나 큰 독수리 였어?")

        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"얼마나 큰 독수리 였어?", 
                                       neu_bhv="do_agree", neu=f"모를 수 있지~")

        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}가 독수리가 되어 날 수 있다면 어디로 가보고 싶니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}가 독수리가 되어 날 수 있다면 어디로 가보고 싶니?", 
                                   neu=f"괜찮아~ 대답하기 어려울 수 있어~")

        cm.tts(bhv="do_question_S", string=f"농부는 어떤 동물을 잡으려고 덫을 놓았을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"농부는 어떤 동물을 잡으려고 덫을 놓았을까?")

        # 2. 등장인물 공감 대화
        cm.tts(bhv="do_question_L", string=f"독수리가 갑자기 모자를 가져갔을 때 농부는 당황했을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", string=f"독수리가 갑자기 모자를 가져갔을 때 농부는 당황했을까?",
                                   pos_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}도 누군가 갑자기 {wm.word(self.user_name, 0)}의 물건을 가져가서 당황한 적이 있니?",
                                   neu_bhv="do_agree", neu="몰라도 괜찮아~",
                                   act_bhv="do_question_L", act=f"{wm.word(self.user_name, 0)}도 누군가 갑자기 {wm.word(self.user_name, 0)}의 물건을 가져가서 당황한 적이 있니?")
        
        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}도 누군가 갑자기 {wm.word(self.user_name, 0)}의 물건을 가져가서 당황한 적이 있니?", 
                                       pos_bhv="do_agree", pos=f"그랬구나! ", 
                                       act_bhv="do_agree", act=f"그랬구나! ")
        
        cm.tts(bhv="do_question_L", string=f"독수리가 농부를 구해준 것을 알았을 때 농부의 기분은 고마웠을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"독수리가 농부를 구해준 것을 알았을 때 농부의 기분은 고마웠을까?", 
                                   pos_bhv="do_question_L", pos=f"OO이도 고마운 기분을 느낀적이 있다면 이야기해 줄래?",
                                   act_bhv="do_question_L", act=f"OO이도 고마운 기분을 느낀적이 있다면 이야기해 줄래?")
        
        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"OO이도 고마운 기분을 느낀적이 있다면 이야기해 줄래?", 
                                       act_bhv="do_agree", act=f"그런 일이 있었구나!")

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
    fat.Famer()