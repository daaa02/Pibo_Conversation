# -*- coding: utf-8 -*-

# 사회기술-다른 사람의 몸을 함부로 만지지 않아요

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
        self.correct = ['친구', '몸', '만지', '만졌']
        self.ox = ''
                
        
    def Body(self):
        
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
        
        cm.tts(bhv="do_explain_A", string="이 카드의 어린이는 다른 친구의 몸을 함부로 만지고 있어.")
     
        # 2.2 경험 질문
        cm.tts(bhv="do_question_S", string="친구가 다른 사람의 몸을 함부로 만지는 것을 본 적이 있니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="친구가 다른 사람의 몸을 함부로 만지는 것을 본 적이 있니?",
                                   pos_bhv="do_question_S", pos="어떤 친구가 그랬니?")
        
        if answer[0] != "negative":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q="어떤 친구가 그랬니?")
            
            cm.tts(bhv="do_question_S", string="그럴 땐 어떻게 해야 할까?")
            answer = cm.responses_proc(re_bhv="do_question_S", re_q="그럴 땐 어떻게 해야 할까?",
                                       pos_bhv="do_explain_B", pos="어른들의 도움이 필요할 수 있어! 선생님이나 엄마에게 이야기하는 건 어떨까?",
                                       neu_bhv="do_explain_B", neu="어른들의 도움이 필요할 수 있어! 선생님이나 엄마에게 이야기하는 건 어떨까?",
                                       neg_bhv="do_explain_B", neg="어른들의 도움이 필요할 수 있어! 선생님이나 엄마에게 이야기하는 건 어떨까?",
                                       act_bhv="do_explain_B", act="어른들의 도움이 필요할 수 있어! 선생님이나 엄마에게 이야기하는 건 어떨까?")
            
        cm.tts(bhv="do_question_L", string="친구의 몸을 함부로 만지는 친구를 본다면 어떻게 해야 할까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="친구의 몸을 함부로 만지는 친구를 본다면 어떻게 해야 할까?",
                                   pos_bhv="do_explain_C", pos="그 친구에게 하지 말라고 말한 뒤, 어른들에게 도움을 구해야 할 것 같아!",
                                   neu_bhv="do_explain_C", neu="그 친구에게 하지 말라고 말한 뒤, 어른들에게 도움을 구해야 할 것 같아!",
                                   neg_bhv="do_explain_C", neg="그 친구에게 하지 말라고 말한 뒤, 어른들에게 도움을 구해야 할 것 같아!",
                                   act_bhv="do_explain_C", act="그 친구에게 하지 말라고 말한 뒤, 어른들에게 도움을 구해야 할 것 같아!")
        
        # 2.3 문제 인식
        cm.tts(bhv="do_question_L", string="다른 친구의 몸을 함부로 만지면 그 친구의 기분이 어떨까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="다른 친구의 몸을 함부로 만지면 그 친구의 기분이 어떨까?",
                                   pos_bhv="do_explain_B", pos="정말 기분이 안 좋겠지?",
                                   neu_bhv="do_explain_B", neu="괜찮아. 모를 수도 있어~ 그 친구는 정말 기분이 안 좋을 것 같아!",
                                   act_bhv="do_explain_B", act="정말 기분이 안 좋겠지?")
    
        # 3.1 마무리 대화
        cm.tts(bhv="do_joy_A", string=f"다른 친구의 몸을 함부로 만지면 안 돼. 친구가 싫어하는 건 하지 않도록 하자!")
    
        
        
        
if __name__ == "__main__":
    
    etq = Etiquette()
    etq.Body()