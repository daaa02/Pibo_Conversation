# -*- coding: utf-8 -*-

# 사회기술-친구집에서 놀고 난 후에는 정리해요

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
        self.correct = ['친구', '장난감', '정리']
        self.ox = ''
                
        
    def Friend5(self):
        
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
        
        cm.tts(bhv="do_explain_A", string="이 카드의 어린이는 친구 집에서 같이 놀고 장난감을 정리하지 않았어.")
     
        # 2.2 경험 질문
        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}는 친구 집에서 놀았던 적이 있니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}는 친구 집에서 놀았던 적이 있니?",
                                   pos_bhv="do_question_S", pos="누구와 함께 가서 놀았니?")
        
        if answer[0] == "positive":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q="누구와 함께 가서 놀았니?",
                                       neu_bhv="do_agree", neu="기억이 안 날 수 있지~ 어떤 장난감을 가지고 놀았니?",
                                       act_bhv="do_question_S", act="어떤 장난감을 가지고 놀았니?")
            
            answer = cm.responses_proc(re_bhv="do_question_S", re_q="어떤 장난감을 가지고 놀았니?",
                                       pos_bhv="do_joy_B", pos="정말 재밌었겠는걸?",
                                       neu_bhv="do_agree", neu="기억이 안 날 수 있지~",
                                       act_bhv="do_joy_B", act="정말 재밌었겠는걸?")
            
            cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}는 장난감을 가지고 논 뒤에 정리를 잘 하니?")
            answer = cm.responses_proc(re_bhv="do_question_L", re_q="친구 집에서 늦게 까지 놀면 집에서 엄마가 기다리시겠지?",
                                       pos_bhv="do_explain_A", pos="대단한 걸? 자기가 가지고 논 장난감은 스스로 정리하는 것이 맞아~",
                                       neu_bhv="do_explain_A", neu="자기가 가지고 논 장난감이라면 스스로 정리하는 것이 맞아~")
        
        # 2.3 문제 인식
        cm.tts(bhv="do_question_L", string="놀고 난 뒤 친구 혼자서 많은 장난감을 정리하려면 힘들겠지?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="놀고 난 뒤 친구 혼자서 많은 장난감을 정리하려면 힘들겠지?",
                                   pos_bhv="do_explain_C", pos="너무 힘들어서 다음에는 초대하지 않을지도 몰라~",
                                   neu_bhv="do_explain_C", neu="괜찮아. 모를 수도 있어~ 잠을 자야 하는데 너무 힘들어서 다음에는 초대하지 않을지도 몰라~",
                                   act_bhv="do_explain_C", act="너무 힘들어서 다음에는 초대하지 않을지도 몰라~")
    
        # 3.1 마무리 대화
        cm.tts(bhv="do_joy_A", string="친구네 집에 가서 재밌게 놀고 난 뒤에는 정리하는 것을 도와줘야 해~ 꼭 기억해!")
    
        
        
        
if __name__ == "__main__":
    
    etq = Etiquette()
    etq.Friend5()