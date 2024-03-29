# -*- coding: utf-8 -*-

# 문제해결-사과를 하기 어려워

import os, sys
import re
import csv
import random
from datetime import datetime
import time
import json

# sys.path.append('/home/kiro/workspace/Conversation_Scenarios/')
sys.path.append('/home/pi/Pibo_Conversation/')
from data.c_conversation_manage import ConversationManage, WordManage, NLP
from data.speech_to_text import speech_to_text
from data.text_to_speech import TextToSpeech, text_to_speech
from data.spread import google_spread_sheet

cm = ConversationManage()
wm = WordManage()
nlp = NLP()
audio = TextToSpeech()
gss = google_spread_sheet()

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
        with open('/home/pi/name_config.json', 'r') as f:
            config = json.load(f)        
            self.user_name = config['user_name'] 
        self.score = []
        self.turns = []
        self.reject = []
                
        
    def Apology(self):
        
        # 1.1 문제 제시
        pibo = cm.tts(bhv="do_sad", string="파이보는 친구에게 사과를 하기가 어려워.")
        
        # 1.2 경험 질문
        pibo = cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}는 친구에게 사과를 한 적이 있니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}는 친구에게 사과를 한 적이 있니?",
                                   pos_bhv="do_question_S", pos="어떤 일이 있었니?")                
    
        if answer[0][0] == "positive":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q="어떤 일이 있었니?",
                                       neu_bhv="do_compliment_S", neu=" 괜찮아. 생각이 나지 않을 수 있어.")
            
            pibo = cm.tts(bhv="do_question_S", string=f"사과를 할 때 {wm.word(self.user_name, 0)}의 마음이 어땠니?")
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"사과를 할 때 {wm.word(self.user_name, 0)}의 마음이 어땠니?")
            
            pibo = cm.tts(bhv="do_question_S", string=f"사과를 받은 친구가 {wm.word(self.user_name, 0)}에게 뭐라고 말했니?")
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"사과를 받은 친구가 {wm.word(self.user_name, 0)}에게 뭐라고 말했니?",
                                       neu_bhv="do_compliment_S", neu="괜찮아. 바로 떠오르지 않을 수 있어.")
            
        pibo = cm.tts(bhv="do_question_S", string="사과를 해야 할 때는 언제라고 생각하니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="사과를 해야 할 때는 언제라고 생각하니?",
                                   pos_bhv="do_compliment_S", pos="그렇게 생각하는구나!",
                                   neu_bhv="do_compliment_S", neu="괜찮아. 말하기 어려울 수 있어.",
                                   act_bhv="do_compliment_S", act="그렇게 생각하는구나!")
        
        pibo = cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}도 친구에게 사과하기 어려울 때가 있니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}도 속마음을 말하기 어려울 때가 있니?",
                                   pos_bhv="do_compliment_S", pos="미안하다는 말은 쫌 쑥스러운 것 같아.",
                                   neu_bhv="do_compliment_S", neu="괜찮아. 말하기 어려울 수 있어. 나도 미안하다는 말은 쫌 쑥스러운 것 같아.",
                                   neg_bhv="do_compliment_L", neg="정말 대단한 걸?")
        
        if answer[0] !="negative":
            pibo = cm.tts(bhv="do_question_L", string="그런데, 사과를 안 하면 친구들이 마음을 모르겠지?")
            answer = cm.responses_proc(re_bhv="do_question_S", re_q="그런데, 미안하다고 말을 안 하면 친구들이 나의 미안한 마음을 알 수 있을까?",
                                       pos_bhv="do_compliment_S", pos="친구들이 알기 어려울거야.",
                                       neu_bhv="do_compliment_S", neu="아마 친구들이 알아채기 어려울거야.",
                                       act_bhv="do_compliment_S", act="친구들이 알기 어려울거야.")
        
        # 2.1 문제 해결
        pibo = cm.tts(bhv="do_joy_A", string="파이보도 이제 다른 친구들에게 미안하다고 잘 표현할 수 있도록 노력해야겠다. 알려줘서 정말 고마워!")
                            
        
        
        
        # 3. 피드백 수집
        time.sleep(1)                   
        pibo = cm.tts(bhv="do_question_S", string="파이보랑 얘기한 거 재미있었어? 재밌었는지, 별로였는지 얘기해줄래?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"파이보랑 얘기한 거 재미있었어?") 
              
        if answer[0][0] == "negative":
            cm.tts(bhv="do_joy_A", string=f"파이보는 {wm.word(self.user_name, 0)}랑 놀아서 재미있었어!")
            self.score = [0.0, -0.5, 0.0, 0.0]
        
        if answer[0][0] == "positive":
            cm.tts(bhv="do_joy_A", string=f"나도야! 다음에 또 재미있는 놀이 알려줄게.")
            self.score = [0.0, 0.5, 0.0, 0.0]
            
        if answer[0][0] != "negative" and answer[0][0] != "positive": # if answer[0][0] == "neutral":
            cm.tts(bhv="do_joy_A", string=f"{wm.word(self.user_name, 0)}랑 노는 건 정말 재미있어.")
            self.score = [0.0, -0.25, 0.0, 0.0]
        
        cwp.writerow([today, filename, self.score[0], self.score[1], self.score[2],self.score[3]])

        # 종료 인사
        pibo = cm.tts(bhv="do_joy_A", string=f"나랑 놀아줘서 고마워~")

        # 4. Paradise framework 기록
        turns = sum((self.reject[i] + 1) * 2 for i in range(len(self.reject)))  
        reject = sum(self.reject) 
        
        cwc.writerow(['Turns', turns])
        cwc.writerow(['Rejections', reject])
        cwc.writerow(['Misrecognitions', ])

        cwc.writerow(['%Turns', ])
        cwc.writerow(['%Rejections', ])
        cwc.writerow(['%Misrecognitions', ])

        # 5. 활동 완료 기록
        gss.write_sheet(name=self.user_name, today=today, activities=filename)




if __name__ == "__main__":
    
    sol = Solution()
    sol.Apology()