# -*- coding: utf-8 -*-

# 마법을 부리는 존재 시나리오

import os, sys
import re
import random

sys.path.append('/home/kiro/workspace/Conversation_Scenarios/')
from data.conversation_manage import ConversationManage, WordManage
from data.speech_to_text import speech_to_text
from data.text_to_speech import TextToSpeech, text_to_speech

cm = ConversationManage()
wm = WordManage()
audio = TextToSpeech()


class Roleplay():    
    
    def __init__(self): 
        self.user_name = '다영'
        
    
    def Strong(self):
        
        # 1. 역할 알림
        cm.tts(bhv="do_suggestion_S", string="역할 놀이를 해볼까?")
        cm.tts(bhv="do_suggestion_S", string="오늘은 크로 힘이 센 역할을 해보자~")
        
        # 2. 역할 놀이 (1 of 3)
        rand = random.randrange(1,4) 
        
        if rand == 1:   # 사자
            cm.tts(bhv="do_suggestion_S", string="이제 우리는 동물의 왕 사자야!")
        
        if rand == 2:   # 늑대
            cm.tts(bhv="do_suggestion_S", string="이제 우리는 재빠른 늑대야!")
        
        if rand == 3:   # 호랑이
            cm.tts(bhv="do_suggestion_S", string="이제 우리는 용감한 호랑이야!")
        
        
        # 3. 대화 시작 (3 of 6)
        rand = random.randrange(1,7) 
        
        
        
        
        
if __name__ == "__main__":
    
    rop = Roleplay()
    rop.Badword()