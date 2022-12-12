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
                                   pog_bhv="do_explain_C", pog="대단한 걸? 나는 조용히 못 놀아.")

        cm.tts(bhv="do_question_S", string="오랫동안 안 씻으면 어떻게 될까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="오랫동안 안 씻으면 어떻게 될까?",
                                   pos_bhv="do_agree", pos="오랫동안 안 씻으면 몸이 아플수도 있겠다!",
                                   neu_bhv="do_agree", neu="괜찮아~ 바로 떠오르지 않을 수 있어~",
                                   act_bhv="do_agree", act="오랫동안 안 씻으면 몸이 아플수도 있겠다!")
            
        cm.tts(bhv="do_question_S", string="안 씻어서 냄새가 나면 친구들이 싫어할수도 있을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="안 씻어서 냄새가 나면 친구들이 싫어할수도 있을까?",
                                   pos_bhv="do_joy_B", pos="나도 좋은 냄새가 나는 친구가 좋았던 것 같아!",
                                   neu_bhv="do_agree", neu="괜찮아~ 모를 수 있어. 좋은 냄새가 나는 친구가 좋았던 것 같아!",
                                   act_bhv="do_joy_B", act="나도 좋은 냄새가 나는 친구가 좋았던 것 같아!")
        
        # 2.1 문제 해결
        cm.tts(bhv="do_joy_A", string=f"파이보도 향기로워 지도록 잘 씻어야 겠다! {wm.word(self.user_name, 0)}도 깨끗하게 잘 씻자!")
                            
        
        
        
if __name__ == "__main__":
    
    sol = Solution()
    sol.Wash()