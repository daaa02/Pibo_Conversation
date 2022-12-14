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
                                   neu_bhv="do_agree", neu="괜찮아~ 생각이 나지 않을 수 있어~")
            
        cm.tts(bhv="do_question_L", string=f"다른 사람들이 {wm.word(self.user_name, 0)}의 마음을 몰라줄 때 어떤 마음이 들었니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"다른 사람들이 {wm.word(self.user_name, 0)}의 마음을 몰라줄 때 어떤 마음이 들었니?",
                                   neu_bhv="do_agree", neu="괜찮아~ 대답하기 어려울 수 있어~",
                                   act_bhv="do_sad", act="나는 속상해서 눈물이 났어.")

        cm.tts(bhv="do_question_S", string="속상한 마음을 다른 사람에게 말하는 게 좋을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"주변에서 누가 가장 {wm.word(self.user_name, 0)}를 많이 혼내니?",
                                   pos_bhv="do_agree", pos="그렇게 생각하는구나!",
                                   neu_bhv="do_agree", neu="그렇게 생각하는구나!",
                                   neg_bhv="do_agree", neg="그렇게 생각하는구나!",
                                   act_bhv="do_agree", act="그렇게 생각하는구나!")

        cm.tts(bhv="do_question_L", string="다른사람에게 속상한 마음을 말한다면 어떻게 말해야 할까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="다른사람에게 속상한 마음을 말한다면 어떻게 말해야 할까?",
                                   pos_bhv="do_agree", pos="천천히 울지않고 말해야 겠지?",
                                   neu_bhv="do_explain_C", neu="괜찮아~ 모를 수도 있어~ 천천히 울지않고 말하면 좋지 않을까?",
                                   act_bhv="do_agree", act="천천히 울지않고 말해야 겠지?")
        
        cm.tts(bhv="do_question_L", string="속상할 땐 어떻게 해야 기분이 나아질까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="속상할 땐 어떻게 해야 기분이 나아질까?",
                                   neu_bhv="do_agree", neu="괜찮아~ 생각이 나지 않을 수 있어~")
        
        if answer[0] != "negative":
        
            cm.tts(bhv="do_question_S", string="또 다른 방법은 뭐가 있을까?")
            answer = cm.responses_proc(re_bhv="do_question_L", re_q="또 다른 방법은 뭐가 있을까?",
                                    pos_bhv="do_joy_B", pos="기분이 좋아질 것 같아!",
                                    neu_bhv="do_agree", neu="괜찮아~ 생각이 나지 않을 수 있어~",
                                    act_bhv="do_joy_B", act="기분이 좋아질 것 같아!")
        
        # 2.1 문제 해결
        cm.tts(bhv="do_joy_A", string="파이보도 혼나고 나서 기분이 좋아지도록 노력해야겠다~ 알려줘서 정말 고마워!")
                            
        
        
        
if __name__ == "__main__":
    
    sol = Solution()
    sol.Upset2()