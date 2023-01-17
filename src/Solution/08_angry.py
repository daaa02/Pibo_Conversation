# -*- coding: utf-8 -*-

# 문제해결-화를 참을 수 없어

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
                
        
    def Angry(self):
        
        # 1.1 문제 제시
        cm.tts(bhv="do_sad", string="요즘 자꾸 화가 나고, 화를 참을 수가 없어.")
        
        # 1.2 경험 질문
        cm.tts(bhv="do_sad", string=f"{wm.word(self.user_name, 0)}는 어떻게 화를 참니?")
        answer = cm.responses_proc(re_bhv="do_sad", re_q=f"{wm.word(self.user_name, 0)}는 어떻게 화를 참니?",
                                   pos_bhv="do_compliment_S", pos="대단한 걸?")    
    
        cm.tts(bhv="do_question_L", string="화가 날때 화를 참으면 어떤 점이 좋을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="화가 날때 화를 참으면 어떤 점이 좋을까?",
                                   pos_bhv="do_agree", pos="친구들이랑 덜 싸울 수 있겠지?",
                                   neu_bhv="do_explain_A", neu="괜찮아~ 모를 수도 있어~ 화를 참으면 친구들이랑 덜 싸울 수 있겠지?",
                                   act_bhv="do_agree", act="친구들이랑 덜 싸울 수 있겠지?")

        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}는 친구가 화를 내면 어떻게 행동하니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}는 친구가 화를 내면 어떻게 행동하니?",
                                   pos_bhv="do_sad", pos="친구가 화를 내면 무서울 것 같아.",
                                   neu_bhv="do_explain_B", neu="괜찮아~ 생각이 나지 않을 수 있어~ 친구가 화를 내면 무서울 것 같아.",
                                   act_bhv="do_sad", act="친구가 화를 내면 무서울 것 같아.")

        cm.tts(bhv="do_question_S", string="파이보가 계속 화를내면 친구들이 무섭게 생각할까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="파이보가 계속 화를내면 친구들이 무섭게 생각할까?",
                                   pos_bhv="do_agree", pos="친구들도 무서워하겠지?",
                                   neu_bhv="do_explain_C", neu="괜찮아~ 상상하기 어려울 수 있어~ 아마 친구들도 무서워하겠지?",
                                   act_bhv="do_agree", act="친구들도 무서워하겠지?")
            
        cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}는 어떤 놀이를 하면 기분 좋아지니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}는 어떤 놀이를 하면 기분 좋아지니?")
        
        cm.tts(bhv="do_question_L", string="화가 날 때 재미있는 놀이를 하면 기분이 좋아질까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="화가 날 때 재미있는 놀이를 하면 기분이 좋아질까?",
                                   pos_bhv="do_agree", pos="기분이 좋아질수도 있겠다~",
                                   neu_bhv="do_agree", neu="괜찮아~ 상상하기 어려울 수 있어~ 재미있는 놀이를 하면 기분이 좋아질수도 있겠다~",
                                   act_bhv="do_agree", act="기분이 좋아질수도 있겠다~")
        # 2.1 문제 해결
        cm.tts(bhv="do_joy_A", string="파이보도 이제 화를 잘 참을 수 있도록 노력해야겠다~ 알려줘서 정말 고마워!")
                            
        
        
        
if __name__ == "__main__":
    
    sol = Solution()
    sol.Angry()