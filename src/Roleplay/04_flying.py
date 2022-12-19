# -*- coding: utf-8 -*-

# 역할놀이-비행하는 존재

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
        
    
    def Flying(self):
        
        # 1. 역할 알림
        
        



if __name__ == "__main__":
    
    rop = Roleplay()
    rop.Flying()