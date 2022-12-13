# -*- coding: utf-8 -*-

# 문제해결-내 마음을 몰라줘서 속상해

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
                
        
    def Upset2(self):
        
        # 1.1 문제 제시
        cm.tts(bhv="do_sad", string="다른 사람들이 내 마음을 몰라줘서 속상해. ")
        
        # 1.2 경험 질문
        cm.tts(bhv="do_sad", string=f"{wm.word(self.user_name, 0)}도 다른 사람들이 마음을 몰라줘서 속상했던 적 있었니?")
        answer = cm.responses_proc(re_bhv="do_sad", re_q=f"{wm.word(self.user_name, 0)}도 다른 사람들이 마음을 몰라줘서 속상했던 적 있었니?",
                                   pos_bhv="do_question_S", pos="속상했겠다. 어떤 일이 있었니?",
                                   neu_bhv="do_agree", neu="괜찮아~ 생각이 나지 않을 수 있어~")    
        
        if answer[0] == "positive":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q="속상했겠다. 어떤 일이 있었니?",
                                   neu_bhv="do_explain_A", neu="괜찮아~ 생각이 나지 않을 수 있어~")
            
        cm.tts(bhv="do_question_L", string=f"다른 사람들이 {wm.word(self.user_name, 0)}의 마음을 몰라줄 때 어떤 마음이 들었니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"다른 사람들이 {wm.word(self.user_name, 0)}의 마음을 몰라줄 때 어떤 마음이 들었니?",
                                   neu_bhv="do_agree", neu="괜찮아~ 대답하기 어려울 수 있어~",
                                   act_bhv="do_sad", act="나는 속상해서 눈물이 났어.")

        cm.tts(bhv="do_question_L", string=f"주변에서 누가 가장 {wm.word(self.user_name, 0)}를 많이 혼내니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"주변에서 누가 가장 {wm.word(self.user_name, 0)}를 많이 혼내니?",
                                   neu_bhv="do_explain_B", neu="괜찮아~ 말하기 어려울 수 있어~")

        cm.tts(bhv="do_question_S", string="혼내는 사람의 마음도 속상할까? ")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="혼내는 사람의 마음도 속상할까? ",
                                   pos_bhv="do_agree", pos="혼내는 사람도 속상할 것 같아.",
                                   neu_bhv="do_explain_C", neu="몰라도 괜찮아~",
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
    sol.Upset2()