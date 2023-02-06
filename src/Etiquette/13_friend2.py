# -*- coding: utf-8 -*-

# 사회기술-친구집에 가서 물건을 함부로 만지지 않아요

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
        self.correct = ['만지', '만졌', '함부로']
        self.ox = ''
                
        
    def Friend2(self):
        
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
        
        cm.tts(bhv="do_explain_A", string="이 카드의 어린이는 친구 집에 가서 물건들을 함부로 만지고 있어.")
     
        # 2.2 경험 질문
        cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}는 친구 집에 놀러 간 적 있니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}는 친구 집에 놀러 간 적 있니?")
        
        if answer[0] != "negative":
            cm.tts(bhv="do_question_S", string="친구 집에 가서 뭐하고 놀았니?")
            answer = cm.responses_proc(re_bhv="do_question_S", re_q="친구 집에 가서 뭐하고 놀았니?",
                                       neu_bhv="do_agree", neu="기억이 안 날 수도 있어~")

            if answer[0] != "neutral":      # 위 질문의 심화 질문 같아서 옵션 답변으로 변경함 (22/12/09)
                cm.tts(bhv="do_question_S", string="어떤 장난감을 가지고 놀았니?")
                answer = cm.responses_proc(re_bhv="do_question_S", re_q="어떤 장난감을 가지고 놀았니?")
        
        # 2.3 문제 인식
        cm.tts(bhv="do_question_L", string="친구 집에 있는 장난감을 함부로 만지면 그 친구는 기분이 어떨까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="어른들을 보고도 인사를 하지 않으면 어른들은 어떻게 생각할까?",
                                   pos_bhv="do_explain_B", pos="그 친구는 화가 날 수도 있겠지?",
                                   neu_bhv="do_explain_B", neu="괜찮아. 모를 수도 있어~ 그 친구는 화가 날 수도 있겠지?",
                                   act_bhv="do_explain_B", act="그 친구는 화가 날 수도 있겠지?")
    
        # 3.1 마무리 대화
        cm.tts(bhv="do_joy_A", string="다른 친구의 장난감은 함부로 만지지 않아야 해~! 친구들과 사이좋게 지낼 수 있도록 노력하자~")
    
        
        
        
if __name__ == "__main__":
    
    etq = Etiquette()
    etq.Friend2()