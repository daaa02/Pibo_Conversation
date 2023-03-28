# -*- coding: utf-8 -*-

# 사회기술-신발을 신고 의자에 올라가지 않아요

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
        self.user_name = '가영'
        self.correct = ['신발']  
        self.ox = ''
        
        
    def Shoes(self):
        
        # 2.1 카드 대화
        # 정/오답과 부정/중립 답변을 가리는 방법, 정답과 오답을 가리는 방법은 아직 구체적이지 않음(221207)
        cm.tts(bhv="do_question_L", string="이 카드의 어린이는 무엇을 잘못했을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="이 카드의 어린이는 무엇을 잘못했을까?",
                                   neg_bhv="do_suggestion_S", neg="같이 다시 한번 볼까?",
                                   neu_bhv="do_suggestion_S", neu="같이 다시 한번 볼까?")
        
        if answer[0][0] == "action":            
            
            for i in range(len(self.correct)):
                if self.correct[i] in answer[1]:
                    self.ox = "right"                    
            if len(self.ox) == 0:
                self.ox = "wrong ㅠㅠ"
              
            if self.ox == "right":
                print(self.ox)
                cm.tts(bhv="do_compliment_S", string="맞아! 아주 똑똑한 걸?")
            else:
                print(self.ox)
                cm.tts(bhv="do_question_S", string="또 무엇을 잘못했을까?")
                answer = cm.responses_proc(re_bhv="do_question_S", re_q="또 무엇을 잘못했을까?")
                
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
        
        cm.tts(bhv="do_explain_A", string="이 카드의 어린이는 신발을 신고 의자에 올라갔어.")
     
        # 2.2 경험 질문
        cm.tts(bhv="do_question_L", string="모두가 함께 사용하는 의자에는 어떤 것이 있을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="모두가 함께 사용하는 의자에는 어떤 것이 있을까?",
                                   neu_bhv="do_explain_B", neu="괜찮아. 생각이 안 날 수도 있어~ 버스나 지하철 의자도 모두가 함께 쓰는 의자야!")

        cm.tts(bhv="do_question_L", string="의자에 신발을 신고 올라가면 어떻게 될까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="의자에 신발을 신고 올라가면 어떻게 될까?",
                                   neu_bhv="do_explain_C", neu="괜찮아. 모를 수도 있어~ 의자가 더러워지겠지?",
                                   act_bhv="do_agree", act="의자가 더러워지겠지?")

        cm.tts(bhv="do_question_L", string="신발을 신고 의자에 올라간 사람을 본 적이 있니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="신발을 신고 의자에 올라간 사람을 본 적이 있니?",
                                   pos_bhv="do_agree", pos="본 적이 있구나!",
                                   neu_bhv="do_agree", neu="괜찮아. 기억이 안 날 수도 있어~")
        
        # 2.3 문제 인식
        cm.tts(bhv="do_question_L", string="신발을 신고 의자에 올라가면 다른 사람들이 어떻게 생각할까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="신발을 신고 의자에 올라가면 다른 사람들이 어떻게 생각할까?",
                                   neu_bhv="do_explain_B", neu="괜찮아. 모를 수도 있어~ 아마 다른 사람들은 지저분해진 의자에 앉지 못해서 속상할거야.",
                                   act_bhv="do_agree", act="다른 사람들은 지저분해진 의자에 앉지 못해서 속상할거야.")
        
        # 3.1 마무리 대화
        cm.tts(bhv="do_joy_A", string="모두가 함께 쓰는 의자는 깨끗하게 써야 해. 잘 기억해 두자!")
                            
                            
                            
                            
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
    etq.Shoes()