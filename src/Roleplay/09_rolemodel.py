# -*- coding: utf-8 -*-

# 역할 놀이-되고 싶은 인물

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


class RolePlay():    
    
    def __init__(self): 
        self.user_name = "다영"
        self.rolemodel = ''
        

    def RoleModel(self):
        
        # 1.1 역할 알림
        cm.tts(bhv="", string=f"역할 놀이를 해볼까? {wm.word(self.user_name, type=0)}가 원하는 사람이 되어볼거야!")
        
        # 2.1 역할놀이(1)
        cm.tts(bhv="", string=f"파이보는 커서 과학자가 되고 싶어! {wm.word(self.user_name, type=0)}는 뭐가 되고 싶니?")
        
        while True:
            answer = cm.responses_proc(re_q=f"{wm.word(self.user_name, type=0)}는 뭐가 되고 싶니?")
            
            if answer == "neutral":
                cm.tts(bhv="", string=f"괜찮아~ 바로 떠오르지 않을 수도 있어~ 소방관, 의사, 디자이너, 화가 등이 있어~ {wm.word(self.user_name, type=0)}는 뭐가 되고 싶니?")
                continue
            
            elif answer != "neutral":
                self.rolemodel = "돌멩이"   # NER
                
                cm.tts(bhv="", string=f"{self.rolemodel} 맞아?")
                answer = cm.responses_proc(re_q=f"{self.rolemodel} 맞아?")

                if answer == "positive":
                    break
                
                elif answer == "negative":
                    cm.tts(bhv="", string=f"다시 크게 말해줄래?")
                    continue
        
        # 3.1 역할 대화
        cm.tts(bhv="", string=f"{wm.word(self.rolemodel, type=2)} 정말 중요한 일을 한다고 생각해")
        
        cm.tts(bhv="", string=f"{wm.word(self.user_name, type=0)}는 가장 유명한 {wm.word(self.rolemodel, type=3)} 아니?")
        answer = cm.responses_proc(re_q=f"{wm.word(self.user_name, type=0)}는 가장 유명한 {wm.word(self.rolemodel, type=3)} 아니?",
                                   neu="몰라도 괜찮아~")
        
        if answer == "positive":
            cm.tts(bhv="", string=f"그 사람은 왜 유명할까?")
            answer = cm.responses_proc(re_q="그 사람은 왜 유명할까?")
            
        cm.tts(bhv="", string=f"{wm.word(self.user_name, type=0)}의 주변에 {wm.word(self.rolemodel, type=1)} 있니?")
        answer = cm.responses_proc(re_q="주변에 있니?",
                                   neu="괜찮아~ 생각 나지 않을 수 있어")
        
        if answer == "positive":
            cm.tts(bhv="", string=f"그 사람은 누구니?")
            answer = cm.responses_proc(re_q="그 사람은 누구니?")
            
        cm.tts(bhv="", string=f"{wm.word(self.rolemodel, type=3)} 생각하면 무슨 색이 떠올라?")
        answer = cm.responses_proc(re_q=f"{wm.word(self.user_name, type=3)} 생각하면 무슨 색이 떠올라?",
                                   neu="괜찮아~ 바로 떠오르지 않을 수도 있어")
        
        if answer == "positive":
            cm.tts(bhv="", string=f"그 색깔이 왜 떠올랐을까?")
            answer = cm.responses_proc(re_q="그 색깔이 왜 떠올랐을까?")
            
        cm.tts(bhv="", string=f"{wm.word(self.user_name, type=0)}가 {wm.word(self.rolemodel, type=1)} 된다면 뭘 하고 싶니?")
        answer = cm.responses_proc(re_q=f"{wm.word(self.rolemodel, type=1)} 된다면 뭘 하고 싶니?",
                                   neu="괜찮아~ 대답하기 어려울 수 있어")
        
        if answer == "positive":
            cm.tts(bhv="", string=f"그렇게 생각한 이유는 뭐야?")
            answer = cm.responses_proc(re_q="그렇게 생각한 이유는 뭐야?")
        
        # 4.1 마무리 대화
        cm.tts(bhv="do_joy_A", string=f"{wm.word(self.user_name, type=0)}가 되고 싶은 역할 놀이를 해서 너무 재미있었어! 다음에 또 재미있는 역할놀이 하자~")
        
        
        
        
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
    rp = RolePlay()
    rp.RoleModel()