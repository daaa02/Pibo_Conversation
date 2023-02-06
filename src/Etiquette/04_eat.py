# -*- coding: utf-8 -*-

# 사회기술-함께 있는 공간에서 소리 내어 음식을 먹지 않아요

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
        self.correct = ['음식', '소리', '김밥', '밥']
        self.ox = ''
                
        
    def Eat(self):
        
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
        
        cm.tts(bhv="do_explain_A", string="이 카드의 어린이는 함께 있는 공간에서 음식을 시끄럽게 먹었어.")
     
        # 2.2 경험 질문
        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}는 음식을 먹을 때 어떻게 먹니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}는 음식을 먹을 때 어떻게 먹니?",
                                   neu_bhv="do_explain_B", neu="괜찮아 생각이 안 날 수도 있어~ ")

        cm.tts(bhv="do_question_L", string="음식을 조용히 먹으려면 어떻게 해야 할까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="음식을 조용히 먹으려면 어떻게 해야 할까?",
                                   pos_bhv="do_agree", pos="입을 다물고 천천히 먹으면 되겠지?",
                                   neu_bhv="do_explain_C", neu="괜찮아 생각이 안 날 수도 있어~ 입을 다물고 천천히 먹으면 되겠지?",
                                   act_bhv="do_agree", act="입을 다물고 천천히 먹으면 되겠지?")
            
        cm.tts(bhv="do_question_L", string="공공장소에서 시끄럽게 음식을 먹으면 어떤 피해를 줄까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="공공장소에서 시끄럽게 음식을 먹으면 어떤 피해를 줄까?",
                                   pos_bhv="do_agree", pos="주변 사람들이 쉬거나 대화하는 것에 방해가 되겠지?",
                                   neu_bhv="do_explain_B", neu="괜찮아 모를 수도 있어~ 주변 사람들이 쉬거나 대화하는 것에 방해가 되겠지?",
                                   act_bhv="do_agree", act="주변 사람들이 쉬거나 대화하는 것에 방해가 되겠지?")
    
        # 2.3 문제 인식
        cm.tts(bhv="do_question_L", string="음식을 시끄럽게 먹으면 다른 사람들이 어떻게 생각할까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="음식을 시끄럽게 먹으면 다른 사람들이 어떻게 생각할까?",
                                   pos_bhv="do_agree", pos="다른 사람들은 지저분하다고 생각할 수도 있겠지?",
                                   neu_bhv="do_explain_A", neu="괜찮아 모를 수도 있어~ 다른 사람들은 지저분하다고 생각할 수도 있겠지?",
                                   act_bhv="do_agree", act="다른 사람들은 지저분하다고 생각할 수도 있겠지?")
    
        # 3.1 마무리 대화
        cm.tts(bhv="do_joy_A", string="함께 사용하는 공간에서는 다른 사람을 배려하기 위해 음식을 조용히 먹는 것이 좋겠어. 잘 기억해 두자!")
                            
        
        
        
if __name__ == "__main__":
    
    etq = Etiquette()
    etq.Eat()