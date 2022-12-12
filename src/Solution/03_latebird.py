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
        cm.tts(bhv="do_sad", string="요즘 늦은 시간까지 안자고 계속 놀고 싶어.")
        
        # 1.2 경험 질문
        cm.tts(bhv="do_sad", string=f"{wm.word(self.user_name, 0)}도 밤 늦게까지 놀고 싶니?")
        answer = cm.responses_proc(re_bhv="do_sad", re_q=f"{wm.word(self.user_name, 0)}도 씻기 싫을 때가 있지?",
                                   pos_bhv="do_agree", pos="나랑 비슷한 걸?")    
     
        # 2.2 경험 질문
        cm.tts(bhv="do_question_L", string="어떻게 하면 계속 놀고 싶은 마음을 멈출 수 있을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="어떻게 하면 계속 놀고 싶은 마음을 멈출 수 있을까?",
                                   neu_bhv="do_agree", neu="괜찮아~ 바로 떠오르지 않을 수 있어~")

        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}는 밤에도 조용히 놀 수 있니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}는 밤에도 조용히 놀 수 있니?",
                                   pos_bhv="do_explain_C", pos="대단한 걸? 나는 조용히 못 놀아.")

        cm.tts(bhv="do_question_S", string="동화책을 보면 조용히 놀 수 있을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="동화책을 보면 조용히 놀 수 있을까?")
            
        cm.tts(bhv="do_question_S", string="늦게까지 놀면 다음 날 무슨 일이 생길까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="늦게까지 놀면 다음 날 무슨 일이 생길까?",
                                   pos_bhv="do_joy_B", pos="다음 날 피곤하겠지?",
                                   neu_bhv="do_agree", neu="괜찮아~ 상상하기 어려울 수 있어. 아마 다음 날 피곤하겠지?",
                                   act_bhv="do_joy_B", act="다음 날 피곤하겠지?")
        
        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}는 내일 무엇을 하며 놀고 싶니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}는 밤에도 조용히 놀 수 있니?",
                                   pos_bhv="do_explain_C", pos="내일 아침이 기다려 지겠다!",
                                   neu_bhv="do_agree", neu="괜찮아~ 바로 떠오르지 않을 수 있어~",
                                   act_bhv="do_joy_A", act="내일 아침이 기다려 지겠다!")
        
        # 2.1 문제 해결
        cm.tts(bhv="do_joy_A", string="파이보도 이제는 늦게까지 놀지 않고 다음 날 아침을 기분 좋게 시작해야겠다~ 알려줘서 정말 고마워!")
                            
        
        
        
if __name__ == "__main__":
    
    sol = Solution()
    sol.Wash()