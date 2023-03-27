# -*- coding: utf-8 -*-

# 사회기술-박물관의 전시물을 만지지 않아요

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


class Etiquette():    
    
    def __init__(self): 
        self.user_name = '가영'
        self.correct = ['만지', '만졌', '전시물', '작품']
        self.ox = ''
                
        
    def Museum(self):
        
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
        
        cm.tts(bhv="do_explain_A", string="이 카드의 어린이는 박물관에 있는 전시물을 마음대로 만졌어.")
     
        # 2.2 경험 질문
        cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}도 박물관이나 미술관에 가 본 적이 있니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="어디에 가면 가지런히 정리된 물건들을 볼 수 있니?",
                                   neu_bhv="do_explain_B", neu="괜찮아 생각이 안 날 수도 있어~ 마트나 문방구에 가면 물건들이 정리되어 있지?")

        cm.tts(bhv="do_question_L", string="박물관에 가면 어떤 주의사항이 적혀 있니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="박물관에 가면 어떤 주의사항이 적혀 있니?",
                                   pos_bhv="do_agree", pos="박물관에는 ‘만지지 마시오’ 라는 주의사항이 붙어 있지?",
                                   neu_bhv="do_explain_C", neu="괜찮아. 모를 수도 있어~ 박물관에는 ‘만지지 마시오’ 라는 주의사항이 붙어 있어.",
                                   act_bhv="do_agree", act="박물관에는 ‘만지지 마시오’ 라는 주의사항이 붙어 있지?")
            
        cm.tts(bhv="do_question_L", string="박물관의 전시물을 만지면 어떤 일이 일어날까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="박물관의 전시물을 만지면 어떤 일이 일어날까?",
                                   pos_bhv="do_agree", pos="전시물을 마음대로 만지면 전시물이 망가질 수도 있겠지?",
                                   neu_bhv="do_explain_B", neu="괜찮아. 기억이 안 날 수도 있어~ 전시물을 마음대로 만지면 전시물이 망가질 수도 있겠지?",
                                   act_bhv="do_agree", act="전시물을 마음대로 만지면 전시물이 망가질 수도 있겠지?")

        # 2.3 문제 인식
        cm.tts(bhv="do_question_L", string="전시물을 만져서 망가지면 어떤 일이 일어날까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="전시물을 만져서 망가지면 어떤 일이 일어날까?",
                                   pos_bhv="do_agree", pos="망가뜨린 사람이 돈을 지불해야 할 수도 있고, 전시물을 보지 못한 다른 사람들은 화가 날 수도 있겠지?",
                                   neu_bhv="do_explain_A", neu="괜찮아 모를 수도 있어~ 망가뜨린 사람이 돈을 지불해야 할 수도 있고, 전시물을 보지 못한 다른 사람들은 화가 날 수도 있겠지?",
                                   act_bhv="do_agree", act="망가뜨린 사람이 돈을 지불해야 할 수도 있고, 전시물을 보지 못한 다른 사람들은 화가 날 수도 있겠지?")
    
        # 3.1 마무리 대화
        cm.tts(bhv="do_joy_A", string="멋진 전시물은 모든 사람들이 오래오래 볼 수 있도록 눈으로만 봐야 해. 잘 기억해 두자!")
    
        
        
        
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
    etq.Museum()