# -*- coding: utf-8 -*-

# 사회기술-물건을 두 손으로 받고 드려요

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
        self.correct = ['어른', '손', '받']
        self.ox = ''
                
        
    def Object1(self):
        
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
        
        cm.tts(bhv="do_explain_A", string="이 카드의 어린이는 어른이 건네주는 물건을 두 손으로 받고 있지 않아.")
     
        # 2.2 경험 질문
        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}는 친구들에게 물건을 줄 때 어떻게 주니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}는 친구들에게 물건을 줄 때 어떻게 주니?",
                                   pos_bhv="do_joy_A", pos="한 손으로 친절하게 전달해 줘야겠지?",
                                   act_bhv="do_joy_B", act="한 손으로 친절하게 전달해 줘야겠지?")
        
        cm.tts(bhv="do_question_S", string="어른들께 물건을 드릴 땐, 어떻게 드리는게 좋을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="어른들께 물건을 드릴 땐, 어떻게 드리는게 좋을까?",
                                   neu_bhv="do_explain_A", neu="두 손으로 공손하게 전달해 드려야 해!")
        
        cm.tts(bhv="do_question_S", string="어른들께서 주는 물건을 받을 땐, 어떻게 받는 것이 맞을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="어른들께 물건을 드릴 땐, 어떻게 드리는게 좋을까?",
                                   pos_bhv="do_explain_B", pos="두 손으로 감사합니다~ 인사하며 받아야 해!",
                                   neu_bhv="do_explain_B", neu="두 손으로 감사합니다~ 인사하며 받아야 해!",
                                   act_bhv="do_explain_B", act="두 손으로 감사합니다~ 인사하며 받아야 해!")
        
        # 2.3 문제 인식
        cm.tts(bhv="do_question_L", string="어른들께 물건을 드릴 때 한 손으로 물건을 받거나 드리게 되면 어른들은 기분이 어떠실까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="어른들께 물건을 드릴 때 한 손으로 물건을 받거나 드리게 되면 어른들은 기분이 어떠실까?",
                                   pos_bhv="do_explain_C", pos=f"{wm.word(self.user_name, 0)}는 버릇이 없다고 생각하실 거야!",
                                   neu_bhv="do_explain_C", neu=f"괜찮아. 모를 수도 있어~ {wm.word(self.user_name, 0)}는 버릇이 없다고 생각하실 거야!",
                                   act_bhv="do_explain_C", act=f"{wm.word(self.user_name, 0)}는 버릇이 없다고 생각하실 거야!")
    
        # 3.1 마무리 대화
        cm.tts(bhv="do_joy_A", string=f"어른들께 물건을 드리거나 받을 땐, 두 손으로 공손하게 드리고 받는 예의 바른 {wm.word(self.user_name, 0)}가 되자!")
    
        
        
        
if __name__ == "__main__":
    
    etq = Etiquette()
    etq.Object1()