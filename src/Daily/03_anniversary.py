# -*- coding: utf-8 -*-

# 일상-기념일 대화

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
        self.hbd_child = ''
        self.hbd_mom = ''
        self.hbd_dad = ''
        