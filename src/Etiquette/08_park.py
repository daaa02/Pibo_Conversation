# -*- coding: utf-8 -*-

# 사회기술-공원의 꽃을 꺾거나 잔디를 밟지 않아요

import os, sys
import re
import csv
import random
from datetime import datetime
import time

# sys.path.append('/home/kiro/workspace/Conversation_Scenarios/')
sys.path.append('/home/pi/Pibo_Conversation/')
from data.conversation_manage import ConversationManage, WordManage
from data.speech_to_text import speech_to_text
from data.text_to_speech import TextToSpeech, text_to_speech

cm = ConversationManage()
wm = WordManage()
audio = TextToSpeech()

folder = "/home/pi/UserData"
filename = os.path.basename(__file__).strip('.py')
today = datetime.now().strftime('%y%m%d_%H%M')
csv_conversation = open(f'{folder}/{today}_{filename}.csv', 'a', newline='', encoding = 'cp949')
csv_preference = open(f'{folder}/aa.csv', 'a', newline='', encoding = 'cp949')
cwc = csv.writer(csv_conversation)
cwp = csv.writer(csv_preference)
crc = csv.reader(csv_conversation, delimiter=',', doublequote=True, lineterminator='\r\n', quotechar='"')


class Etiquette():    
    
    def __init__(self): 
        self.user_name = "가영"
        
        
    def Park(self):     

        # 2.1 카드 대화
        cm.tts(bhv="do_question_L", string="이 카드의 어린이는 무엇을 잘못했을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="이 카드의 어린이는 무엇을 잘못했을까?",
                                   neg_bhv="do_suggestion_S", neg="같이 다시 한번 볼까?",
                                   neu_bhv="do_suggestion_S", neu="같이 다시 한번 볼까?")             
        
        if answer[0][0] == "action":            
            
            for i in range(len(self.correct)):
                if self.correct[i] in answer[1]:
                    self.ox = "(right)"                    
            if len(self.ox) == 0:
                self.ox = "(wrong ㅠㅠ)"
              
            if self.ox == "(right)":
                print(self.ox)
                cm.tts(bhv="do_compliment_S", string="맞아! 아주 똑똑한 걸?")
            else:
                print(self.ox)
                cm.tts(bhv="do_suggestion_S", string="또 무엇을 잘못했을까?")
                answer = cm.responses_proc(re_bhv="do_suggestion_S", re_q="또 무엇을 잘못했을까?")
                
                if answer[0][0] == "action":        
                                
                    for i in range(len(self.correct)):
                        if self.correct[i] in answer[1]:
                            self.ox = "(right)"                    
                    if len(self.ox) == 0:
                        self.ox = "(wrong ㅠㅠ)"
                    
                    if self.ox == "(right)":
                        print(self.ox)
                        cm.tts(bhv="do_compliment_S", string="맞아! 아주 똑똑한 걸?")
                    else:
                        print(self.ox)
                        cm.tts(bhv="do_suggestion_S", string="같이 다시 한번 볼까?")

        cm.tts(bhv="do_question_S", string="이 카드의 어린이는 공원의 잔디를 밟고 꽃을 꺾었어.")
        
        # 2.2 경험 질문
        cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, type=0)}는 공원에 가면 무엇을 하니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, type=0)}는 공원에 가면 무엇을 하니?",
                                   neu_bhv="do_agree", neu="괜찮아, 기억이 안 날 수 있어.")
        
        cm.tts(bhv="do_question_S", string="공원에 가면 사람들이 무엇을 하고 있니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="공원에 가면 사람들이 무엇을 하고 있니?",
                                   neu_bhv="do_agree", neu="괜찮아 모를 수도 있어~ 사람들은 앉아서 쉬기도 하고 가족과 친구와 놀기도 하겠지?",
                                   act_bhv="do_agree", act="사람들은 앉아서 쉬기도 하고 가족과 친구와 놀기도 하겠지?")
        
        cm.tts(bhv="do_question_S", string="공원의 잔디와 꽃을 망가뜨리면 어떤 일이 일어날까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="공원의 잔디와 꽃을 망가뜨리면 어떤 일이 일어날까?",
                                   pos_bhv="do_agree", pos="예쁜 공원이 망가지고 사람들은 쉴 수 없겠지?",
                                   act_bhv="do_agree", act="예쁜 공원이 망가지고 사람들은 쉴 수 없겠지?",
                                   neu_bhv="do_agree", neu="괜찮아 모를 수도 있어~ 예쁜 공원이 망가지고 사람들은 쉴 수 없겠지?")
        
        # 2.3 문제 인식
        cm.tts(bhv="do_question_S", string="누군가 공원의 잔디와 꽃을 망가뜨리면 다른 사람들은 어떻게 느낄까?") 
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="누군가 공원의 잔디와 꽃을 망가뜨리면 다른 사람들은 어떻게 느낄까?",
                                   neu_bhv="do_agree", neu="괜찮아 모를 수도 있어~  공원이 망가져서 속상하기도 하고, 잔디랑 꽃이 불쌍하다고 생각하겠지?",
                                   act_bhv="do_agree", act="공원이 망가져서 속상하기도 하고, 잔디랑 꽃이 불쌍하다고 생각하겠지?")
        
        # 3.1 마무리 대화
        cm.tts(bhv="do_joy_A", string="모두가 함께 이용하는 공원을 망가뜨리는 것은 잘못된 행동이야. 식물도 생명이니까 소중히 다뤄야 해. 잘 기억해 두자!")




        # 3. 피드백 수집
        time.sleep(1)                   
        cm.tts(bhv='do_question_S', string="활동 어땠어? 재밌었는지, 별로였는지 얘기해줄래?")
        answer = cm.responses_proc()  
              
        if answer[0][0] == "negative":
            self.score = [0.0, -0.5, 0.0, 0.0]
        
        if answer[0][0] == "positive":
            self.score = [0.0, 0.5, 0.0, 0.0]
            
        else: # if answer[0][0] == "neutral":
            self.score = [0.0, -0.25, 0.0, 0.0]
        
        cwp.writerow([today, filename, self.score[0], self.score[1], self.score[2],self.score[3]])
        
        # 4. Paradise framework 기록
        turns = [(self.reject[i] + 1) * 2 for i in range(len(self.reject))]      
        reject = sum(self.reject) 
        
        cwc.writerow(['Turns', turns])
        cwc.writerow(['Rejections', reject])
        cwc.writerow(['Misrecognitions', ])




if __name__ == "__main__":
    etq = Etiquette()
    etq.Park()
    
