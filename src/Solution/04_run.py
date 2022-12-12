# -*- coding: utf-8 -*-

# 문제해결-씻기 싫어

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


class Solution():    
    
    def __init__(self): 
        self.user_name = '다영'
                
        
    def Wash(self):
        
        # 1.1 문제 제시
        cm.tts(bhv="do_sad", string="요즘 사람들이 많은 곳이든 집 안이든 신나게 뛰어다니고 싶어.")
        
        # 1.2 경험 질문
        cm.tts(bhv="do_sad", string=f"{wm.word(self.user_name, 0)}도 뛰다가 넘어진 적이 있니?")
        answer = cm.responses_proc(re_bhv="do_sad", re_q=f"{wm.word(self.user_name, 0)}도 씻기 싫을 때가 있지?",
                                   pos_bhv="do_agree", pos="넘어져서 아팠겠다~")    
    
        # 2.2 경험 질문
        cm.tts(bhv="do_question_L", string="사람이 많은 곳에서 뛰어다니면 위험할까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="사람이 많은 곳에서 뛰어다니면 위험할까?",
                                   pos_bhv="do_agree", pos="부딪히면 아프겠지?",
                                   neu_bhv="do_agree", neu="괜찮아~ 부딪히면 아프겠지?")

        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}는 평소에 천천히 조용히 걷니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}는 평소에 천천히 조용히 걷니?",
                                   pos_bhv="do_explain_C", pos="신사같은 걸?")

        cm.tts(bhv="do_question_S", string="천천히 걸으면 어떤 점이 좋을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="천천히 걸으면 어떤 점이 좋을까?",
                                   pos_bhv="do_agree", pos="천천히 걸으면 안전하겠지?",
                                   neu_bhv="do_agree", neu="괜찮아~ 생각이 나지 않을 수 있어~ 천천히 걸으면 안전하겠지?",
                                   act_bhv="do_agree", act="천천히 걸으면 안전하겠지?")
            
        cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}는 천장에서 발소리를 들어 본 적이 있니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}는 천장에서 발소리를 들어 본 적이 있니?",
                                   pos_bhv="do_joy_B", pos="시끄러웠겠다!")
        
        cm.tts(bhv="do_question_L", string="어떻게 하면 발소리가 나지 않게 조용히 걸을 수 있을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="어떻게 하면 발소리가 나지 않게 조용히 걸을 수 있을까?",
                                   pos_bhv="do_agree", pos="사뿐사뿐 천천히 걸어야겠지?",
                                   neu_bhv="do_agree", neu="괜찮아~ 대답하기 어려울 수 있어~ 사뿐사뿐 천천히 걸으면 발소리가 나지 않겠지?",
                                   act_bhv="do_agree", act="사뿐사뿐 천천히 걸어야겠지?")
        # 2.1 문제 해결
        cm.tts(bhv="do_joy_A", string="파이보도 이제 조용하고 안전하게 걸으려고 노력해야겠다~ 알려줘서 정말 고마워!")
                            
        
        
        
if __name__ == "__main__":
    
    sol = Solution()
    sol.Wash()