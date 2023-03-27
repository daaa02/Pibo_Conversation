# -*- coding: utf-8 -*-

# 문제해결-속마음을 말하기가 어려워

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
                
        
    def Mind(self):
        
        # 1.1 문제 제시
        cm.tts(bhv="do_sad", string="파이보는 다른 사람한테 속마음을 말하기가 어려워.")
        
        # 1.2 경험 질문
        cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}의 속마음을 다른 사람에게 말한 적 있니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}의 속마음을 다른 사람에게 말한 적 있니?",
                                   pos_bhv="do_question_S", pos="말하고 나니까 기분이 어땠니?")                
    
        if answer[0][0] == "positive":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q="말하고 나니까 기분이 어땠니?",
                                       pos_bhv="do_agree", pos="속마음을 말하면 마음이 편해질수도 있겠지?",
                                       act_bhv="do_agree", act="속마음을 말하면 마음이 편해질수도 있겠지?")
            

        cm.tts(bhv="do_question_L", string=f"나는 속마음이 10개정도 있는 것 같아. {wm.word(self.user_name, 0)}는 속마음이 얼마나 많니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"나는 속마음이 10개정도 있는 것 같아. {wm.word(self.user_name, 0)}는 속마음이 얼마나 많니?",
                                   neu_bhv="do_agree", neu="괜찮아~ 바로 떠오르지 않을 수 있어~")
        
        cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}도 속마음을 말하기 어려울 때가 있니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}도 속마음을 말하기 어려울 때가 있니?",
                                   pos_bhv="do_agree", pos=f"나는 속마음을 말로 표현하기 어려운 것 같아. {wm.word(self.user_name, 0)}는 언제 말하기가 어렵니?",
                                   neg_bhv="do_agree", neg=f"파이보는 잘 못하는데, {wm.word(self.user_name, 0)} 정말 대단한 걸?")
        
        if answer[0][0] =="positive":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"나는 속마음을 말로 표현하기 어려운 것 같아. {wm.word(self.user_name, 0)}는 언제 말하기가 어렵니?",
                                       neu_bhv="do_agree", neu="괜찮아~ 대답하기 어려울 수 있어~")
        
        cm.tts(bhv="do_question_L", string="속마음을 계속 말하지 않으면 어떻게 될까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}가 친구의 물건을 마음대로 만지면 친구의 기분을 어떨까?",
                                   pos_bhv="do_agree", pos="마음이 힘들어 지겠지?",
                                   neg_bhv="do_agree", neg="마음이 힘들어 지겠지?",
                                   act_bhv="do_agree", act="마음이 힘들어 지겠지?")
        
        cm.tts(bhv="do_question_S", string="나의 속마음을 언제 이야기하는 것이 좋을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="나의 속마음을 언제 이야기하는 것이 좋을까?",
                                   pos_bhv="do_agree", pos="그렇게 생각하는구나!",                                   
                                   neu_bhv="do_suggestion_S", neu="괜찮아~ 모를 수도 있어~  속상한 날에는 나에게 꼭 말해줘~",
                                   neg_bhv="do_agree", neg="그렇게 생각하는구나!",
                                   act_bhv="do_agree", act="그렇게 생각하는구나!")
        
        # 2.1 문제 해결
        cm.tts(bhv="do_joy_A", string="파이보도 이제 속마음을 잘 표현할 수 있도록 노력해야겠다~ 알려줘서 정말 고마워!")
                            
        
        
        
if __name__ == "__main__":
    
    sol = Solution()
    sol.Mind()