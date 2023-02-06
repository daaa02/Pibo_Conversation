# -*- coding: utf-8 -*-

# 사회기술-친구를 도와줘요

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
        self.correct = ['도와', '도우', '도울']
        self.ox = ''
                
        
    def Friend3(self):
        
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
        
        cm.tts(bhv="do_explain_A", string="이 카드의 어린이는 친구를 도와주지 않고 있어.")
     
        # 2.2 경험 질문
        cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}는 친구를 잘 도와주니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}는 친구를 잘 도와주니?",
                                   pos_bhv="do_joy_A", pos="정말 대단한 걸!")
        
        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}도 도움이 필요한 적이 있었니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}도 도움이 필요한 적이 있었니?",
                                   pos_bhv="do_question_S", pos="언제였니?",
                                   neu_bhv="do_agree", neu="기억이 안 날 수도 있지~")
        
        if answer[0] == "positive":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q="언제였니?",
                                       pos_bhv="do_agree", pos="그 때 도움이 필요했구나!",
                                       neu_bhv="do_agree", neu="기억이 안 날 수도 있어~")            
        
        # 2.3 문제 인식
        cm.tts(bhv="do_question_L", string="도움이 필요한 친구를 보면 어떻게 해야 할까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="도움이 필요한 친구를 보면 어떻게 해야 할까?",
                                   pos_bhv="do_explain_B", pos="친구에게 어떻게 도와주면 좋을지 물어보면 좋을 것 같아~",
                                   neu_bhv="do_explain_B", neu="몰라도 괜찮아~ 친구에게 어떻게 도와주면 좋을지 물어보면 좋을 것 같아~",
                                   act_bhv="do_explain_B", act="친구에게 어떻게 도와주면 좋을지 물어보면 좋을 것 같아~")
    
        # 3.1 마무리 대화
        cm.tts(bhv="do_joy_A", string=f"{wm.word(self.user_name, 0)}에게 친구들이 도와 달라고 하면 도와주자~ 할 수 없거나 위험한 일이라면 어른들께 도움을 구해 보는 것도 좋을 거야!")
    
        
        
        
if __name__ == "__main__":
    
    etq = Etiquette()
    etq.Friend3()