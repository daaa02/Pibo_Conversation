# -*- coding: utf-8 -*-

# 문제해결-친구들과 장난감 가지고 놀고 싶어

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
                
        
    def Toy(self):
        
        # 1.1 문제 제시
        cm.tts(bhv="do_sad", string="친구들이랑 싸우지 않고 사이좋게 장난감을 가지고 놀고 싶어.")
        
        # 1.2 경험 질문
        cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}는 친구들이랑 어떤 장난감을 가지고 놀 때 제일 재밌니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}는 친구들이랑 어떤 장난감을 가지고 놀 때 제일 재밌니?",
                                   neu_bhv="do_agree", neu="괜찮아~ 생각이 나지 않을 수 있어~")
        
        cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)} 친구들은 장난감을 잘 양보해주니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)} 친구들은 장난감을 잘 양보해주니?",
                                   pos_bhv="do_joy_B", pos=f"{wm.word(self.user_name, 0)}는 멋진 친구들이 있구나!")
            
        cm.tts(bhv="do_question_L", string=f"다른 친구만 계속 장난감을 가지고 놀면 {wm.word(self.user_name, 0)}의 기분이 어때?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"다른 친구만 계속 장난감을 가지고 놀면 {wm.word(self.user_name, 0)}의 기분이 어때?",
                                   pos_bhv="do_agree", pos="나도 그렇게 생각해!",
                                   neu_bhv="do_explain_A", neu=f"괜찮아~ 바로 떠오르지 않을 수 있어~ {wm.word(self.user_name, 0)}의 기분이 속상하지 않았을까?",
                                   neg_bhv="do_agree", neg="나도 그렇게 생각해!",
                                   act_bhv="do_agree", act="나도 그렇게 생각해!")
            
        cm.tts(bhv="do_question_S", string="장난감을 혼자서만 가지고 놀면 친구들이 싫어하겠지?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="장난감을 혼자서만 가지고 놀면 친구들이 싫어하겠지?",
                                   pos_bhv="do_agree", pos="같이 가지고 놀면 더 재미있을 것 같아!",
                                   neu_bhv="do_explain_B", neu="괜찮아~ 모를 수도 있어~ 그런데, 같이 가지고 놀면 더 재미있을 것 같아!",
                                   neg_bhv="do_agree", neg="같이 가지고 놀면 더 재미있을 것 같아!",
                                   act_bhv="do_agree", act="같이 가지고 놀면 더 재미있을 것 같아!")
            
        cm.tts(bhv="do_question_S", string="혼자 장난감을 가지고 노는 친구에게 뭐라고 말하는게 좋을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="혼자 장난감을 가지고 노는 친구에게 뭐라고 말하는게 좋을까?",
                                   neu_bhv="do_explain_C", neu="괜찮아~ 말하기 어려울 수 있어~ 같이 놀자~ 라고 말해보면 어떨까?")
         
        cm.tts(bhv="do_question_L", string="장난감을 친구들이랑 사이좋게 가지고 노는 방법은 뭘까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="장난감을 친구들이랑 사이좋게 가지고 노는 방법은 뭘까?",
                                   pos_bhv="do_agree", pos="서로 양보하면 사이좋게 놀 수 있겠다!",
                                   neu_bhv="do_explain_A", neu="찮아~ 생각이 나지 않을 수 있어~ 서로 양보하면 사이좋게 놀 수 있겠지?",
                                   act_bhv="do_agree", act="서로 양보하면 사이좋게 놀 수 있겠다!")
        
        
        # 2.1 문제 해결
        cm.tts(bhv="do_joy_A", string="파이보도 이제는 친구들이랑 장난감을 가지고 놀 땐 다른 친구들도 생각하면서 재밌게 잘 놀아야 겠다~ 알려줘서 정말 고마워!")
                            
        
        
        
if __name__ == "__main__":
    
    sol = Solution()
    sol.Toy()