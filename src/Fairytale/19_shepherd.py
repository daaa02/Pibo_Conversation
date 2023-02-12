# -*- coding: utf-8 -*-

# 동화-양치기 소년과 늑대

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
        self.user_name = '가영'
                
        
    def Shepherd(self):
        
        # 1. 동화 줄거리 대화        
        cm.tts(bhv="do_joy_A", string=f"정말 재미있는 이야기였어! {wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?")
        answer = cm.responses_proc(re_bhv="do_joy_A", re_q=f"{wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?",
                                   neu_bhv="do_agree", neu=f"그럴 수 있지~")
        
        cm.tts(bhv="do_question_S", string=f"양치기 소년은 양들을 돌볼 때 힘들겠지?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"양치기 소년은 양들을 돌볼 때 힘들겠지?")
        
        cm.tts(bhv="do_question_S", string=f"양치기 소년이 돌보는 양은 몇 마리 일지 상상해볼까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"양치기 소년이 돌보는 양은 몇 마리 일지 상상해볼까?",
                                   neu_bhv="do_agree", neu=f"몰라도 괜찮아~")
        
        cm.tts(bhv="do_question_S", string=f"그 많은 양들은 풀을 얼마나 먹을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"그 많은 양들은 풀을 얼마나 먹을까?")

        # 2. 등장인물 공감 대화        
        cm.tts(bhv="question_S", string=f"양치기 소년에게 속은 마을 사람들은 화가 났을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"양치기 소년에게 속은 마을 사람들은 화가 났을까?", 
                                   pos_bhv="do_question_S", pos=f"{wm.word(self.user_name, 0)}도 최근에 속아서 화가 난 적이 있다면 말해 줄 수 있니?",
                                   act_bhv="do_question_S", act=f"{wm.word(self.user_name, 0)}도 최근에 속아서 화가 난 적이 있다면 말해 줄 수 있니?")

        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}도 최근에 속아서 화가 난 적이 있다면 말해 줄 수 있니?",
                                       neu_bhv="do_agree", neu=f"괜찮아~ 생각 나지 않을 수 있어~", 
                                       act_bhv="do_sad", act=f"정말 화가 났었겠구나!")
            
        cm.tts(bhv="question_S", string=f"거짓말을 한 양치기 소년은 후회했을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"거짓말을 한 양치기 소년은 후회했을까?", 
                                   pos_bhv="do_question_S", pos=f"{wm.word(self.user_name, 0)}도 최근에 후회 한 적이 있다면 말해줄래?", 
                                   neu_bhv="do_agree", neu=f"괜찮아~ 생각 나지 않을 수 있어~", 
                                   act_bhv="do_question_S", act=f"{wm.word(self.user_name, 0)}도 최근에 후회 한 적이 있다면 말해줄래?")

        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}도 최근에 후회 한 적이 있다면 말해줄래?",
                                       pos_bhv="do_sad", pos=f"속상했겠다.",
                                       act_bhv="do_sad", act=f"속상했겠다.")        
            
        # 3. 마무리 대화    
        cm.tts(bhv="do_question_L", string=f"자꾸 거짓말을 하는 양치기 소년에게 뭐라고 해주고 싶니?")
        answer = cm.responses_proc(re_bhv="do_question_L", string=f"자꾸 거짓말을 하는 양치기 소년에게 뭐라고 해주고 싶니?",  
                                   pos_bhv="do_agree", pos=f"그렇구나!",
                                   neu_bhv="do_agree", neu=f"괜찮아~ 모를 수 있지~ ",
                                   neg_bhv="do_agree", neg=f"그렇구나!",
                                   act_bhv="do_agree", act=f"그렇구나!")
        
        cm.tts(bhv="do_explain_C", string=f"오늘 동화 재미있었지? 다음에 또 재미있는 동화를 들려줄게~")
        
        
        
        
if __name__ == "__main__":    
    
    fat = Fairytale()
    fat.Shepherd()
