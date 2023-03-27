# -*- coding: utf-8 -*-

# 역할놀이-작은 존재

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


class Roleplay():    
    
    def __init__(self): 
        self.user_name = '다영'
        self.count = 0
        
    
    def Tiny(self):
        
        # 1. 역할 알림
        cm.tts(bhv="do_suggestion_S", string="역할 놀이를 해볼까?")
        cm.tts(bhv="do_suggestion_S", string="오늘은 아주 작은 역할을 해보자~") 
        
        # 2. 역할 놀이 (1 of 3)        
        
        animal = (['귀뚜라미', '작은귀뚜라미', '멋진 울음소리를 들려주는 귀뚜라미는 싸움을 하거나, 암컷을 부를 때 소리를 낸다고 해. 신기하지 않니?'],
                  ['고양이', '새끼고양이', '고양이는 수영도 잘하고 높은 곳에서도 안전하게 뛰어내릴 수 있다고 해.대단하지 않니?'],
                  ['개구리', '작은개구리', '개구리 중에 금개구리는 우리나라에서만 사는 아주 작고 귀여운 개구리라고 해. 금개구리 등에는 금색 줄이 있단다. 멋지지 않니?'])

        role = random.choice([animal[0], animal[1], animal[2]])
        
        cm.tts(bhv="do_suggestion_S", string=f"이제 우리는 {wm.word(role[1], 0)}야!")
        
        cm.tts(bhv="do_suggestion_L", string=f"{wm.word(self.user_name, 0)}도 {role[0]} 소리를 흉내내 보자! 시작!")
        answer = cm.responses_proc(re_bhv="do_suggestion_L", re_q=f"{wm.word(self.user_name, 0)}도 {role[0]} 울음 소리를 흉내내보자! 시작!",
                                   neu_bhv="do_explain_A", neu=f"{wm.word(role[0], 2)} 이렇게 울어~",
                                   act_bhv="do_joy_A", act=f"{wm.word(role[1], 1)} 나타났다!")
        # audio.audio_play(filename)
        cm.tts(bhv="do_explain_B", string=role[2])
        
        # 3. 대화 시작 (3 of 6)
        rand = random.sample(range(1,7), 3)
        
        while True:
            for i in range(len(rand)):
                if rand[i] == 1:                             
                    cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}가 {wm.word(role[0], 1)} 된다면 어떤 점이 가장 좋을까?")
                    answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}가 {wm.word(role[0], 1)} 된다면  어떤 점이 가장 좋을까?",
                                               neu_bhv="do_agree", neu="괜찮아~ 생각나지 않을 수 있어~")                    
                    self.count += 1 
                    
                if rand[i] == 2: 
                    cm.tts(bhv="do_question_L", string=f"{wm.word(role[1], 2)} 작아서 언제 가장 힘들까?")
                    answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}가 {wm.word(role[0], 1)} 된다면  어떤 점이 가장 좋을까?",
                                               pos_bhv="do_question_S", pos=f"{wm.word(self.user_name, 0)}도 작아서 속상했던 적이 있니?",
                                               neu_bhv="do_agree", neu="괜찮아~ 대답하기 어려울 수 있어~",
                                               act_bhv="do_question_S", act=f"{wm.word(self.user_name, 0)}도 작아서 속상했던 적이 있니?")
                    
                    if answer[0][0] == "action":
                        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}도 작아서 속상했던 적이 있니?",
                                                   pos_bhv="do_question_S", pos="자세히 이야기해 줄래?",
                                                   neu_bhv="do_agree", neu="괜찮아~ 대답하기 어려울 수 있어~")
                        
                        if answer[0][0] == "positive":
                            answer = cm.responses_proc(re_bhv="do_question_S", re_q="자세히 이야기해 줄 수 있니?",
                                                       pos_bhv="do_sad", pos=f"{wm.word(self.user_name, 0)}가 속상했겠다.",
                                                       neu_bhv="do_agree", neu="괜찮아~말하기 어려울 수 있어~",
                                                       act_bhv="do_sad", act=f"{wm.word(self.user_name, 0)}가 속상했겠다.")                            
                    self.count += 1
                    
                if rand[i] == 3: 
                    cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}가 {wm.word(role[0], 1)} 되어서 숨고 싶다고 느낀 적이 있니?")
                    answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}가 {wm.word(role[0], 1)} 되어서 숨고 싶다고 느낀 적이 있니?",
                                               pos_bhv="do_question_S", pos="언제 숨고 싶었니?",
                                               neu_bhv="do_agree", neu="괜찮아~ 말하기 어려울 수 있어~")
                    
                    if answer[0][0] == "positive":
                        answer = cm.responses_proc(re_bhv="do_question_S", re_q="언제 숨고 싶었니?",
                                                   neu_bhv="do_agree", neu="괜찮아~ 말하기 어려울 수 있어~",
                                                   act_bhv="do_agree", act="그래서 숨고 싶었구나~")                   

                    self.count += 1
                    
                if rand[i] == 4: 
                    cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}가 {wm.word(role[0], 1)} 된다면 어디에 살고 싶니?")
                    answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}가 {wm.word(role[0], 1)} 된다면 어디에 살고 싶니?",
                                               pos_bhv="do_question_S", pos="언제 숨고 싶었니?",
                                               neu_bhv="do_agree", neu="괜찮아~ 생각이 나지 않을 수도 있어~")
                    
                    if answer[0][0] == "positive":
                        answer = cm.responses_proc(re_bhv="do_question_S", re_q="누구랑 그곳에 살고 싶니?",
                                                   neu_bhv="do_agree", neu="괜찮아~ 생각이 나지 않을 수도 있어~",
                                                   act_bhv="do_joy_B", act="같이 살면 정말 좋겠다!")               
                    self.count += 1
                    
                if rand[i] == 5: 
                    cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}는 {wm.word(role[0], 1)} 되어서 몰래 가보고 싶은 곳이 있니?")
                    answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}가 {wm.word(role[0], 1)} 된다면 어디에 살고 싶니?",
                                               pos_bhv="do_question_S", pos="그 곳에 가서 무엇을 하고 싶니?",
                                               neu_bhv="do_agree", neu="괜찮아~ 바로 떠오르지 않을 수 있어~")
                    
                    if answer[0][0] == "positive":
                        answer = cm.responses_proc(re_bhv="do_question_S", re_q="그 곳에 가서 무엇을 하고 싶니?",
                                                   neu_bhv="do_agree", neu="괜찮아~ 바로 떠오르지 않을 수 있어~",
                                                   act_bhv="do_joy_B", act="파이보도 함께 가고 싶다~")      
                    self.count += 1
                    
                if rand[i] == 6: 
                    cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}는 {wm.word(role[0], 1)} 되어서 몰래 도와주고 싶은 사람이 있니?")
                    answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}는 {wm.word(role[0], 1)} 되어서 몰래 도와주고 싶은 사람이 있니?",
                                               pos_bhv="do_question_S", pos="어떤 도움을 주고 싶니?",
                                               neu_bhv="do_agree", neu="괜찮아~ 생각나지 않을 수도 있어~")
                    
                    if answer[0][0] == "positive":
                        answer = cm.responses_proc(re_bhv="do_question_S", re_q="어떤 도움을 주고 싶니?",
                                                   neu_bhv="do_agree", neu="몰라도 괜찮아~",
                                                   act_bhv="do_joy_B", act=f"{wm.word(self.user_name, 0)}가 도와주면 정말 좋겠다~")      
                    self.count += 1
            
            if self.count < 3:
                print(self.count)
                continue
            
            elif self.count == 3:
                print(self.count)
                break
        
        # 4. 마무리 대화
        cm.tts(bhv="do_joy_A", string=f"{wm.word(role[0], 2)} 작지만 멋진 친구들이야! 다음에 또 재미있는 역할놀이 하자~")



if __name__ == "__main__":
    
    rop = Roleplay()
    rop.Tiny()