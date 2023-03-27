# -*- coding: utf-8 -*-

# 동화-늑대와 여우

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
        
        
    def Wolf(self):
        
        # 1. 동화 줄거리 대화
        cm.tts(bhv="do_joy_A", string=f"정말 재미있는 이야기였어! {wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?")
        answer = cm.responses_proc(re_bhv="do_joy_A", re_q=f"{wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?",
                                   neu_bhv="do_agree", neu=f"그럴 수 있지~")

        cm.tts(bhv="do_question_S", string=f"는 여우나 늑대를 본 적이 있다면 말해 줄래?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"는 여우나 늑대를 본 적이 있다면 말해 줄래?", 
                                   pos_bhv="do_question_S", pos=f"봤을 때 {wm.word(self.user_name, 0)}가 놀라진 않았니?", 
                                   act_bhv="do_question_S", act=f"봤을 때 {wm.word(self.user_name, 0)}가 놀라진 않았니?")

        if answer[0][0] == "positive" or answer[0][0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"봤을 때 {wm.word(self.user_name, 0)}가 놀라진 않았니?", 
                                       neu_bhv="do_agree", neu=f"괜찮아~ 모를 수 있지~")

        cm.tts(bhv="do_question_S", string=f"늑대가 가장 좋아할 것 같은 음식을 상상해볼까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"늑대가 가장 좋아할 것 같은 음식을 상상해볼까?", 
                                   pos_bhv="do_question_S", pos=f"{wm.word(self.user_name, 0)}는 어떤 음식을 좋아하니?", 
                                   act_bhv="do_question_S", act=f"{wm.word(self.user_name, 0)}는 어떤 음식을 좋아하니?")

        if answer[0][0] == "positive" or answer[0][0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}는 어떤 음식을 좋아하니?", 
                                       pos_bhv="do_agree", pos=f"그 음식을 좋아하는구나!", 
                                       neu_bhv="do_agree", neu=f"몰라도 괜찮아~", 
                                       act_bhv="do_agree", act=f"그 음식을 좋아하는구나!")

        cm.tts(bhv="do_question_S", string=f"음식을 마음껏 먹은 늑대는 얼마나 뚱뚱해졌을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", string=f"음식을 마음껏 먹은 늑대는 얼마나 뚱뚱해졌을까?")


        # 2. 등장인물 공감 대화
        cm.tts(bhv="do_question_S", string=f"늑대가 여우를 잡아 먹는다고 했을 때 여우는 무서웠을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"늑대가 여우를 잡아 먹는다고 했을 때 여우는 무서웠을까?", 
                                   pos_bhv="do_question_L", pos=f"{wm.word(self.user_name, 0)}는 최근에 무서웠던 적이 있다면 말해 줄래?", 
                                   act_bhv="do_question_L", act=f"{wm.word(self.user_name, 0)}는 최근에 무서웠던 적이 있다면 말해 줄래?")

        if answer[0][0] == "positive" or answer[0][0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}는 최근에 무서웠던 적이 있다면 말해 줄래?", 
                                       pos_bhv="do_agree", pos=f"그랬구나! 정말 무서웠겠다", 
                                       act_bhv="do_agree", act=f"그랬구나! 정말 무서웠겠다")

        cm.tts(bhv="do_question_S", string=f"여우가 늑대에게 무사히 도망갔을 때 마음이 편안해졌을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"여우가 늑대에게 무사히 도망갔을 때 마음이 편안해졌을까?", 
                                   pos_bhv="do_question_S", pos=f"{wm.word(self.user_name, 0)}도 편안한 기분을 느낀적이 있다면 말해 줄래?", 
                                   act_bhv="do_question_S", act=f"{wm.word(self.user_name, 0)}도 편안한 기분을 느낀적이 있다면 말해 줄래?")

        if answer[0][0] == "positive" or answer[0][0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}도 편안한 기분을 느낀적이 있다면 말해 줄래?", 
                                       pos_bhv="do_agree", pos=f"그런 일이 있었구나!", 
                                       act_bhv="do_agree", act=f"그런 일이 있었구나!")

        # 3. 마무리 대화
        cm.tts(bhv="do_question_L", string=f"만약 {wm.word(self.user_name, 0)}가 음식을 아주 많이 먹은 늑대를 만난다면 뭐라고 해줄 수 있을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"만약 {wm.word(self.user_name, 0)}가 음식을 아주 많이 먹은 늑대를 만난다면 뭐라고 해줄 수 있을까?", 
                                   pos_bhv="do_agree", pos=f"그렇구나!", 
                                   neu_bhv="do_agree", neu=f"괜찮아~ 모를 수 있지~", 
                                   neg_bhv="do_agree", neg=f"그렇구나!", 
                                   act_bhv="do_agree", act=f"그렇구나!")
        
        cm.tts(bhv="do_explain_C", string=f"오늘 동화 재미있었지? 다음에 또 재미있는 동화 들려줄게~")
            
        


if __name__ == "__main__":    
    
    fat = Fairytale()
    fat.Wolf()