# -*- coding: utf-8 -*-

# 동화-개미와 베짱이

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


class Fairytale():
        
    def __init__(self): 
        self.user_name = '다영'
        
    
    def Ants(self):      
        # 1. 동화 줄거리 대화  
        cm.tts(bhv="do_joy_A", string=f"정말 재미있는 이야기였어! {wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?")
        answer = cm.responses_proc(re_bhv="do_joy_A", re_q=f"{wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?",
                                   neu_bhv="do_agree", neu=f"그럴 수 있지~")
             
        cm.tts(bhv="do_question_S", string=f"개미들은 겨울을 준비하기 위해 어떤 일을 했을 것 같니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"개미들은 겨울을 준비하기 위해 어떤 일을 했을 것 같니?", 
                                   neu_bhv="do_agree", neu=f"모를 수 있지~")
        
        cm.tts(bhv="do_question_S", string=f"개미들은 어떤 먹이를 모았을 것 같니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"개미들은 어떤 먹이를 모았을 것 같니?", 
                                   neu_bhv="do_agree", neu=f"몰라도 괜찮아~")
        
        cm.tts(bhv="do_question_L", string=f"베짱이는 좋아하는 노래를 부르며 놀았을 것 같아! {wm.word(self.user_name, 0)}가 좋아하는 노래는 어떤 노래니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}가 좋아하는 노래는 어떤 노래니?", 
                                   pos_bhv="do_agree", pos=f"그 노래를 좋아하는구나!")
            
        # 2. 등장인물 공감 대화   
        cm.tts(bhv="do_question_S", string=f"추운 겨울 먹을 것이 없던 베짱이는 후회했을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"추운 겨울 먹을 것이 없던 베짱이는 후회했을까?", 
                                   pos_bhv="do_question_S", pos=f"{wm.word(self.user_name, 0)}이도 후회한 적이 있다면 말해줄래?",
                                   neu_bhv="do_agree", neu=f"몰라도 괜찮아~",
                                   neg_bhv="do_question_S", neg=f"{wm.word(self.user_name, 0)}도 후회한 적이 있다면 말해줄래?",
                                   act_bhv="do_question_S", act=f"{wm.word(self.user_name, 0)}도 후회한 적이 있다면 말해줄래?")
        
        if answer[0] != "neutral": 
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}이도 후회한 적이 있다면 말해줄래?")
            
        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}가 개미라면 겨울에 베짱이에게 먹을 것을 나눠줬을 것 같니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}가 개미라면 겨울에 베짱이에게 먹을 것을 나눠줬을 것 같니?", 
                                   pos_bhv="do_agree", pos=f"그럴 수 있겠구나!",
                                   neg_bhv="do_agree", neg=f"그럴 수 있겠구나!",
                                   act_bhv="do_agree", act=f"그럴 수 있겠구나!")

        # 3. 마무리 대화
        cm.tts(bhv="do_suggestion_S", string=f"열심히 일한 개미에게 칭찬을 해볼까?")
        answer = cm.responses_proc(re_bhv="do_suggestion_S", re_q=f"열심히 일한 개미에게 칭찬을 해볼까?", 
                                   pos_bhv="do_agree", pos=f"정말 잘 하는 걸~?", 
                                   neu_bhv="do_agree", neu=f"괜찮아~ 모를 수 있지~", 
                                   act_bhv="do_agree", act=f"정말 잘 하는 걸~?")
        
        cm.tts(bhv="do_explain_C", string=f"다음에 또 재미있는 동화 들려줄게~")
            

if __name__ == "__main__":
    fat = Fairytale()
    fat.Ants()