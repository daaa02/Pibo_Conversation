# -*- coding: utf-8 -*-

# 사회기술-길을 걸으면서 뛰거나 장난치지 않아요

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
        self.correct = ['뛰', '장난']
        self.ox = ''
                
        
    def Street(self):
        
        # 2.1 카드 대화
        cm.tts(bhv="do_question_L", string="이 카드의 어린이는 무엇을 잘못했을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="이 카드의 어린이는 무엇을 잘못했을까?",
                                   neg_bhv="do_suggestion_S", neg="같이 다시 한번 볼까?",
                                   neu_bhv="do_suggestion_S", neu="같이 다시 한번 볼까?")             
        
        if answer[0] == "action":            
            
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
                
                if answer[0] == "action":        
                                
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
        
        cm.tts(bhv="do_explain_A", string="이 카드의 어린이는 길에서 뛰어 다니고 장난을 쳤어.")
     
        # 2.2 경험 질문
        cm.tts(bhv="do_question_S", string="길거리에서 뛰어다니는 사람을 본 적이 있니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="길거리에서 뛰어다니는 사람을 본 적이 있니?",
                                   pos_bhv="do_agree", pos="본 적이 있구나!",
                                   neu_bhv="do_agree", neu="괜찮아. 기억이 안 날 수도 있어~")

        cm.tts(bhv="do_question_L", string="길에서 뛰어 다니면 어떤 위험한 일이 일어날까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="길에서 뛰어 다니면 어떤 위험한 일이 일어날까?",
                                   pos_bhv="do_agree", pos="뛰어다니다 부딪히면 넘어질 수도 있겠지?",
                                   neu_bhv="do_explain_C", neu="괜찮아 모를 수도 있어~뛰어다니다 부딪히면 넘어질 수도 있겠지?",
                                   act_bhv="do_agree", act="뛰어다니다 부딪히면 넘어질 수도 있겠지?")
            
        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}도 길에서 넘어진 적이 있니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}도 길에서 넘어진 적이 있니?",
                                   pos_bhv="do_sad", pos="너무 아팠겠다.",
                                   neu_bhv="do_agree", neu="괜찮아. 기억이 안 날 수도 있어~")

        # 2.3 문제 인식
        cm.tts(bhv="do_question_L", string="길에서 뛰어다니면 다른 사람들이 어떻게 느낄까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="길에서 뛰어다니면 다른 사람들이 어떻게 느낄까?",
                                   pos_bhv="do_agree", pos="부딪힐까봐 겁이 날 수도 있겠지?",
                                   neu_bhv="do_explain_A", neu="괜찮아 모를 수도 있어~ 부딪힐까봐 겁이 날 수도 있겠지?",
                                   act_bhv="do_agree", act="부딪힐까봐 겁이 날 수도 있겠지?")
    
        # 3.1 마무리 대화
        cm.tts(bhv="do_joy_A", string="길에서는 앞을 보고 안전하게 걷는 것이 좋아. 잘 기억해 두자!")
    
        
        
        
if __name__ == "__main__":
    
    etq = Etiquette()
    etq.Street()