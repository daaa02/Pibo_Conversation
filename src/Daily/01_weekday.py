# -*- coding: utf-8 -*-

# 일상-귀가 후 요일 대화 시나리오
# -*- coding: utf-8 -*-

# 일상-자기 전 감정 대화

import os, sys
import re
import random
import time
import datetime

# sys.path.append('/home/kiro/workspace/Conversation_Scenarios/')
sys.path.append('/home/pi/Pibo_Conversation/')
from data.conversation_manage import ConversationManage, WordManage
from data.speech_to_text import speech_to_text
from data.text_to_speech import TextToSpeech, text_to_speech

cm = ConversationManage()
wm = WordManage()
audio = TextToSpeech()


class Daily():    
    
    def __init__(self): 
        self.user_name = "윤지"
        self.today = 2 # datetime.now().weekday()
        self.place = '유치원'
    
    
    def Weekday(self):
        
        # if self.today == 0: # 월요일
        
        # if self.today == 1: # 화요일
            
        if self.today == 2: # 수요일
            cm.tts(bhv="do_question_S", string=f"안녕 {wm.word(self.user_name, type=4)}, {self.place} 잘 다녀왔니?")
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{self.place} 잘 다녀왔니?",
                                       pos_bhv="do_joy_A", pos="")
            
            cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, type=0)}가 {self.place}에서 어떤 걸 배웠는지 궁금한 걸?")
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, type=0)}이가 {self.place}에서 어떤 걸 배웠는지 궁금한 걸?",
                                       pos_bhv="do_joy_A", pos="정말 새로운 걸?",
                                       act_bhv="do_joy_A", act="정말 새로운 걸?")
                                       
            cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, type=0)}는 어떤 활동 할 때가 가장 재밌었는지 말해 줄래?")
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, type=0)}는 어떤 활동 할 때가 가장 재밌었는지 말해 줄래?",
                                       pos_bhv="do_question_S", pos="그 활동을 언제 했니?",
                                       act_bhv="do_question_S", act="그 활동을 언제 했니?")
            
            if answer[0] == "postive" or answer[0] == "action":            
                answer = cm.responses_proc(re_bhv="do_question_S", re_q="그 활동을 언제 했니?", 
                                           pos_bhv="do_question_S", pos="어떤 점이 재미있었니?", 
                                           act_bhv="do_question_S", act="어떤 점이 재미있었니?") 
                
                if answer[0] == "postive" or answer[0] == "action":
                    answer = cm.responses_proc(re_bhv="do_question_S", re_q="어떤 점이 재미있었니?",
                                               pos_bhv="do_joy_B", pos="정말 재밌겠는걸?",
                                               act_bhv="do_joy_B", act="정말 재밌겠는걸?")
                
            cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, type=0)}는 {self.place} 가는 게 재밌니?")
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, type=0)}는 {self.place} 가는 게 재밌니?",
                                       pos_bhv="do_joy_A", pos="정말 유치원 생활이 재밌나 보구나!")
            
            cm.tts(bhv="do_question_S", string=f"친구들이나 선생님께 말하기 힘든 일이 있니?")
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"친구들이나 선생님께 말하기 힘든 일이 있니?",
                                       neg_bhv="do_agree", neg=f"정말 {wm.word(self.user_name, type=0)}는 {self.place}에 가는 것을 좋아하는 것 같아!")
            
            if answer[0] != "negative":
                cm.tts(bhv="do_sad", string=f"요즘 {wm.word(self.user_name, type=0)}가 마음이 힘들구나. 최근에 울고 싶었던 적이 있었니?")
                answer = cm.responses_proc(re_bhv="do_question_S", re_q="최근에 울고 싶었던 적이 있었니?",
                                           pos_bhv="do_sad", pos=f"정말 속상했겠다. 언제 울고 싶었는지 말해 줄래?",
                                           neg_bhv="do_question_L", neg="마음이 힘든 이유가 있다면 말해 줄래?")
                
                if answer[0] == "positive":
                    answer = cm.responses_proc(re_bhv="do_question_S", re_bhv="언제 울고 싶었는지 말해 줄래?",
                                               neu_bhv="do_agree", neu=f"{wm.word(self.user_name, type=0)}가 힘들었겠구나. 엄마한테 이야기를 해보는 건 어때?",
                                               act_bhv="do_agree", act=f"{wm.word(self.user_name, type=0)}가 힘들었겠구나. 엄마한테 속마음을 이야기 해보는 건 어때?")

                    time.sleep(1)
                    cm.tts(bhv="do_agree", string="도움이 필요할 수 있을 것 같아. 엄마가 잘 도와주실테니 너무 걱정하지마~")
                    
                if answer[0] == "neutral" or answer[0] == "negative":
                    cm.tts(bhv="do_agree", string=f"속상한 일이 있으면 언제든 나에게 이야기해도 괜찮아!")
            
            cm.tts(bhv="do_joy_A", string=f"내일도 {wm.word(self.user_name, type=0)}가 유치원에서 좋은 하루를 보냈으면 좋겠어~ 내일도 이야기 하자!")
                
                
            
        # if self.today == 3: # 목요일
            
            
        # if self.today == 4: # 금요일
            
        else:
            print("WEEKEND")
            
            
            
            
if __name__ == "__main__":
    day = Daily()
    day.Weekday()
    