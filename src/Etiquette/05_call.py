# -*- coding: utf-8 -*-

# 사회기술-큰 소리로 이야기 하거나 통화하지 않아요

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
        self.correct = ['시끄', '통화', '이야기', '큰 소리']
        self.ox = ''
                
        
    def Call(self):
        
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
        
        cm.tts(bhv="do_explain_A", string="이 카드의 어린이는 전화 통화를 시끄럽게 했어.")
     
        # 2.2 경험 질문
        cm.tts(bhv="do_question_S", string="시끄럽게 이야기를 하는 사람을 본 적이 있니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="시끄럽게 이야기를 하는 사람을 본 적이 있니?",
                                   pos_bhv="do_agree", pos="본 적이 있구나!",
                                   neu_bhv="do_agree", neu="괜찮아 기억이 안 날 수도 있어~ ")

        cm.tts(bhv="do_question_L", string="우리는 어떤 상황에서 조용히 이야기해야 할까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="우리는 어떤 상황에서 조용히 이야기해야 할까?",
                                   pos_bhv="do_agree", pos="모두가 함께 있는 공간에서는 조용히 이야기하는 것이 좋겠지?",
                                   neu_bhv="do_explain_C", neu="괜찮아 생각이 안날 수도 있어~ 모두가 함께 있는 공간에서는 조용히 이야기하는 것이 좋겠지?",
                                   act_bhv="do_agree", act="모두가 함께 있는 공간에서는 조용히 이야기하는 것이 좋겠지?")
            
        cm.tts(bhv="do_question_L", string="모두가 시끄럽게 이야기를 하거나 통화를 하면 어떤 일이 일어날까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="모두가 시끄럽게 이야기를 하거나 통화를 하면 어떤 일이 일어날까?",
                                   pos_bhv="do_agree", pos="공간이 시끄러워서 모두 다 더 큰 소리로 이야기해야 겠지?",
                                   neu_bhv="do_explain_B", neu="괜찮아 모를 수도 있어~ 공간이 시끄러워서 모두 다 더 큰 소리로 이야기해야 겠지?",
                                   act_bhv="do_agree", act="공간이 시끄러워서 모두 다 더 큰 소리로 이야기해야 겠지?")
    
        # 2.3 문제 인식
        cm.tts(bhv="do_question_L", string="시끄럽게 이야기를 하거나 전화 통화를 하면 다른 사람들이 어떻게 느낄까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="시끄럽게 이야기를 하거나 전화 통화를 하면 다른 사람들이 어떻게 느낄까?",
                                   pos_bhv="do_agree", pos="다른 사람들은 시끄러워서 화가 날 수도 있겠지?",
                                   neu_bhv="do_explain_A", neu="괜찮아 모를 수도 있어~ 다른 사람들은 시끄러워서 화가 날 수도 있겠지?",
                                   act_bhv="do_agree", act="다른 사람들은 시끄러워서 화가 날 수도 있겠지?")
    
        # 3.1 마무리 대화
        cm.tts(bhv="do_joy_A", string="모두가 함께 있는 공간에서는 조용히 이야기하고 통화하는 것이 좋겠어. 잘 기억해 두자!")
                            
        
        
        
if __name__ == "__main__":
    
    etq = Etiquette()
    etq.Call()