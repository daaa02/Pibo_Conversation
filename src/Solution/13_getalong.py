# -*- coding: utf-8 -*-

# 친구랑 친하게 지내고 싶어 시나리오

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
                
                
    def Getalong(self):
        
        # 1.1 문제 제시
        cm.tts(bhv="do_explain_A", string=f"파이보도 친구들이랑 친하게 지내고 싶어.")

        # 1.2 경험 질문        
        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}의 가장 친한 친구 이름은 뭐니? 한 명만 말해봐.")
        answer = cm.responses_proc(re_bhv="do_question_L", string=f"{wm.word(self.user, 0)}의 가장 친한 친구는 누구니?") 
        
        cm.tts(bhv="do_question_S", string=f"그 친구랑 어떻게 친해지게 됐니?")
        answer = cm.responses_proc(re_bhv="do_question_S", string=f"그 친구랑 어떻게 친해지게 됐니?",
                                   neu_bhv="do_agree", neu="괜찮아~ 생각이 나지 않을 수 있어~")
        
        cm.tts(bhv="do_question_S", string=f"그 친구랑 뭐하고 놀 때가 제일 재밌어?")
        answer = cm.responses_proc(re_bhv="do_question_S", string=f"그 친구랑 뭐하고 놀 때가 제일 재밌어?",
                                   pos_bhv="do_agree", pos="그렇게 생각하는구나!",
                                   act_bhv="do_agree", act="그렇게 생각하는구나!")
        
        cm.tts(bhv="do_question_S", string=f"또 친해지고 싶은 친구가 있니?")
        answer = cm.responses_proc(re_bhv="do_question_S", string=f"또 친해지고 싶은 친구가 있니?")

        cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)} 주변에는 어떤 친구들이 인기가 많니?")
        answer = cm.responses_proc(re_bhv="do_question_S", string=f"{wm.word(self.user_name, 0)} 주변에는 어떤 친구들이 인기가 많니?",
                                   pos_bhv="do_agree", pos=f"재미있는 친구들도 인기가 많겠지?",
                                   neu_bhv="do_explain_A", neu=f"괜찮아~ 대답하기 어려울 수 있어. 아마 재미있는 친구들도 인기가 많겠지?",
                                   act_bhv="do_agree", act=f"재미있는 친구들도 인기가 많겠지?")
        
        cm.tts(bhv="do_question_S", string=f"어떻게 하면 새로운 친구와 친해질 수 있을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", string=f"어떻게 하면 새로운 친구와 친해질 수 있을까?",
                                   neu_bhv="do_agree", neu="괜찮아~ 말하기 어려울 수 있어~")
        
        # 2.1 문제 해결
        cm.tts(bhv="do_joy_A", string=f"파이보도 친구들이랑 사이좋게 잘 지내야 겠다~ 알려줘서 정말 고마워!")
    
    
if __name__ == "__main__":
    
    sol = Solution()
    sol.Getalong()