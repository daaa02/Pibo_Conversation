# -*- coding: utf-8 -*-

# 역할놀이-부모님

import os, sys
import re
import time
import random

sys.path.append('/home/kiro/workspace/Conversation_Scenarios/')
from data.conversation_manage import ConversationManage, WordManage
from data.speech_to_text import speech_to_text
from data.text_to_speech import TextToSpeech, text_to_speech

cm = ConversationManage()
wm = WordManage()
audio = TextToSpeech()


class Roleplay():    
    
    def __init__(self): 
        self.user_name = '다영'
        self.role=''
        self.count = 0
        
    
    def Teacher(self):      # 이 시나리오 미완성인듯
        
        # 1. 역할 알림
        cm.tts(bhv="do_suggestion_S", string="역할 놀이를 해볼까?")
        cm.tts(bhv="do_suggestion_S", string=f"오늘은 유치원 선생님이 되어 보는거야~") 
                
        # 2. 역할 놀이
        cm.tts(bhv="do_explain_A", string="파이보가 유치원 선생님이 된다면  아침에 어린이들에게 인사를 하면서 꼭 안아줄거야.")
        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}가 유치원 선생님이 된다면 어린이들에게 어떻게 인사를 해주고 싶니?")
        
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}가 유치원 선생님이 된다면 어린이들에게 어떻게 인사를 해주고 싶니?",
                                   pos_bhv="do_question_S", pos="친구들에게 왜 그렇게 인사해 주고 싶니?",
                                   neu_bhv="do_agree", neu="몰라도 괜찮아~",
                                   act_bhv="do_question_S", act="친구들에게 왜 그렇게 인사해 주고 싶니?")
        
        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_L", re_q="친구들에게 왜 그렇게 인사해 주고 싶니?",
                                       neu_bhv="do_agree", neu="괜찮아~ 대답하기 어려울 수 있어~")
        
        # 3. 대화 시작
        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}가 유치원 선생님이라면 물건을 뺏는 친구들에게 뭐라고 말해주고 싶니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}가 유치원 선생님이라면 물건을 뺏는 친구들에게 뭐라고 말해주고 싶니?",
                                   neu_bhv="do_agree", neu="괜찮아~ 생각이 나지 않을 수 있어~")
        
        cm.tts(bhv="do_question_L", string="최근에 물건을 뺏는 친구들을 본 적이 있었니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="최근에 물건을 뺏는 친구들을 본 적이 있었니?",
                                   pos_bhv="do_question_S", pos="어떤 상황이었는지 나에게 말해 줄 수 있니?")
        
        if answer[0] == "positive":
            cm.tts(bhv="do_sad", string="어떤 상황이었는지 나에게 말해줄 수 있니? ")
            answer = cm.responses_proc(re_bhv="do_sad", re_q="어떤 상황이었는지 말해줄 수 있니?")
            
        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}가 유치원 선생님이라면 싸우고 있는 친구들을 어떻게 화해 시킬 것 같니?")
        
        
        # 4. 마무리 대화
        cm.tts(bhv="do_joy_B", string=f"{wm.word(self.user_name, 0)}와 유치원 선생님 놀이를 해서 너무 재미있었어~ 유치원에서 있었던 다양한 일들을 나에게 또 말해줘!")




if __name__ == "__main__":
    
    rop = Roleplay()
    rop.Teacher()