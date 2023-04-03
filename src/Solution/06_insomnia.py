# -*- coding: utf-8 -*-

# 문제해결-잠이 안와

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
                

    def Insomnia(self):
        
        # 1.1 문제 제시
        pibo = cm.tts(bhv="do_sad", string="요즘 밤에 잠이 안 와.")
        
        # 1.2 경험 질문
        pibo = cm.tts(bhv="do_sad", string=f"{wm.word(self.user_name, 0)}는 보통 몇 시에 잠을 자니?")
        answer = cm.responses_proc(re_bhv="do_sad", re_q=f"{wm.word(self.user_name, 0)}는 보통 몇 시에 잠을 자니?")    
    
        pibo = cm.tts(bhv="do_question_L", string="키가 크려면 몇시에 자야 할까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="키가 크려면 몇시에 자야 할까?",
                                   pos_bhv="do_explain_A", pos="일찍자면 키가 커지겠지?",
                                   neu_bhv="do_explain_A", neu="몰라도 괜찮아~ 아마 일찍자면 키가 커지겠지?",
                                   act_bhv="do_explain_A", act="일찍자면 키가 커지겠지?",)

        pibo = cm.tts(bhv="do_question_L", string="잠을 많이 못자면 다음날 기분이 어떠니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="잠을 많이 못자면 다음날 기분이 어떠니?",
                                   pos_bhv="do_agree", pos="많이 못자면 피곤하겠지?",
                                   neu_bhv="do_agree", neu="괜찮아~ 생각이 나지 않을 수 있어~ 많이 못자면 피곤하겠지?",
                                   act_bhv="do_agree", act="많이 못자면 피곤하겠지?")

        pibo = cm.tts(bhv="do_question_S", string=f"양을 세면 잠이 온다던데, {wm.word(self.user_name, 0)}는 잠이 안 올 때 어떻게 하니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"양을 세면 잠이 온다던데, {wm.word(self.user_name, 0)}는 잠이 안 올 때 어떻게 하니?",
                                   neu_bhv="do_agree", neu="괜찮아~ 모를 수도 있어~")
            
        pibo = cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}는 평소에 어떤 꿈을 꾸니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}는 평소에 어떤  꿈을 꾸니?",
                                   pos_bhv="do_agree", pos="신기한 걸?",
                                   neu_bhv="do_agree", neu="괜찮아~ 생각이 나지 않을 수 있어~",
                                   act_bhv="do_agree", act="신기한 걸")
        
        pibo = cm.tts(bhv="do_question_L", string="눈을 계속 감고 상상을 하면 잠이 올까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="눈을 계속 감고 상상을 하면 잠이 올까?",
                                   pos_bhv="do_agree", pos="왠지 잠이 올 것만 같아!",
                                   neu_bhv="do_agree", neu="괜찮아~ 모를 수도 있어~ 눈을 감고 상상을 하면 왠지 잠이 올 것만 같아!",
                                   act_bhv="do_agree", act="왠지 잠이 올 것만 같아!")
        
        # 2.1 문제 해결
        pibo = cm.tts(bhv="do_joy_A", string="파이보도 이제 일찍 자도록 노력해야겠다~ 알려줘서 정말 고마워!")
                            
        
        
        
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
    sol.Insomnia()