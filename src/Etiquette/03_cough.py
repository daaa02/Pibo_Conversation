# -*- coding: utf-8 -*-

# 사회기술-입을 가리고 기침을 해요

import os, sys
import re
import random

sys.path.append('/home/kiro/workspace/Conversation_Scenarios/')
# sys.path.append('/home/pi/Pibo_Conversation/')
from data.conversation_manage import ConversationManage, WordManage
from data.speech_to_text import speech_to_text
from data.text_to_speech import TextToSpeech, text_to_speech

cm = ConversationManage()
wm = WordManage()
audio = TextToSpeech()


class Etiquette():    
    
    def __init__(self): 
        self.user_name = '다영'
        self.correct = ['기침', '재채기']
        self.ox = ''
                
        
    def Cough(self):
        
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
        
        cm.tts(bhv="do_explain_A", string="이 카드의 어린이는 입을 가리지 않고 기침을 했어.")
     
        # 2.2 경험 질문
        cm.tts(bhv="do_question_L", string="우리는 보통 언제 기침을 할까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="우리는 보통 언제 기침을 할까?",
                                   pos_bhv="do_agree", pos="감기에 걸리면 기침을 하지?",
                                   neu_bhv="do_explain_B", neu="괜찮아 생각이 안 날 수도 있어~ 감기에 걸리면 기침을 하지? ",
                                   act_bhv="do_agree", act="감기에 걸리면 기침을 하지?")

        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}는 밖에서 기침이 나올 때 어떻게 하니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}는 밖에서 기침이 나올 때 어떻게 하니?",
                                   neu_bhv="do_explain_C", neu="괜찮아 모를 수도 있어~")

        cm.tts(bhv="do_question_L", string="입을 가리지 않고 기침을 하면 어떤 일이 일어날까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="입을 가리지 않고 기침을 하면 어떤 일이 일어날까?",
                                   pos_bhv="do_agree", pos="다른 사람도 감기에 걸릴 수 있겠지?",
                                   neu_bhv="do_explain_B", neu="괜찮아 모를 수도 있어~ 다른 사람도 감기에 걸릴 수 있을거야.",
                                   act_bhv="do_agree", act="다른 사람도 감기에 걸릴 수 있겠지?")
            
        # 2.3 문제 인식
        cm.tts(bhv="do_question_L", string="입을 가리지 않고 기침을 하면 다른 사람들이 어떻게 생각할까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="입을 가리지 않고 기침을 하면 다른 사람들이 어떻게 생각할까?",
                                   pos_bhv="do_agree", pos="다른 사람들은 침이 튀어서 깨끗하지 못하다고 생각하겠지?",
                                   neu_bhv="do_explain_A", neu="괜찮아 모를 수도 있어~ 아마 다른 사람들은 침이 튀어서 깨끗하지 않다고 생각할거야.",
                                   act_bhv="do_agree", act="다른 사람들은 침이 튀어서 깨끗하지 못하다고 생각하겠지?")
        
        # 3.1 마무리 대화
        cm.tts(bhv="do_joy_A", string="기침을 할 때 입을 가리는 건 중요한 공공예절이야. 잘 기억해 두자!")
                            
        
        
        
if __name__ == "__main__":
    
    etq = Etiquette()
    etq.Cough()