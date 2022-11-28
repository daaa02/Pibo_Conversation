# -*- coding: utf-8 -*-

# 역할 놀이-되고 싶은 인물

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


class RolePlay():    
    
    def __init__(self): 
        self.user_name = "다영"
        self.rolemodel = ''
        

    def RoleModel(self):
        
        # 1.1 역할 알림
        text_to_speech(f"역할 놀이를 해볼까? {wm.word(self.user_name, type=0)}가 원하는 사람이 되어볼거야!")
        
        # 2.1 역할놀이(1)
        text_to_speech(f"파이보는 커서 과학자가 되고 싶어! {wm.word(self.user_name, type=0)}는 뭐가 되고 싶니?")
        
        while True:
            answer = cm.responses_proc(re_q=f"{wm.word(self.user_name, type=0)}는 뭐가 되고 싶니?")
            
            if answer == "neutral":
                text_to_speech(f"괜찮아~ 바로 떠오르지 않을 수도 있어~ 소방관, 의사, 디자이너, 화가 등이 있어~ {wm.word(self.user_name, type=0)}는 뭐가 되고 싶니?")
                continue
            
            elif answer != "neutral":
                self.rolemodel = "돌멩이"   # NER
                
                text_to_speech(f"{self.rolemodel} 맞아?")
                answer = cm.responses_proc(re_q=f"{self.rolemodel} 맞아?")

                if answer == "positive":
                    break
                
                elif answer == "negative":
                    text_to_speech("다시 크게 말해줄래?")
                    continue
        
        # 3.1 역할 대화
        text_to_speech(f"{wm.word(self.rolemodel, type=2)} 정말 중요한 일을 한다고 생각해")
        
        text_to_speech(f"{wm.word(self.user_name, type=0)}는 가장 유명한 {wm.word(self.rolemodel, type=3)} 아니?")
        answer = cm.responses_proc(re_q=f"{wm.word(self.user_name, type=0)}는 가장 유명한 {wm.word(self.rolemodel, type=3)} 아니?",
                                   neu="몰라도 괜찮아~")
        
        if answer == "positive":
            text_to_speech("그 사람은 왜 유명할까?")
            answer = cm.responses_proc(re_q="그 사람은 왜 유명할까?")
            
        text_to_speech(f"{wm.word(self.user_name, type=0)}의 주변에 {wm.word(self.rolemodel, type=1)} 있니?")
        answer = cm.responses_proc(re_q="주변에 있니?",
                                   neu="괜찮아~ 생각 나지 않을 수 있어")
        
        if answer == "positive":
            text_to_speech("그 사람은 누구니?")
            answer = cm.responses_proc(re_q="그 사람은 누구니?")
            
        text_to_speech(f"{wm.word(self.rolemodel, type=3)} 생각하면 무슨 색이 떠올라?")
        answer = cm.responses_proc(re_q=f"{wm.word(self.user_name, type=3)} 생각하면 무슨 색이 떠올라?",
                                   neu="괜찮아~ 바로 떠오르지 않을 수도 있어")
        
        if answer == "positive":
            text_to_speech("그 색깔이 왜 떠올랐을까?")
            answer = cm.responses_proc(re_q="그 색깔이 왜 떠올랐을까?")
            
        text_to_speech(f"{wm.word(self.user_name, type=0)}가 {wm.word(self.rolemodel, type=1)} 된다면 뭘 하고 싶니?")
        answer = cm.responses_proc(re_q=f"{wm.word(self.rolemodel, type=1)} 된다면 뭘 하고 싶니?",
                                   neu="괜찮아~ 대답하기 어려울 수 있어")
        
        if answer == "positive":
            text_to_speech("그렇게 생각한 이유는 뭐야?")
            answer = cm.responses_proc(re_q="그렇게 생각한 이유는 뭐야?")
        
        # 4.1 마무리 대화
        text_to_speech(f"{wm.word(self.user_name, type=0)}가 되고 싶은 역할 놀이를 해서 너무 재미있었어!")
        text_to_speech("다음에 또 하자!")
        
        
        
if __name__ == "__main__":
    rp = RolePlay()
    rp.RoleModel()