# -*- coding: utf-8 -*-

# 일상-자기 전 감정 대화

import os, sys
import re
import random

sys.path.append('/home/kiro/workspace/Conversation_Scenarios/data')
from conversation_manage import ConversationManage, WordManage
from speech_to_text import speech_to_text
from text_to_speech import TextToSpeech, text_to_speech

cm = ConversationManage()
wm = WordManage()
audio = TextToSpeech()


class Daily():    
    
    def __init__(self): 
        self.user_name = "다영"

    
    def Bedtime(self):
        
        # 1.1 시간 알림
        rand_list = ["벌써 어두운 밤이 되었어~", "하루가 빨리 지나갔지?", "좋은 하루 보냈니?"]
        text_to_speech(random.choice(rand_list))
        
        # 1.2 점수 파악 ~ 1.3 대화 시작
        text_to_speech("오늘의 기분을 감정 단어로 말해볼까?")
        text_to_speech("기분이 좋다면 좋아. 보통이면 평범해. 안 좋았다면 안 좋았어 라고 말할 수 있어!")
        answer = cm.responses_proc(re_q="오늘의 기분을 감정 단어로 말해볼까?", 
                                pos="오늘 좋은 일이 있다면 말해줄래?",
                                neu=f"오늘 하루도 고생 많았어. 내일은 좋은 일이 가득할거야~ {wm.word(self.user_name, type=4)} 잘 자!",
                                neg="오늘 무슨 일 있었다면 말해 줄래?", 
                                act="오늘 재미있는 일이 있었다면 말해줄래?")
        
        if answer == "neutral":
            sys.exit(0)        
    
        answer = cm.responses_proc(re_q="오늘 있었던 일 말해줄 수 있어?",
                                pos="어떤 일이 있었니?",
                                neu=f"시간이 벌써 이렇게 됐네! 어서 자야겠는 걸? {wm.word(self.user_name, type=4)} 잘 자!",
                                neg=f"오늘 하루도 고생 많았어. 내일은 좋은 일이 가득할거야~ {wm.word(self.user_name, type=4)} 잘 자!",
                                act=f"시간이 벌써 이렇게 됐네! 어서 자야겠는 걸? {wm.word(self.user_name, type=4)} 잘 자!")

        if answer == "positive":
            answer = cm.responses_proc(re_q="어떤 일이 있었니?",
                                    pos=f"정말 기분 좋은 일이었겠는걸?",
                                    neg=f"정말 기분 안 좋았을 것 같아. 너무 우울해하지 마.",
                                    act=f"재밌었겠다!")
            
            text_to_speech(f"활기찬 내일을 위해 오늘은 이만 자자~ {wm.word(self.user_name, type=4)} 잘 자!")

        
if __name__ == "__main__":
    day = Daily()
    day.Bedtime()
    