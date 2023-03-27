# -*- coding: utf-8 -*-

# 사회기술-가위나 칼은 손잡이가 있는 쪽으로 물건을 줘요

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


class Etiquette():    
    
    def __init__(self): 
        self.user_name = '가영'
        self.correct = ['밤', '늦']
        self.ox = ''
                
        
    def Friend4(self):
        
        # 2.1 카드 대화
        cm.tts(bhv="do_question_L", string="이 카드의 어린이는 무엇을 잘못했을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="이 카드의 어린이는 무엇을 잘못했을까?",
                                   neg_bhv="do_suggestion_S", neg="같이 다시 한번 볼까?",
                                   neu_bhv="do_suggestion_S", neu="같이 다시 한번 볼까?")             
        
        if answer[0][0] == "action":            
            
            for i in range(len(self.correct)):
                if self.correct[i] in answer[1]:
                    self.ox = "(right)"                    
            if len(self.ox) == 0:
                self.ox = "(wrong ㅠㅠ)"
              
            if self.ox == "(right)":
                print(self.ox)
                cm.tts(bhv="do_compliment_S", string="맞아! 아주 똑똑한 걸?")
            else:
                print(self.ox)
                cm.tts(bhv="do_suggestion_S", string="또 무엇을 잘못했을까?")
                answer = cm.responses_proc(re_bhv="do_suggestion_S", re_q="또 무엇을 잘못했을까?")
                
                if answer[0][0] == "action":        
                                
                    for i in range(len(self.correct)):
                        if self.correct[i] in answer[1]:
                            self.ox = "(right)"                    
                    if len(self.ox) == 0:
                        self.ox = "(wrong ㅠㅠ)"
                    
                    if self.ox == "(right)":
                        print(self.ox)
                        cm.tts(bhv="do_compliment_S", string="맞아! 아주 똑똑한 걸?")
                    else:
                        print(self.ox)
                        cm.tts(bhv="do_suggestion_S", string="같이 다시 한번 볼까?")
        
        cm.tts(bhv="do_explain_A", string="이 카드의 어린이는 밤 늦도록 친구의 집에서 놀고 있어.")
     
        # 2.2 경험 질문
        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}는 친구 집에서 놀았던 적이 있니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}는 친구 집에서 놀았던 적이 있니?",
                                   pos_bhv="do_question_S", pos="누구의 집이었니?")
        
        if answer[0][0] == "positive":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q="누구의 집이었니?",
                                       act_bhv="do_question_S", act="무엇을 하고 놀았니?")
            
            answer = cm.responses_proc(re_bhv="do_question_S", re_q="무엇을 하고 놀았니?",
                                       neu_bhv="do_agree", neu="기억이 안 날 수 있지~")
            
            cm.tts(bhv="do_question_L", string="친구 집에서 늦게 까지 놀면 집에서 엄마가 기다리시겠지?")
            answer = cm.responses_proc(re_bhv="do_question_L", re_q="친구 집에서 늦게 까지 놀면 집에서 엄마가 기다리시겠지?")
        
        # 2.3 문제 인식
        cm.tts(bhv="do_question_L", string="친구네 집에서 밤 늦게 까지 놀면 친구네 가족들은 어떤 기분이 들까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="친구네 집에서 밤 늦게 까지 놀면 친구네 가족들은 어떤 기분이 들까?",
                                   pos_bhv="do_explain_C", pos=f"잠을 자야 하는데 {wm.word(self.user_name, 0)}가 있어서 불편하다고 느낄 수 있어!",
                                   neu_bhv="do_explain_C", neu=f"괜찮아. 모를 수도 있어~ 잠을 자야 하는데 {wm.word(self.user_name, 0)}가 있어서 불편하다고 느낄 수 있어!",
                                   act_bhv="do_explain_C", act=f"잠을 자야 하는데 {wm.word(self.user_name, 0)}가 있어서 불편하다고 느낄 수 있어!")
    
        # 3.1 마무리 대화
        cm.tts(bhv="do_joy_A", string=f"친구네 집에서는 밤 늦게 까지 놀면 안 돼~ 다음에 다시 만나서 또 놀면 되니까 일찍 집에 가도록 하자!")
    
        
        
        
if __name__ == "__main__":
    
    etq = Etiquette()
    etq.Friend4()