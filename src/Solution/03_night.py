# -*- coding: utf-8 -*-

# 문제해결-늦게까지 놀고 싶어

import os, sys
import re
import csv
import random
from datetime import datetime
import time

# sys.path.append('/home/kiro/workspace/Conversation_Scenarios/')
sys.path.append('/home/pi/Pibo_Conversation/')
from data.conversation_manage import ConversationManage, WordManage, NLP
from data.speech_to_text import speech_to_text
from data.text_to_speech import TextToSpeech, text_to_speech


cm = ConversationManage()
wm = WordManage()
nlp = NLP()
audio = TextToSpeech()

folder = "/home/pi/UserData"
filename = os.path.basename(__file__).strip('.py')
today = datetime.now().strftime('%y%m%d_%H%M')
csv_conversation = open(f'{folder}/{today}_{filename}.csv', 'a', newline='', encoding = 'utf-8')
csv_preference = open(f'{folder}/aa.csv', 'a', newline='', encoding = 'utf-8')
cwc = csv.writer(csv_conversation)
cwp = csv.writer(csv_preference)
crc = csv.reader(csv_conversation, delimiter=',', doublequote=True, lineterminator='\r\n', quotechar='"')


class Solution():    
    
    def __init__(self): 
        self.user_name = '다영'
        self.score = []
        self.turns = []
        self.reject = []
                
        
    def Wash(self):
        
        # 1.1 문제 제시
        pibo = cm.tts(bhv="do_sad", string="요즘 늦은 시간까지 안자고 계속 놀고 싶어.")
        
        # 1.2 경험 질문
        pibo = cm.tts(bhv="do_sad", string=f"{wm.word(self.user_name, 0)}도 밤 늦게까지 놀고 싶니?")
        answer = cm.responses_proc(re_bhv="do_sad", re_q=f"{wm.word(self.user_name, 0)}도 씻기 싫을 때가 있지?",
                                   pos_bhv="do_agree", pos="나랑 비슷한 걸?")    
     
        pibo = cm.tts(bhv="do_question_L", string="어떻게 하면 계속 놀고 싶은 마음을 멈출 수 있을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="어떻게 하면 계속 놀고 싶은 마음을 멈출 수 있을까?",
                                   neu_bhv="do_agree", neu="괜찮아~ 바로 떠오르지 않을 수 있어~")

        pibo = cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}는 밤에도 조용히 놀 수 있니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}는 밤에도 조용히 놀 수 있니?",
                                   pos_bhv="do_explain_C", pos="대단한 걸? 나는 조용히 못 놀아.")

        pibo = cm.tts(bhv="do_question_S", string="동화책을 보면 조용히 놀 수 있을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="동화책을 보면 조용히 놀 수 있을까?")
            
        pibo = cm.tts(bhv="do_question_S", string="늦게까지 놀면 다음 날 무슨 일이 생길까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="늦게까지 놀면 다음 날 무슨 일이 생길까?",
                                   pos_bhv="do_joy_B", pos="다음 날 피곤하겠지?",
                                   neu_bhv="do_agree", neu="괜찮아~ 상상하기 어려울 수 있어. 아마 다음 날 피곤하겠지?",
                                   act_bhv="do_joy_B", act="다음 날 피곤하겠지?")
        
        pibo = cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}는 내일 무엇을 하며 놀고 싶니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}는 밤에도 조용히 놀 수 있니?",
                                   pos_bhv="do_explain_C", pos="내일 아침이 기다려 지겠다!",
                                   neu_bhv="do_agree", neu="괜찮아~ 바로 떠오르지 않을 수 있어~",
                                   act_bhv="do_joy_A", act="내일 아침이 기다려 지겠다!")
        
        # 2.1 문제 해결
        pibo = cm.tts(bhv="do_joy_A", string="파이보도 이제는 늦게까지 놀지 않고 다음 날 아침을 기분 좋게 시작해야겠다~ 알려줘서 정말 고마워!")
                            
        
        # 3. 피드백 수집
        time.sleep(1)                   
        pibo = cm.tts(bhv="do_question_S", string="활동 어땠어? 재밌었는지, 별로였는지 얘기해줄래?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"활동 어땠어?") 
              
        if answer[0][0] == "negative":
            self.score = [0.0, -0.5, 0.0, 0.0]
        
        if answer[0][0] == "positive":
            self.score = [0.0, 0.5, 0.0, 0.0]
            
        if answer[0][0] != "negative" and answer[0][0] != "positive": # if answer[0][0] == "neutral":
            self.score = [0.0, -0.25, 0.0, 0.0]
        
        cwp.writerow([today, filename, self.score[0], self.score[1], self.score[2],self.score[3]])
        
        # 4. Paradise framework 기록
        turns = sum((self.reject[i] + 1) * 2 for i in range(len(self.reject)))  
        reject = sum(self.reject) 
        
        cwc.writerow(['Turns', turns])
        cwc.writerow(['Rejections', reject])
        cwc.writerow(['Misrecognitions', ])

        cwc.writerow(['%Turns', ])
        cwc.writerow(['%Rejections', ])
        cwc.writerow(['%Misrecognitions', ])




if __name__ == "__main__":
    
    sol = Solution()
    sol.Wash()