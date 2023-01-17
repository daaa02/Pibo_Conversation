# -*- coding: utf-8 -*-

# 문제해결-고맙다고 말하기 어려워

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
                
        
    def Thanks(self):
        
        # 1.1 문제 제시
        cm.tts(bhv="do_sad", string="파이보는 다른 사람에게 고맙다고 말하기가 어려워. ")
        
        # 1.2 경험 질문
        cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}는 친구에게 고마운 마음을 표현한 적 있니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}는 친구에게 고마운 마음을 표현한 적 있니?",
                                   pos_bhv="do_question_S", pos=f"어떤 말로 {wm.word(self.user_name, 0)}의 마음을 표현했니?")                
    
        if answer[0] == "positive":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"어떤 말로 {wm.word(self.user_name, 0)}의 마음을 표현했니?",
                                       neu_bhv="do_agree", neu=" 괜찮아~ 바로 떠오르지 않을 수 있어~")
            
        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}도 고맙다고 말하기 어려울 때가 있니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}도 고맙다고 말하기 어려울 때가 있니?",
                                   pos_bhv="do_explain_A", pos="난 고맙다고 말하기가 쑥스러워",
                                   neu_bhv="do_explain_A", neu="난 고맙다고 말하기가 쑥스러워",
                                   neg_bhv="do_compliment_S", neg="대단한 걸?")
            
        cm.tts(bhv="do_question_S", string=f"친구가 {wm.word(self.user_name, 0)}에게 고맙다고 하면 어떤 마음이 드니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"친구가 {wm.word(self.user_name, 0)}에게 고맙다고 하면 어떤 마음이 드니?",
                                   pos_bhv="do_agree", pos="나도 같은 마음이 들어!",
                                   neu_bhv="do_agree", neu="괜찮아~ 생각이 나지 않을 수 있어~",
                                   act_bhv="do_agree", act="나도 같은 마음이 들어!")
            
        cm.tts(bhv="do_question_S", string="고맙다고 말해야 할 때는 언제라고 생각하니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="고맙다고 말해야 할 때는 언제라고 생각하니?",
                                   pos_bhv="do_agree", pos="그렇게 생각하는구나!",
                                   neu_bhv="do_agree", neu="괜찮아~ 말하기 어려울 수 있어~ 친구에게 도움을 받을 때 고맙다고 말하면 좋겠지?",
                                   act_bhv="do_agree", act="그렇게 생각하는구나!")
        
        cm.tts(bhv="do_question_L", string="그런데, 고맙다고 말을 안하면 친구들이 내 마음을 알 수 있을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="그런데, 미안하다고 말을 안 하면 친구들이 나의 미안한 마음을 알 수 있을까?",
                                   pos_bhv="do_explain_B", pos="아마 친구들이 알기 어렵겠지?",
                                   neu_bhv="do_explain_B", neu="아마 친구들이 알기 어렵겠지?",
                                   act_bhv="do_agree", act="나도 그렇게 생각해!")
        
        cm.tts(bhv="do_question_L", string="어떻게 하면 나의 고마운 마음을 잘 전달할 수 있을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="어떻게 하면 나의 고마운 마음을 잘 전달할 수 있을까?",
                                   pos_bhv="do_agree", pos="나도 그렇게 생각해!",
                                   neu_bhv="do_suggestion_S", neu="괜찮아~ 모를 수 있어~ 예쁜 편지를 적어봐도 좋을 것 같아!",
                                   act_bhv="do_agree", act="나도 그렇게 생각해!")
        
        
        # 2.1 문제 해결
        cm.tts(bhv="do_joy_A", string="파이보도 이제 다른 사람들에게 고맙다고 잘 표현할 수 있도록 노력해야겠다~ 알려줘서 정말 고마워!")
                            
        
        
        
if __name__ == "__main__":
    
    sol = Solution()
    sol.Thanks()