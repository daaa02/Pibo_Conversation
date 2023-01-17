# -*- coding: utf-8 -*-

# 문제해결-나쁜 말을 쓰게 돼

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


class Solution():    
    
    def __init__(self): 
        self.user_name = '다영'
                
        
    def Badword(self):
        
        # 1.1 문제 제시
        cm.tts(bhv="do_sad", string="요즘 나도 모르게 나쁜 말을 자꾸 쓰는 것 같아.")
        
        # 1.2 경험 질문
        cm.tts(bhv="do_sad", string=f"파이보가 {wm.word(self.user_name, 0)}에게도 나쁜 말을 쓰면 기분이 어떨 것 같니?")
        answer = cm.responses_proc(re_bhv="do_sad", re_q=f"파이보가 {wm.word(self.user_name, 0)}에게도 나쁜 말을 쓰면 기분이 어떨 것 같니?",
                                   neg_bhv="do_agree", neg=f"{wm.word(self.user_name, 0)}의 기분이 안 좋겠지?",
                                   act_bhv="do_agree", act=f"{wm.word(self.user_name, 0)}의 기분이 안 좋겠지?")    

        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}가 나쁜 말을 쓰면 다른 친구들은 기분이 어떨까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}가 나쁜 말을 쓰면 다른 친구들은 기분이 어떨까?",
                                   neu_bhv="do_agree", neu="괜찮아~ 상상하기 어려울 수 있어~",
                                   neg_bhv="do_agree", neg="친구들도 기분이 안 좋겠지?",
                                   act_bhv="do_agree", act="친구들도 기분이 안 좋겠지?")

        cm.tts(bhv="do_question_S", string="친구에게 나쁜 말을 하고 싶을 때는 참는게 좋겠지?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="친구에게 나쁜 말을 하고 싶을 때는 참는게 좋겠지?",
                                   neu_bhv="do_explain_C", neu="나쁜 말을 쓰면 기분이 안 좋아지니까 참는게 좋을 것 같아.")

        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)} 주변에는 기분 좋을 말을 누가 가장 많이 하니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)} 주변에는 기분 좋을 말을 누가 가장 많이 하니?",
                                   pos_bhv="do_agree", pos="나도 배우고 싶은 걸?")
        
        cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}는 어떤 말을 들으면 가장 기분이 좋니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}는 어떤 말을 들으면 가장 기분이 좋니?",
                                   pos_bhv="do_joy_B", pos="기분이 좋았겠다!",
                                   neu_bhv="do_agree", neu="괜찮아~ 바로 떠오르지 않을 수 있어~")
            
        cm.tts(bhv="do_question_L", string="나는 척척박사라는 말을 들으면 기분이 좋아! 기분 좋은 말에는 또 뭐가 있을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="나는 척척박사라는 말을 들으면 기분이 좋아! 기분 좋은 말에는 또 뭐가 있을까?",
                                   pos_bhv="do_joy_B", pos="듣기만 해도 행복한 걸?",
                                   neu_bhv="do_agree", neu="괜찮아~ 생각이 나지 않을 수 있어~",
                                   act_bhv="do_joy_B", act="듣기만 해도 행복한 걸?")
        
        # 2.1 문제 해결
        cm.tts(bhv="do_joy_A", string="파이보도 이제 기분 좋은 말을 많이 쓰도록 노력해야겠다~ 알려줘서 정말 고마워!")
                            
        
        
        
if __name__ == "__main__":
    
    sol = Solution()
    sol.Badword()