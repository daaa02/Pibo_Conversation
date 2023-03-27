# -*- coding: utf-8 -*-

# 문제 해결-아침에 일찍 일어나기 힘들어

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


class Solution():    
    
    def __init__(self): 
        self.user_name = '윤지'
        
        
    def Morning(self):
        
        # 1.1 문제 제시
        cm.tts(bhv="do_sad", string="요즘 자꾸 늦잠을 자.")
        
        # 1.2 경험 질문
        cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, type=0)}도 아침에 일어나기 힘드니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, type=0)}도 아침에 일어나기 힘드니?",
                                   pos_bhv="do_agree", pos="나랑 비슷하구나.")
        
        cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, type=0)}는 보통 몇시에 일어나니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="보통 몇 시에 일어나니?")
        
        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, type=0)} 친구들은 보통 몇시에 일어나는지 알고 있니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, type=0)} 친구들은 보통 몇시에 일어나는지 알고 있니?",
                                   neu_bhv="do_agree", neu="괜찮아~ 모를 수도 있어~")
        
        cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, type=0)}랑 친구들 나이에는 일찍자고 일찍 일어나는 것이 좋다고 해!")
        
        cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, type=0)}는 일어나자마자 하는 일이 있니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, type=0)}는 일어나자마자 하는 일이 있니?",
                                   neu_bhv="do_agree", neu="괜찮아~ 생각이 나지 않을 수 있어!")
        
        cm.tts(bhv="do_question_S", string="어떻게 하면 잠을 빨리 깰 수 있을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="어떻게 하면 잠을 빨리 깰 수 있을까?",
                                   neu_bhv="do_agree", neu="괜찮아~ 모를 수도 있어~",
                                   act_bhv="do_agree", act="세수를 하는 것도 좋겠지?")
        
        cm.tts(bhv="do_question_S", string="아침에 일찍 일어나면 뭐가 좋을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="아침에 일찍 일어나면 뭐가 좋을까?",
                                   pos_bhv="do_agree", pos="일찍 일어나면 더 많이 놀 수 있겠지?",
                                   neu_bhv="do_agree", neu="괜찮아~ 모를 수도 있어~",
                                   act_bhv="do_agree", act="일찍 일어나면 더 많이 놀 수 있겠지?")
        
        # 2.1 마무리 대화
        cm.tts(bhv="do_joy_A", string="파이보도 이제 일찍 일어나도록 노력해야겠다~ 알려줘서 정말 고마워!")
        
        
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
    
    sol = Solution()
    sol.Morning()