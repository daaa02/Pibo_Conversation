# -*- coding: utf-8 -*-

# 문제해결-혼나서 속상해

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
                
        
    def Upset1(self):
        
        # 1.1 문제 제시
        cm.tts(bhv="do_sad", string="한 번 혼나고 나면 오랫동안 기분이 안 좋아.")
        
        # 1.2 경험 질문
        cm.tts(bhv="do_sad", string=f"{wm.word(self.user_name, 0)}도 한번씩 혼이 나니?")
        answer = cm.responses_proc(re_bhv="do_sad", re_q=f"{wm.word(self.user_name, 0)}도 한번씩 혼이 나니?",
                                   pos_bhv="do_sad", pos=f"{wm.word(self.user_name, 0)}도 속상했겠다.")    
    
        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}는 혼나면 어떻게 하니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}는 혼나면 어떻게 하니?",
                                   neu_bhv="do_agree", neu="괜찮아~ 말하기 어려울 수 있어~")

        cm.tts(bhv="do_question_L", string=f"주변에서 누가 가장 {wm.word(self.user_name, 0)}를 많이 혼내니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"주변에서 누가 가장 {wm.word(self.user_name, 0)}를 많이 혼내니?",
                                   neu_bhv="do_agree", neu="괜찮아~ 말하기 어려울 수 있어~")

        cm.tts(bhv="do_question_S", string="혼내는 사람의 마음도 속상할까? ")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="혼내는 사람의 마음도 속상할까? ",
                                   pos_bhv="do_agree", pos="혼내는 사람도 속상할 것 같아.",
                                   neu_bhv="do_agree", neu="몰라도 괜찮아~",
                                   act_bhv="do_agree", act="혼내는 사람도 속상할 것 같아.")
        
        cm.tts(bhv="do_question_L", string="혼나고 나서 어떻게 하면 기분이 좋아질까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="화가 날 때 재미있는 놀이를 하면 기분이 좋아질까?",
                                   pos_bhv="do_agree", pos="기분이 좋아지겠다~",
                                   neu_bhv="do_agree", neu="괜찮아~ 생각이 나지 않을 수 있어~")
        
        cm.tts(bhv="do_question_L", string="혼난 친구에게 무슨 말을 해주면 좋을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="혼난 친구에게 무슨 말을 해주면 좋을까?",
                                   pos_bhv="do_agree", pos="친구에게 도움이 되겠는 걸?",
                                   neu_bhv="do_agree", neu="괜찮아~ 생각이 나지 않을 수 있어~",
                                   act_bhv="do_agree", act="친구에게 도움이 되겠는 걸?")
        
        # 2.1 문제 해결
        cm.tts(bhv="do_joy_A", string="파이보도 혼나고 나서 기분이 좋아지도록 노력해야겠다~ 알려줘서 정말 고마워!")
                            
        
        
        
if __name__ == "__main__":
    
    sol = Solution()
    sol.Upset1()