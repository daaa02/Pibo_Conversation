# -*- coding: utf-8 -*-

# 사회기술-차례대로 순서를 지켜요

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
        self.correct = ['차례', '순서', '줄', '새치기']
        self.ox = ''
                
        
    def Sequence(self):
        
        # 2.1 카드 대화
        cm.tts(bhv="do_question_L", string="이 카드의 어린이는 무엇을 잘못했을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="이 카드의 어린이는 무엇을 잘못했을까?",
                                   neg_bhv="do_suggestion_S", neg="같이 다시 한번 볼까?",
                                   neu_bhv="do_suggestion_S", neu="같이 다시 한번 볼까?")             
        
        if answer[0] == "action":            
            
            for i in range(len(self.correct)):
                if self.correct[i] in answer[1]:
                    self.ox = "right"                    
            if len(self.ox) == 0:
                self.ox = "wrong ㅠㅠ"
              
            if self.ox == "right":
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
        
        cm.tts(bhv="do_explain_A", string="이 카드의 어린이는 차례를 지키지 않았어.")
     
        # 2.2 경험 질문
        cm.tts(bhv="do_question_L", string="우리는 어떤 상황에서 차례를 지켜야 할까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="우리는 어떤 상황에서 차례를 지켜야 할까?",
                                   pos_bhv="do_agree", pos="화장실을 가기 위해 줄을 설 때도 차례를 지켜야 하지?",
                                   neu_bhv="do_explain_B", neu="괜찮아 생각이 안 날 수도 있어~ 화장실을 가기 위해 줄을 설 때도 차례를 지켜야 하지?",
                                   act_bhv="do_agree", act="화장실을 가기 위해 줄을 설 때도 차례를 지켜야 하지?")

        cm.tts(bhv="do_question_L", string="사람들이 모두 차례를 지키지 않으면 어떤 일이 일어날까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="사람들이 모두 차례를 지키지 않으면 어떤 일이 일어날까?",
                                   pos_bhv="do_agree", pos="모두가 차례를 지키지 않으면 사고가 발생할 수도 있고 모두 다 더 오래 기다려야 할 수도 있겠지?",
                                   neu_bhv="do_explain_C", neu="괜찮아 모를 수도 있어~ 모두가 차례를 지키지 않으면 사고가 발생할 수도 있고 모두 다 더 오래 기다려야 할 수도 있겠지?",
                                   act_bhv="do_agree", act="모두가 차례를 지키지 않으면 사고가 발생할 수도 있고 모두 다 더 오래 기다려야 할 수도 있겠지?")

        cm.tts(bhv="do_question_L", string="차례를 지키지 않는 사람을 본 적이 있니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="차례를 지키지 않는 사람을 본 적이 있니?",
                                   pos_bhv="do_agree", pos="본 적이 있구나!",
                                   neu_bhv="do_agree", neu="괜찮아. 기억이 안 날 수도 있어~")
        
        # 2.3 문제 인식
        cm.tts(bhv="do_question_L", string="차례를 지키지 않으면 다른 사람들이 어떻게 느낄까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="차례를 지키지 않으면 다른 사람들이 어떻게 느낄까?",
                                   neu_bhv="do_explain_B", neu="괜찮아 모를 수도 있어~ 다른 사람들은 화가 날 수도 있겠지?",
                                   act_bhv="do_agree", act="다른 사람들은 화가 날 수도 있겠지?")
        
        # 3.1 마무리 대화
        cm.tts(bhv="do_joy_A", string="차례 지키기는 중요한 공공예절이야. 잘 기억해 두자!")
                            
        
        
        
if __name__ == "__main__":
    
    etq = Etiquette()
    etq.Sequence()