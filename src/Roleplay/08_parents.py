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
        self.time = 5  # 테스트를 위해 5까지만 셈
        self.role=''
        self.count = 0
        
    
    def Parents(self):
        
        # 1. 역할 알림
        cm.tts(bhv="do_suggestion_S", string="역할 놀이를 해볼까?")
        cm.tts(bhv="do_suggestion_S", string=f"오늘은 {wm.word(self.user_name, 0)}가 집의 어른이 되어보자!") 
                
        # 2. 역할 놀이 (1 of 3)     # 2개만 있음
        rand = random.sample(range(1,3), 1)
        
        if rand[0] == 1: 
            self.role = "엄마"
            cm.tts(bhv="do_suggestion_S", string=f"엄마가 되어 {wm.word(self.user_name, 0)}가 장난감 정리를 해보자!")
            cm.tts(bhv="do_suggestion_S", string=f"내가 5분 줄게~ 지금부터 100까지 센다!")
            
            for i in range(1, (self.time+1)):   # 테스트를 위해 10까지만 셈
                text_to_speech(f"{i}")
                time.sleep(2)   # 3초에 1카운트
            
            cm.tts(bhv="do_waiting_A", string="다 되면 다 됐다고 말해줘!")
            answer = cm.responses_proc(re_bhv="do_question_S", re_q="다 되면 다 됐다고 말해줘!",
                                       neu_bhv="do_agree", neu="몰라도 괜찮아~")    # 뭘 모르죠
            
            cm.tts(bhv="do_joy_A", string="정리를 하고 나니 깨끗해진 것 같아!")
        
        if rand[0] == 2:
            self.role = "아빠"
            cm.tts(bhv="do_suggestion_S", string=f"아빠가 되어 아빠가 좋아하는 요리를 만들어 보자!")
            cm.tts(bhv="do_suggestion_S", string=f"내가 3분을 줄게~ 지금부터 만들어보자 시작!")
            
            for i in range(1, (self.time+1)):   # 테스트를 위해 10까지만 셈
                text_to_speech(i)
                time.sleep(2)   # 3초에 1카운트
            
            cm.tts(bhv="do_waiting_A", string="다 되면 다 됐다고 말해줘!")
            answer = cm.responses_proc(re_bhv="do_question_S", re_q="다 되면 다 됐다고 말해줘!",
                                       neu_bhv="do_agree", neu="몰라도 괜찮아~")
            
            cm.tts(bhv="do_joy_A", string="맛있는 냄새가 나는 것 같아!")
        
        # 3. 대화 시작 (3 of 6)     # 4개만 있음
        rand = random.sample(range(1,5), 3)
        
        while True:
            for i in range(len(rand)):
                if rand[i] == 1:                             
                    cm.tts(bhv="do_sad", string=f"우리 {wm.word(self.role, 2)} 나한테 조용히 하라는 말을 제일 많이 해.")
                    cm.tts(bhv="do_question_L", string=f"{wm.word(self.role, 1)} {wm.word(self.user_name, 0)}에게 제일 많이 하는 말은 뭐니?")
                    answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.role, 1)} {wm.word(self.user_name, 0)}에게 제일 많이 하는 말은 뭐니?",
                                               neu_bhv="do_agree", neu="괜찮아~ 생각이 나지 않을 수 있어~",
                                               act_bhv="do_question_S", act=f"그 말을 들을 때 {wm.word(self.user_name, 0)}의 기분은 어떠니?")  
                    
                    if answer[0] == "action":
                        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"그 말을 들을 때 {wm.word(self.user_name, 0)}의 기분은 어떠니?",
                                                   neu_bhv="do_agree", neu=f"괜찮아~ 대답하기 어려울 수 있어~ {wm.word(self.role, 3)}를 흉내내볼까?",
                                                   act_bhv="do_suggestion_S", act=f"{wm.word(self.role, 3)} 흉내내볼까?")
                    
                        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.role, 3)} 흉내내볼까?")                    
                    self.count += 1 

                if rand[i] == 2:                             
                    cm.tts(bhv="do_sad", string=f"{wm.word(self.role, 2)} 하는 말 중에 {wm.word(self.user_name, 0)}가 가장 듣기 싫은 말은 뭐니?")
                    answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.role, 2)} 하는 말 중에 {wm.word(self.user_name, 0)}가 가장 듣기 싫은 말은 뭐니?",
                                               neu_bhv="do_agree", neu="괜찮아~ 대답하기 어려울 수 있어~",
                                               act_bhv="do_sad", act=f"{wm.word(self.user_name, 0)}가 속상했겠다.")  
                    
                    if answer[0] == "action":
                        cm.tts(bhv="do_question_L", string=f"{wm.word(self.role, 2)} 어떻게 말하면 {wm.word(self.user_name, 0)}가 덜 속상할까?")
                        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.role, 2)} 어떻게 말하면 {wm.word(self.user_name, 0)}가 덜 속상할까?",
                                                   neu_bhv="do_agree", neu="괜찮아~ 생각이 나지 않을 수 있어~",
                                                   act_bhv="do_agree", act="그것도 좋은 방법이야!")
                    self.count += 1 
                    
                if rand[i] == 3:                             
                    cm.tts(bhv="do_sad", string=f"{wm.word(self.user_name, 0)}가 {wm.word(self.role, 0)}에게 가장 화가 났던 때는 언제였어?")
                    answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.role, 2)} 하는 말 중에 {wm.word(self.user_name, 0)}가 가장 듣기 싫은 말은 뭐니?",
                                               neu_bhv="do_agree", neu="괜찮아~ 대답하기 어려울 수 있어~",
                                               act_bhv="do_question_S", act="자세히 이야기해 줄래?")  
                    
                    if answer[0] == "action":
                        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"자세히 이야기해 줄래?",
                                                   neu_bhv="do_agree", neu="괜찮아~ 대답하기 어려울 수 있어~",
                                                   act_bhv="do_agree", act=f"{wm.word(self.user_name, 0)}의 기분이 안 좋았겠다.")
                    self.count += 1 
                      
                if rand[i] == 4:                             
                    cm.tts(bhv="do_sad", string=f"{wm.word(self.role, 2)} 해준 말 중에 {wm.word(self.user_name, 0)}를 가장 행복하게 하는 말은 뭐니?")
                    answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.role, 2)} 하는 말 중에 {wm.word(self.user_name, 0)}가 가장 듣기 싫은 말은 뭐니?",
                                               pos_bhv="do_question_S", pos="그 말을 언제 가장 듣고 싶니?",
                                               neu_bhv="do_agree", neu="괜찮아~ 생각이 나지 않을 수 있어~",
                                               act_bhv="do_question_S", act="그 말을 언제 가장 듣고 싶니?")  
                    
                    if answer[0] == "action" or answer[0] == "positive":
                        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"그 말을 언제 가장 듣고 싶니?",
                                                   neu_bhv="do_agree", neu="괜찮아~ 생각이 나지 않을 수 있어~",
                                                   act_bhv="do_joy_B", act=" 기분 좋겠는 걸?")
                    self.count += 1 
                            
            if self.count < 3:
                print(self.count)
                continue
            
            elif self.count == 3:
                print(self.count)
                break
        
        # 4. 마무리 대화
        cm.tts(bhv="do_joy_B", string="오늘 역할놀이도 정말 재미있었어. 다음에 또 놀자!")




if __name__ == "__main__":
    
    rop = Roleplay()
    rop.Parents()