# -*- coding: utf-8 -*-

# 문제해결-남의 것을 함부로 손대면 안 돼

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


class Solution():    
    
    def __init__(self): 
        self.user_name = '윤지'
                
        
    def Other(self):
        
        # 1.1 문제 제시
        cm.tts(bhv="do_sad", string="자꾸 다른 친구 물건이 예뻐 보이고 갖고 싶어. ")
        
        # 1.2 경험 질문
        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}는 다른 친구 물건이 갖고 싶거나 만져보고 싶을 때가 있었니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}도 잘 몰라서 속상했던 적이 있니?는 다른 친구 물건이 갖고 싶거나 만져보고 싶을 때가 있었니?",
                                   pos_bhv="do_question_S", pos="어떤 물건이었는지 기억이 나니?")                

        if answer[0] == "positive":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q="어떤 물건이었는지 기억이 나니?",
                                       neu_bhv="do_agree", neu="괜찮아~ 생각이 나지 않을 수 있어~")

        cm.tts(bhv="do_question_S", string="다른 친구 물건이 예뻐 보여서 갖고 싶을 땐 어떻게 하는 게 좋을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="다른 친구 물건이 예뻐 보여서 갖고 싶을 땐 어떻게 하는 게 좋을까?",
                                   pos_bhv="do_agree", pos="그렇게 생각하는구나!",
                                   neu_bhv="do_explain_C", neu="괜찮아~ 모를 수도 있어~",
                                   act_bhv="do_agree", act="그렇게 생각하는구나!")
        
        cm.tts(bhv="do_question_S", string=f"다른 친구가 {wm.word(self.user_name, 0)} 물건을 함부로 만지면 {wm.word(self.user_name, 0)}는 기분이 어떨까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"다른 친구가 {wm.word(self.user_name, 0)} 물건을 함부로 만지면 {wm.word(self.user_name, 0)}는 기분이 어떨까?",
                                   pos_bhv="do_agree", pos=f"{wm.word(self.user_name, 0)}의 기분이 안 좋겠지?",
                                   neu_bhv="do_explain_B", neu=f"아마 {wm.word(self.user_name, 0)}의 기분이 안 좋겠지?",
                                   neg_bhv="do_agree", neg=f"{wm.word(self.user_name, 0)}의 기분이 안 좋겠지?",
                                   act_bhv="do_agree", act=f"{wm.word(self.user_name, 0)}의 기분이 안 좋겠지?")
        
        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}가 친구의 물건을 마음대로 만지면 친구의 기분을 어떨까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}가 친구의 물건을 마음대로 만지면 친구의 기분을 어떨까?",
                                   pos_bhv="do_agree", pos="친구의 기분도 안 좋을 것 같아",
                                   neu_bhv="do_explain_B", neu="괜찮아~ 상상하기 어려울 수 있어~ 아마 친구의 기분도 안 좋을 것 같아.",
                                   neg_bhv="do_agree", neg="친구의 기분도 안 좋을 것 같아",
                                   act_bhv="do_agree", act="친구의 기분도 안 좋을 것 같아")
        
        cm.tts(bhv="do_question_S", string="친구의 물건을 만져보고 싶을때는 친구에게 어떻게 이야기 해야 할까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="친구의 물건을 만져보고 싶을때는 친구에게 어떻게 이야기 해야 할까?",
                                   neu_bhv="do_suggestion_S", neu="만져봐도 될까? 라고 말하면 어떨까?")
        
        # 2.1 문제 해결
        cm.tts(bhv="do_joy_A", string="파이보도 친구들의 물건을 함부로 만지면 안되는 것을 알았어~ 알려줘서 정말 고마워!")
                            
        
        
        
if __name__ == "__main__":
    
    sol = Solution()
    sol.Other()