# -*- coding: utf-8 -*-

# 문제해결-친구가 기분이 안 좋아 보여

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
                
        
    def Cheerup(self):
        
        # 1.1 문제 제시
        cm.tts(bhv="do_sad", string="기분이 안 좋은 친구를 어떻게 기쁘게 만들 수 있을지 궁금해.")
        
        # 1.2 경험 질문
        cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}는 기분이 안 좋은 친구를 기쁘게 만들어 준 적이 있니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}는 기분이 안 좋은 친구를 기쁘게 만들어 준 적이 있니?",
                                   pos_bhv="do_question_S", pos="친구가 정말 좋아했겠다!")                
    
            
        cm.tts(bhv="do_question_L", string=f"나는 기분이 안 좋을 때 잠을 자. {wm.word(self.user_name, 0)}는 기분이 안 좋을 때 어떻게 하니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"나는 기분이 안 좋을 때 잠을 자. {wm.word(self.user_name, 0)}는 기분이 안 좋을 때 어떻게 하니?",
                                   neu_bhv="do_explain_A", neu="괜찮아~ 생각이 나지 않을 수 있어~")
            
        cm.tts(bhv="do_question_L", string=f"나는 칭찬을 들었을 때 기분이 좋아져. {wm.word(self.user_name, 0)}는 어떤 칭찬을 들으면 기분이 좋아지니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"나는 칭찬을 들었을 때 기분이 좋아져. {wm.word(self.user_name, 0)}는 어떤 칭찬을 들으면 기분이 좋아지니?",
                                   pos_bhv="do_agree", pos="듣기만 해도 좋은 걸?",
                                   neu_bhv="do_agree", neu="괜찮아~ 바로 떠오르지 않을 수 있어~",
                                   act_bhv="do_agree", act="듣기만 해도 좋은 걸?")
            
        cm.tts(bhv="do_question_S", string="친구들이랑 재미있는 놀이를 하면 기분이 좋아질까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="친구들이랑 재미있는 놀이를 하면 기분이 좋아질까?",
                                   pos_bhv="do_agree", pos="같이 놀이를 하면 신나겠다~")
        
        cm.tts(bhv="do_question_L", string="나는 맛있는 음식을 먹어도 기분이 좋아져. 무엇을 먹으면 기분이 좋아질까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="나는 맛있는 음식을 먹어도 기분이 좋아져. 무엇을 먹으면 기분이 좋아질까?",
                                   pos_bhv="do_explain_B", pos="기분이 좋아지겠다~")
        
        cm.tts(bhv="do_question_L", string="기분이 안 좋은 친구를 어떻게 도와주는게 좋을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="기분이 안 좋은 친구를 어떻게 도와주는게 좋을까?",
                                   pos_bhv="do_agree", pos="친구에게 도움이 되겠는 걸?",
                                   neu_bhv="do_suggestion_S", neu="괜찮아~ 모를 수도 있어~ 친구랑 재미있는 놀이를 같이해도 좋겠지?",
                                   act_bhv="do_agree", act="친구에게 도움이 되겠는 걸?")
        
        
        # 2.1 문제 해결
        cm.tts(bhv="do_joy_A", string="파이보도 기분이 안 좋은 친구를 잘 도와줘 볼게. 알려줘서 정말 고마워!")
                            
        
        
        
if __name__ == "__main__":
    
    sol = Solution()
    sol.Cheerup()