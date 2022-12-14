# -*- coding: utf-8 -*-

# 문제해결-기분 나쁜 말을 들어서 속상해

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
                
        
    def Upset3(self):
        
        # 1.1 문제 제시
        cm.tts(bhv="do_sad", string="기분 나쁜 말을 들어서 너무 속상해.")
        
        # 1.2 경험 질문
        cm.tts(bhv="do_sad", string=f"{wm.word(self.user_name, 0)}도 기분 나쁜 말을 들어서 속상했던 적이 있었니?")
        answer = cm.responses_proc(re_bhv="do_sad", re_q=f"{wm.word(self.user_name, 0)}도 기분 나쁜 말을 들어서 속상했던 적이 있었니?",
                                   pos_bhv="do_question_S", pos=f"{wm.word(self.user_name, 0)}도 속상했겠다. 어떤 일이 있었니?",
                                   neu_bhv="do_agree", neu="괜찮아~ 생각이 나지 않을 수 있어~")    
        
        if answer[0] == "positive":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}도 속상했겠다. 어떤 일이 있었니?",
                                   neu_bhv="do_agree", neu="괜찮아~ 대답하기 어려울 수 있어~")
            

        cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}는 친구에게 기분 나쁜 말을 들었을 때 어떻게 하니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}는 친구에게 기분 나쁜 말을 들었을 때 어떻게 하니?",
                                   neg_bhv="do_agree", neg="몰라도 괜찮아~")

        cm.tts(bhv="do_question_L", string="친구에게 기분 나쁜 말을 들으면 똑같이 기분 나쁜 말을 해줘야 할까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="다른사람에게 속상한 마음을 말한다면 어떻게 말해야 할까?",
                                   pos_bhv="do_agree", pos="친구를 속상하게 만드는 건 좋지 않겠지?",
                                   neu_bhv="do_explain_C", neu="괜찮아~ 생각이 나지 않을 수 있어~ 친구를 속상하게 만드는 건 좋지 않겠지?",
                                   neg_bhv="do_explain_C", neg="친구를 속상하게 만드는 건 좋지 않겠지?",
                                   act_bhv="do_agree", act="친구를 속상하게 만드는 건 좋지 않겠지?")
        
        cm.tts(bhv="do_question_L", string="기분 나쁜 말을 들었을 때 친구에게 뭐라고 말해주는게 좋을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="기분 나쁜 말을 들었을 때 친구에게 뭐라고 말해주는게 좋을까?",
                                   neu_bhv="do_agree", neu="괜찮아~ 모를 수도 있어~")
        
        cm.tts(bhv="do_question_L", string="어떻게 하면 친구와 같이 기분이 좋아질 수 있을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="어떻게 하면 친구와 같이 기분이 좋아질 수 있을까?",
                                   neu_bhv="do_agree", neu="괜찮아~ 모를 수도 있어~")
        
        cm.tts(bhv="do_question_S", string="어떤 놀이를 하면 즐겁게 같이 놀 수 있을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="또 다른 방법은 뭐가 있을까?",
                                pos_bhv="do_joy_B", pos="그럼 정말 기분이 좋아지겠다~",
                                neu_bhv="do_agree", neu="몰라도 괜찮아~",
                                act_bhv="do_joy_B", act="그럼 정말 기분이 좋아지겠다~")
        
        # 2.1 문제 해결
        cm.tts(bhv="do_joy_A", string=f"파이보도 상대방을 생각해서 기분 나쁜 말을 사용하지 않아야 겠다~ {wm.word(self.user_name, 0)}도 그랬으면 좋겠어!")
                            
        
        
        
if __name__ == "__main__":
    
    sol = Solution()
    sol.Upset3()