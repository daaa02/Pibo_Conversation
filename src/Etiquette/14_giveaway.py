# -*- coding: utf-8 -*-

# 사회기술-장난감이나 놀이 기구를 양보해요

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
        self.correct = ['친구', '장난감', '양보']
        self.ox = ''
                
        
    def Giveaway(self):
        
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
        
        cm.tts(bhv="do_explain_A", string="이 카드의 어린이는 친구들에게 장난감을 양보하지 않았어.")
     
        # 2.2 경험 질문
        cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}는 장난감을 양보하지 않는 친구를 본 적이 있니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}는 장난감을 양보하지 않는 친구를 본 적이 있니?")
        
        if answer[0] == "positive":
            cm.tts(bhv="do_question_S", string="어떤 장난감이었니?")
            answer = cm.responses_proc(re_bhv="do_question_S", re_q="어떤 장난감이었니?",
                                       act_bhv="do_explain_A", act="다 같이 함께 놀면 좋을텐데!")
 
        cm.tts(bhv="do_question_S", string="친구들과 함께 장난감을 나눠 가지고 놀면 더 재밌겠지?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="친구들과 함께 장난감을 나눠 가지고 놀면 더 재밌겠지")
        
        # 2.3 문제 인식
        cm.tts(bhv="do_question_L", string="혼자서만 장난감을 가지고 놀면 다른 친구들은 어떻게 생각할까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="혼자서만 장난감을 가지고 놀면 다른 친구들은 어떻게 생각할까?",
                                   pos_bhv="do_explain_B", pos="다른 친구들은 그 친구와 같이 안 놀고 싶다고 생각할 수 있겠지?",
                                   neu_bhv="do_explain_B", neu="괜찮아. 모를 수도 있어~ 다른 친구들은 그 친구와 같이 안 놀고 싶다고 생각할 수 있겠지?",
                                   act_bhv="do_explain_B", act="다른 친구들은 그 친구와 같이 안 놀고 싶다고 생각할 수 있겠지?")
    
        # 3.1 마무리 대화
        cm.tts(bhv="do_joy_A", string=f"혼자서만 장난감을 다 가지고 놀면 안 돼~ 다른 친구들에게도 장난감을 양보할 수 있는 {wm.word(self.user_name, 0)}가 되자~")
    
        
        
        
if __name__ == "__main__":
    
    etq = Etiquette()
    etq.Giveaway()