# -*- coding: utf-8 -*-

# 문제해결-차례를 기다리기 어려워

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
                
        
    def Sequence(self):
        
        # 1.1 문제 제시
        cm.tts(bhv="do_sad", string="여러 사람들이랑 있을 때 차례를 기다리기가 어려워.")
        
        # 1.2 경험 질문
        cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}도 차례를 지키는게 어려울 때가 있니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}도 차례를 지키는게 어려울 때가 있니?",
                                   pos_bhv="do_agree", pos="나랑 비슷하구나!",
                                   neg_bhv="do_compliment_S", neg=f"{wm.word(self.user_name, 0)} 대단한 걸?")
            
        cm.tts(bhv="do_question_L", string="선생님께서 버스에 탈 때는 차례를 지켜야 한다고 했어. 우리는 언제 또 차례를 지켜야 할까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="선생님께서 버스에 탈 때는 차례를 지켜야 한다고 했어. 우리는 언제 또 차례를 지켜야 할까?",
                                   pos_bhv="do_agree", pos="차례를 지켜야 할 때가 많구나!",
                                   neu_bhv="do_agree", neu="괜찮아~ 모를 수도 있어~",
                                   act_bhv="do_agree", act="차례를 지켜야 할 때가 많구나!")
            
        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}는 차례를 지키지 않는 사람을 본 적 있니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}는 차례를 지키지 않는 사람을 본 적 있니?",
                                   pos_bhv="do_agree", pos=f"{wm.word(self.user_name, 0)} 주변에도 있구나!",
                                   neu_bhv="do_agree", neu=f"{wm.word(self.user_name, 0)} 주변 사람들은 차례를 잘 지키는구나!")
            
        cm.tts(bhv="do_question_S", string="순서를 기다리지 않으면 다른 사람들이 화를 낼까? ")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="순서를 기다리지 않으면 다른 사람들이 화를 낼까? ",
                                   pos_bhv="do_agree", pos="기다리는 사람들은 화가 날 것 같아.",
                                   neu_bhv="do_explain_B", neu="괜찮아~ 바로 떠오르지 않을 수 있어. 아마 기다리는 사람들은 화가 나겠지?",
                                   act_bhv="do_agree", act="기다리는 사람들은 화가 날 것 같아.")
        
        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}는 차례를 기다리는 시간이 지루하지는 않니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}는 차례를 기다리는 시간이 지루하지는 않니?")
        
        cm.tts(bhv="do_question_L", string="어떻게 하면 기다리는 시간이 빨리 갈까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="어떻게 하면 기다리는 시간이 빨리 갈까?",
                                   pos_bhv="do_agree", pos="또, 노래를 들어도 시간이 빨리가겠다!",
                                   neu_bhv="do_suggestion_S", neu="괜찮아~ 생각이 나지 않을 수 있어~ 노래를 들으면 시간이 빨리갈 것 같아!",
                                   act_bhv="do_agree", act="또, 노래를 들어도 시간이 빨리가겠다!")
        
        
        # 2.1 문제 해결
        cm.tts(bhv="do_joy_A", string="파이보도 이제 차례를 잘 지키도록 노력해야겠다~ 알려줘서 정말 고마워!")
                            
        
        
        
if __name__ == "__main__":
    
    sol = Solution()
    sol.Sequence()