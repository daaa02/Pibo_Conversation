# -*- coding: utf-8 -*-

# 역할놀이-크고 강한 존재

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


class Roleplay():    
    
    def __init__(self): 
        with open('/home/pi/name_config.json', 'r') as f:
            config = json.load(f)        
            self.user_name = config['user_name'] 
        self.score = []
        self.turns = []
        self.reject = []
        
    
    def Strong(self):
        
        # 1. 역할 알림
        pibo = cm.tts(bhv="do_suggestion_S", string="역할 놀이를 해볼까?")
        pibo = cm.tts(bhv="do_suggestion_S", string="오늘은 크고 힘이 센 역할을 해보자.")
        
        # 2. 역할 놀이 (1 of 3)
        rand = random.randrange(1,4)
        
        if rand == 1:   # 사자
            pibo = cm.tts(bhv="do_suggestion_S", string="이제 우리는 동물의 왕 사자야!")
            pibo = cm.tts(bhv="do_suggestion_L", string=f"{wm.word(self.user_name, 0)}도 사자 울음 소리를 흉내내보자! 시작!")
            answer = cm.responses_proc(re_bhv="do_suggestion_L", re_q=f"{wm.word(self.user_name, 0)}도 사자 울음 소리를 흉내내보자! 시작!",
                                       pos_bhv="do_joy_A", pos="사자가 나타났다!",
                                       neu_bhv="do_explain_A", neu="사자는 이렇게 울어.",
                                       act_bhv="do_joy_A", act="사자가 나타났다!")
            # audio.audio_play(filename)                        
            cwc.writerow(['pibo', pibo])
            cwc.writerow(['user', answer[0][1], answer[1]])
            self.reject.append(answer[1])
            
            pibo = cm.tts(bhv="do_explain_B", string="사자는 자동차처럼 빨리 달릴 수 있다고 해. 멋지지 않니?")
            
        if rand == 2:   # 늑대
            pibo = cm.tts(bhv="do_suggestion_S", string="이제 우리는 재빠른 늑대야!")
            pibo = cm.tts(bhv="do_suggestion_L", string=f"{wm.word(self.user_name, 0)}도 늑대 울음 소리를 흉내내보자! 시작!")
            answer = cm.responses_proc(re_bhv="do_suggestion_L", re_q=f"{wm.word(self.user_name, 0)}도 늑대 울음 소리를 흉내내보자! 시작!",
                                       pos_bhv="do_joy_A", pos="늑대가 나타났다!",
                                       neu_bhv="do_explain_A", neu="늑대는 이렇게 울어.",
                                       act_bhv="do_joy_A", act="늑대가 나타났다!")
            # audio.audio_play(filename)                        
            cwc.writerow(['pibo', pibo])
            cwc.writerow(['user', answer[0][1], answer[1]])
            self.reject.append(answer[1])
            
            pibo = cm.tts(bhv="do_explain_B", string="늑대는 울음 소리를 통해 멀리 떨어진 늑대랑 이야기 할 수 있다고 해. 신기하지 않니? ")
        
        if rand == 3:   # 호랑이
            pibo = cm.tts(bhv="do_suggestion_S", string="이제 우리는 용감한 호랑이야!")
            pibo = cm.tts(bhv="do_suggestion_L", string=f"{wm.word(self.user_name, 0)}도 무서운 호랑이를 흉내내보자! 시작!")
            answer = cm.responses_proc(re_bhv="do_suggestion_L", re_q=f"{wm.word(self.user_name, 0)}도 무서운 호랑이를 흉내내보자! 시작!",
                                       pos_bhv="do_joy_A", pos="호랑이가 나타났다!",
                                       neu_bhv="do_explain_A", neu="호랑이는 이렇게 울어.",
                                       act_bhv="do_joy_A", act="호랑이가 나타났다!")
            # audio.audio_play(filename)                        
            cwc.writerow(['pibo', pibo])
            cwc.writerow(['user', answer[0][1], answer[1]])
            self.reject.append(answer[1])
            
            pibo = cm.tts(bhv="do_explain_B", string="호랑이는 고양이중에 가장 큰 동물이라고 해! 엄청나지?")
                    
        # 3. 대화 시작 (3 of 6)
        rand = random.randrange(1,7) 
        animal = random.choice(['사자', '늑대', '호랑이'])
        
        if rand == 1:            
            pibo = cm.tts(bhv="do_question_L", string=f"{wm.word(animal, 1)} 된다면 씨름을 하고 싶어. \
                   {wm.word(self.user_name, 0)}가 {wm.word(animal, 1)} 된다면 가장 먼저 무엇을 하고 싶니?")
            answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}가 {wm.word(animal, 1)} 된다면 가장 먼저 무엇을 하고 싶니?",
                                       pos_bhv="do_question_S", pos="언제 하고 싶니?",
                                       neu_bhv="do_compliment_S", neu="괜찮아. 갑자기 떠오르지 않을 수 있어.",
                                       act_bhv="do_question_S", act="언제 하고 싶니?")
            cwc.writerow(['pibo', pibo])
            cwc.writerow(['user', answer[0][1], answer[1]])
            self.reject.append(answer[1])

            if answer[0][0] == "positive" or answer[0][0] =="action":
                answer = cm.responses_proc(re_bhv="do_question_S", re_q="언제 하고 싶니?",
                                           neu_bhv="do_compliment_S", neu="괜찮아. 떠오르지 않을 수 있어.",
                                           act_bhv="do_compliment_S", act=f"{wm.word(self.user_name, 0)}는 그렇게 생각했구나.")
                cwc.writerow(['pibo', pibo])
                cwc.writerow(['user', answer[0][1], answer[1]])
                self.reject.append(answer[1])

        if rand == 2:            
            pibo = cm.tts(bhv="do_question_L", string=f"{wm.word(animal, 1)} 된다면 누구를 보호해주고 싶니?")
            answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(animal, 1)} 된다면 누구를 보호해주고 싶니?",
                                       pos_bhv="do_question_S", pos="언제 보호해 주고 싶니?",
                                       neu_bhv="do_compliment_S", neu="괜찮아. 생각나지 않을 수 있어.",
                                       act_bhv="do_question_S", act="언제 보호해 주고 싶니?")
            
            if answer[0][0] == "positive" or answer[0][0] =="action":
                answer = cm.responses_proc(re_bhv="do_question_S", re_q="언제 보호해 주고 싶니?",
                                           neu_bhv="do_compliment_S", neu="괜찮아. 생각나지 않을 수 있어.",
                                           act_bhv="do_compliment_S", act=f"{wm.word(self.user_name, 0)}가 보호해주면 정말 든든하겠다!")
            
        if rand == 3:
            pibo = cm.tts(bhv="do_question_L", string=f"{wm.word(animal, 1)} 누구를 도와주고 싶니?")
            answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}가 {wm.word(animal, 1)} 된다면 가장 먼저 무엇을 하고 싶니?",
                                       pos_bhv="do_question_S", pos="어떻게 도와주고 싶니?",
                                       neu_bhv="do_compliment_S", neu="괜찮아. 상상하기 어려울 수 있어.",
                                       act_bhv="do_question_S", act="어떻게 도와주고 싶니?")
            
            if answer[0][0] == "positive" or answer[0][0] =="action":
                answer = cm.responses_proc(re_bhv="do_question_S", re_q="어떻게 도와주고 싶니?",
                                           neu_bhv="do_compliment_S", neu="괜찮아. 상상하기 어려울 수 있어.",
                                           act_bhv="do_compliment_S", act=f"{wm.word(self.user_name, 0)}가 도와주면 정말 좋겠다!")
            
        if rand == 4:
            pibo = cm.tts(bhv="do_question_L", string=f"{wm.word(animal, 1)} 된다면 커다란 고래랑 친구가 되고 싶어. \
                   {wm.word(self.user_name, 0)}가 {wm.word(animal, 1)} 된다면 누구와 친구가 되고 싶니?")
            answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}가 {wm.word(animal, 1)} 누구와 친구가 되고 싶니?",
                                       pos_bhv="do_question_S", pos="친구가 돼서 무엇을 하고 싶니?",
                                       neu_bhv="do_compliment_S", neu="괜찮아. 상상하기 어려울 수 있어.",
                                       act_bhv="do_question_S", act="친구가 돼서 무엇을 하고 싶니?")
            
            if answer[0][0] == "positive" or answer[0][0] =="action":
                answer = cm.responses_proc(re_bhv="do_question_S", re_q="친구가 돼서 무엇을 하고 싶니?",
                                           neu_bhv="do_compliment_S", neu="괜찮아. 상상하기 어려울 수 있어.",
                                           act_bhv="do_compliment_S", act="그래서 친구가 되고 싶구나.")
            
        if rand == 5:
            pibo = cm.tts(bhv="do_question_L", string=f"{wm.word(animal, 2)} 어떻게 하면 작은 동물들이랑도 친구가 될 수 있을까?")
            answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(animal, 2)} 어떻게 하면 작은 동물들이랑도 친구가 될 수 있을까?",
                                       pos_bhv="do_question_S", pos=f"{wm.word(self.user_name, 0)}는 친해지기 어려운 친구가 있니?",
                                       neu_bhv="do_compliment_S", neu="괜찮아. 대답하기 어려울 수 있어.",
                                       act_bhv="do_question_S", act=f"{wm.word(self.user_name, 0)}는 친해지기 어려운 친구가 있니?")
            
            if answer[0][0] == "positive" or answer[0][0] =="action":
                answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}는 친해지기 어려운 친구가 있니?",
                                           pos_bhv="do_sad", pos=f"{wm.word(self.user_name, 0)}가 속상했겠다.",
                                           neu_bhv="do_compliment_S", neu="괜찮아. 대답하기 어려울 수 있어.",
                                           neg_bhv="do_compliment_S", neg=f"{wm.word(self.user_name, 0)}는 친구랑 잘 지내는 구나!")
            
        if rand == 6:
            pibo = cm.tts(bhv="do_question_L", string=f"{wm.word(animal, 2)} 무섭기도 하지만 정말 용감하고 씩씩한 동물이야. \
                   {wm.word(self.user_name, 0)} 주변에는 {animal}처럼 용감하고 씩씩한 친구가 있니?")
            answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)} 주변에는 {animal}처럼 용감하고 씩씩한 친구가 있니?",
                                       pos_bhv="do_question_S", pos="그 친구의 이름이 뭐니?",
                                       neu_bhv="do_compliment_S", neu="괜찮아. 생각나지 않을 수 있어.")
            
            if answer[0][0] == "positive":
                answer = cm.responses_proc(re_bhv="do_question_S", re_q="그 친구의 이름이 뭐니?",
                                           pos_bhv="do_compliment_S", pos=f"의 어떤 점이 {animal} 같니?",
                                           neg_bhv="do_question_S", neg="다시 말해 줄래?")
            
                if answer[0][0] == "positive":
                    answer = cm.responses_proc(re_bhv="do_compliment_S", re_q=f"의 어떤 점이 {animal} 같니?",
                                               pos_bhv="do_joy_B", pos="파이보도 용감하고 씩씩해지고 싶다!",
                                               neu_bhv="do_compliment_S", neu="몰라도 괜찮아.",
                                               act_bhv="do_joy_B", act="파이보도 용감하고 씩씩해지고 싶다!")
        
        # 4. 마무리 대화
        pibo = cm.tts(bhv="do_joy_A", string=f"친구들을 지켜주는 {wm.word(animal, 2)} 정말 멋있어! 다음에 또 재미있는 역할놀이 하자.")
        
        
        
        # 3. 피드백 수집
        time.sleep(1)                   
        pibo = cm.tts(bhv="do_question_S", string="파이보랑 얘기한 거 재미있었어? 재밌었는지, 별로였는지 얘기해줄래?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"파이보랑 얘기한 거 재미있었어?")

        pibo = cm.tts(bhv="do_joy_A", string=f"나랑 놀아줘서 고마워.") 
              
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
    
    rop = Roleplay()
    rop.Strong()