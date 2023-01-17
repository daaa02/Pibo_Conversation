# -*- coding: utf-8 -*-

# 역할놀이-날씨를 나타내는 존재

import os, sys
import re
import random

sys.path.append('/home/kiro/workspace/Conversation_Scenarios/')
# sys.path.append('/home/pi/Pibo_Conversation/')
from data.conversation_manage import ConversationManage, WordManage
from data.speech_to_text import speech_to_text
from data.text_to_speech import TextToSpeech, text_to_speech

cm = ConversationManage()
wm = WordManage()
audio = TextToSpeech()


class Roleplay():    
    
    def __init__(self): 
        self.user_name = '다영'
        self.count = 0
        
    
    def Flying(self):
        
        # 1. 역할 알림
        cm.tts(bhv="do_suggestion_S", string="역할 놀이를 해볼까?")
        cm.tts(bhv="do_suggestion_S", string="오늘은 날씨 역할을 해보자~ ") 
      
        # 4. 마무리 대화
        


if __name__ == "__main__":
    
    rop = Roleplay()
    rop.Flying()