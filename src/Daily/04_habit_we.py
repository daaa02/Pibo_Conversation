# -*- coding: utf-8 -*-

# 일상-주말 생활 습관 대화

import os, sys
import re
import random
from datetime import date

sys.path.append('/home/kiro/workspace/Conversation_Scenarios/')
from data.conversation_manage import ConversationManage, WordManage
from data.speech_to_text import speech_to_text
from data.text_to_speech import TextToSpeech, text_to_speech

cm = ConversationManage()
wm = WordManage()
audio = TextToSpeech()


class Daily():    
    
    def __init__(self): 
        self.user_name = '다영'