# -*- coding: utf-8 -*-

# 문제해결-소리지르고 싶어

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
                
        
    def Shout(self):
        
        # 1.1 문제 제시
        cm.tts(bhv="do_sad", string="요즘 자꾸 시끄럽게 소리를 지르게 돼.")
        
        # 1.2 경험 질문
        cm.tts(bhv="do_sad", string=f"{wm.word(self.user_name, 0)}도 평소에 소리를 지르니?")
        answer = cm.responses_proc(re_bhv="do_sad", re_q=f"{wm.word(self.user_name, 0)}도 평소에 소리를 지르니?",
                                   pos_bhv="do_agree", pos="파이보랑 비슷하네!")    

        cm.tts(bhv="do_question_L", string="소리를 계속 지르면 목이 아파지지 않을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="소리를 계속 지르면 목이 아파지지 않을까?",
                                   pos_bhv="do_agree", pos="계속 소리를 지르면 아플 것 같아.",
                                   neu_bhv="do_agree", neu="괜찮아~ 모를 수도 있어~ 계속 소리를 지르면 아플 것 같아.",
                                   act_bhv="do_agree", act="계속 소리를 지르면 아플 것 같아.",)

        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)} 주변에 소리를 지르는 친구가 있니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)} 주변에 소리를 지르는 친구가 있니?",
                                   pos_bhv="do_explain_A", pos="그 친구도 파이보랑 비슷하네!")

        cm.tts(bhv="do_question_S", string="소리를 지르면 주변 사람들이 안좋게 생각할까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="소리를 지르면 주변 사람들이 안좋게 생각할까?",
                                   pos_bhv="do_agree", pos="시끄럽다고 생각하겠지?",
                                   neu_bhv="do_agree", neu="괜찮아~ 상상하기 어려울 수 있어~ 아마 사람들이 시끄럽다고 생각하겠지?",
                                   act_bhv="do_agree", act="시끄럽다고 생각하겠지?")
            
        cm.tts(bhv="do_question_S", string="그럼 소리를 지르는 대신 어떻게 말하는 것이 좋을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="그럼 소리를 지르는 대신 어떻게 말하는 것이 좋을까?",
                                   pos_bhv="do_explain_B", pos="낮은 목소리로 또박또박 말하면 좋겠지?",
                                   neu_bhv="do_explain_B", neu="괜찮아~ 생각이 나지 않을 수 있어. 소리를 지르는 대신 낮은 목소리로 또박또박 말하면 좋겠지?",
                                   act_bhv="do_explain_B", act="낮은 목소리로 또박또박 말하면 좋겠지?")
        
        cm.tts(bhv="do_question_L", string="소리를 지르는 친구한테는 뭐라고 말하면 좋을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="소리를 지르는 친구한테는 뭐라고 말하면 좋을까?",
                                   pos_bhv="do_explain_C", pos="조금 조용히 말해볼까? 라고 말해도 좋을 것 같아~",
                                   neu_bhv="do_explain_C", neu="괜찮아~ 대답하기 어려울 수 있어~ 조금 조용히 말해볼까? 라고 말해도 좋을 것 같아~",
                                   act_bhv="do_explain_C", act="조금 조용히 말해볼까? 라고 말해도 좋을 것 같아~")
        # 2.1 문제 해결
        cm.tts(bhv="do_joy_A", string="파이보도 이제 소리 지르지 않아야겠다~ 알려줘서 정말 고마워!")
                            
        
        
        
if __name__ == "__main__":
    
    sol = Solution()
    sol.Shout()