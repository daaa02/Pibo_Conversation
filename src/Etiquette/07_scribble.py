# -*- coding: utf-8 -*-

# 사회기술-아무 곳에나 낙서를 하지 않아요

import os, sys
import re
import random

sys.path.append('/home/kiro/workspace/Conversation_Scenarios/')
from data.conversation_manage import ConversationManage, WordManage
from data.speech_to_text import speech_to_text
from data.text_to_speech import TextToSpeech, text_to_speech

cm = ConversationManage()
wm = WordManage()
audio = TextToSpeech()


class Etiquette():    
    
    def __init__(self): 
        self.user_name = '다영'
        self.correct = ['낙서', '그림']
        self.ox = ''
                
        
    def Scribble(self):
        
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
        
        cm.tts(bhv="do_explain_A", string="이 카드의 어린이는 아무 곳에나 낙서를 했어.")
     
        # 2.2 경험 질문
        cm.tts(bhv="do_question_S", string="낙서를 하는 사람을 본 적이 있니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="낙서를 하는 사람을 본 적이 있니?",
                                   pos_bhv="do_agree", pos="본 적이 있구나!",
                                   neu_bhv="do_agree", neu="괜찮아. 기억이 안 날 수도 있어~")

        cm.tts(bhv="do_question_L", string="그림을 그리고 싶을 때는 어디에 그리는게 좋을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="그림을 그리고 싶을 때는 어디에 그리는게 좋을까?",
                                   pos_bhv="do_agree", pos="그림은 스케치북이나 종이에 그리는게 좋겠지?",
                                   neu_bhv="do_explain_C", neu="괜찮아 모를 수도 있어~ 그림은 스케치북이나 종이에 그리는게 좋겠지?",
                                   act_bhv="do_agree", act="그림은 스케치북이나 종이에 그리는게 좋겠지?")
            
        cm.tts(bhv="do_question_L", string="모두가 아무 곳에나 그림을 그리면 어떤 일이 일어날까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="모두가 아무 곳에나 그림을 그리면 어떤 일이 일어날까?",
                                   pos_bhv="do_sad", pos="벽이 엄청 지저분해지고 청소하는 사람이 힘들겠지?",
                                   neu_bhv="do_agree", neu="괜찮아 상상이 안 될 수 있어. 벽이 엄청 지저분해지고 청소하는 사람이 힘들겠지?",
                                   act_bhv="do_agree", act="벽이 엄청 지저분해지고 청소하는 사람이 힘들겠지?")
    
        # 2.3 문제 인식
        cm.tts(bhv="do_question_L", string="아무 곳에나 그림을 그리는 사람을 보면 사람들은 어떻게 생각할까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="아무 곳에나 그림을 그리는 사람을 보면 사람들은 어떻게 생각할까?",
                                   pos_bhv="do_agree", pos="공공시설물을 망가뜨리는 것을 보고 올바르지 않다고 생각하겠지?",
                                   neu_bhv="do_explain_A", neu="괜찮아 모를 수도 있어~ 공공시설물을 망가뜨리는 것을 보고 올바르지 않다고 생각하겠지?",
                                   act_bhv="do_agree", act="공공시설물을 망가뜨리는 것을 보고 올바르지 않다고 생각하겠지?")
    
        # 3.1 마무리 대화
        cm.tts(bhv="do_joy_A", string="모두가 함께 쓰는 공간은 깨끗하게 사용해야 해. 잘 기억해 두자!")
    
        
        
        
if __name__ == "__main__":
    
    etq = Etiquette()
    etq.Scribble()