# -*- coding: utf-8 -*-

# 동화-신데렐라

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

folder = "home/pi/UserData"
filename = os.path.basename(__file__).strip('.py')
today = datetime.now().strftime('%y%m%d_%H%M')
csv_conversation = open(f'{folder}/{today}_{filename}.csv', 'a', newline='', encoding = 'cp949')
csv_preference = open(f'{folder}/aa.csv', 'a', newline='', encoding = 'cp949')
cwc = csv.writer(csv_conversation)
cwp = csv.writer(csv_preference)
crc = csv.reader(csv_conversation, delimiter=',', doublequote=True, lineterminator='\r\n', quotechar='"')


class Fairytale():    
    
    def __init__(self): 
        self.user_name = '가영'
                
        
    def Cinderella(self):
        
        # 1. 동화 줄거리 대화        
        cm.tts(bhv="do_joy_A", string=f"이 동화는 신데렐라가 나오는 동화였어! {wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?")
        answer = cm.responses_proc(re_bhv="do_joy_A", re_q=f"{wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?",
                                   neu_bhv="do_agree", neu=f"그럴 수 있지~")
        
        cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}도 형제나 자매가 있니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}도 형제나 자매가 있니?",
                                   pos_bhv="do_question_L", pos=f"{wm.word(self.user_name, 0)}는 형제가 있으니까 어떤 것 같아?")
        
        if answer[0][0] == "positive":
            answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}는 형제가 있으니까 어떤 것 같아?",
                                       pos_bhv="do_agree", pos=f"그렇게 생각 하는 구나!",
                                       neu_bhv="do_agree", neu=f"괜찮아~ 대답하기 어려울 수 있어~",
                                       act_bhv="do_agree", act=f"그렇게 생각 하는 구나!")
        
        cm.tts(bhv="do_question_L", string=f"신데렐라는 어떤 색의 구두와 드레스를 입고 무도 회장에 갔을 것 같니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"신데렐라는 어떤 색의 구두와 드레스를 입고 무도 회장에 갔을 것 같니?",
                                   pos_bhv="do_agree", pos=f"정말 예뻤을 것 같아!",
                                   act_bhv="do_agree", act=f"정말 예뻤을 것 같아!")
        
        cm.tts(bhv="do_question_S", string=f"신데렐라가 왕자님과 만나지 못했다면 어떻게 됐을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"신데렐라가 왕자님과 만나지 못했다면 어떻게 됐을까?",
                                   neu_bhv="do_agree", neu=f"모를 수 있지~")

        # 2. 등장인물 공감 대화        
        cm.tts(bhv="question_S", string=f"처음에 무도 회장을 못 가게 된 신데렐라의 마음이 슬펐을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"처음에 무도 회장을 못 가게 된 신데렐라의 마음이 슬펐을까?", 
                                   pos_bhv="do_question_S", pos=f"{wm.word(self.user_name, 0)}도 어디 못 가서 슬펐던 적이 있니?",
                                   neu_bhv="do_agree", neu=f"몰라도 괜찮아~",
                                   act_bhv="do_question_S", act=f"{wm.word(self.user_name, 0)}도 어디 못 가서 슬펐던 적이 있니?")

        if answer[0][0] == "positive" or answer[0][0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}도 어디 못 가서 슬펐던 적이 있니?",
                                       pos_bhv="do_agree", pos=f"그랬구나!")
            
        cm.tts(bhv="question_S", string=f"유리 구두가 신데렐라의 발에 딱 맞았을 때 기뻤을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"유리 구두가 신데렐라의 발에 딱 맞았을 때 기뻤을까?", 
                                   pos_bhv="do_question_S", pos=f"정말 기뻤을 것 같아!", 
                                   neg_bhv="do_agree", neg=f"그럴 수 있겠구나!")
            
        # 3. 마무리 대화    
        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}는 신데렐라를 괴롭힌 새 엄마와 두 언니들에게 해주고 싶은 말이 있니?")
        answer = cm.responses_proc(re_bhv="do_question_L", string=f"신데렐라를 괴롭힌 새 엄마와 두 언니들에게 해주고 싶은 말이 있니?",  
                                   pos_bhv="do_agree", pos=f"그렇구나!",
                                   neu_bhv="do_agree", neu=f"괜찮아~ 모를 수 있지~",
                                   neg_bhv="do_agree", neg=f"그렇구나!",
                                   act_bhv="do_agree", act=f"그렇구나!")
        
        cm.tts(bhv="do_explain_C", string=f"오늘 동화 재미있었지? 다음에 또 재미있는 동화를 들려줄게~")
        
        
        
        
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
    
    fat = Fairytale()
    fat.Cinderella()
