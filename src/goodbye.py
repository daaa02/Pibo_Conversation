# -*- coding: utf-8 -*-

# 헤어짐 시나리오

import os, sys
import re
import random

# sys.path.append('/home/kiro/workspace/Conversation_Scenarios/')
sys.path.append('/home/pi/Pibo_Conversation/')
from data.conversation_manage import ConversationManage, WordManage
from data.speech_to_text import speech_to_text
from data.text_to_speech import TextToSpeech, text_to_speech

cm = ConversationManage()
wm = WordManage()
audio = TextToSpeech()

class Say():
    
    def __init__(self):
        self.user_name = '가영'
        
    
    def Goodbye(self):

        cm.tts(bhv="do_sad", string=f"{wm.word(self.user_name, 4)}, 나는 내일 집에 가야해. ")

        cm.tts(bhv="do_question_L", string=f"나는 {wm.word(self.user_name, 0)}랑 같이 놀고, 이야기 나눈 시간들이 정말 즐거웠어! {wm.word(self.user_name, 0)}는 어땠니?")
        answer = cm.responses_proc(pos_bhv="do_question_L", pos=f"나랑 무슨 놀이를 하는 게 가장 재미있었니?",
                                   neu_bhv="do_question_L", neu=f"나랑 무슨 놀이를 하는 게 가장 재미있었니?",
                                   neg_bhv="do_question_L", neg=f"나랑 무슨 놀이를 하는 게 가장 재미있었니?",
                                   act_bhv="do_question_L", act=f"나랑 무슨 놀이를 하는 게 가장 재미있었니?")

        answer = cm.responses_proc(pos_bhv="do_question_L", pos=f"그럼 나랑 어떤 이야기를 했던 게 기억에 남니?",
                                   neu_bhv="do_question_L", neu=f"그럼 나랑 어떤 이야기를 했던 게 기억에 남니?",
                                   neg_bhv="do_question_L", neg=f"그럼 나랑 어떤 이야기를 했던 게 기억에 남니?",
                                   act_bhv="do_question_L", act=f"그럼 나랑 어떤 이야기를 했던 게 기억에 남니?")

        answer = cm.responses_proc(pos_bhv="do_question_L", pos=f"다음에 나랑 또 만나면 어떤 걸 하고 싶니?",
                                   neu_bhv="do_question_L", neu=f"다음에 나랑 또 만나면 어떤 걸 하고 싶니?",
                                   neg_bhv="do_question_L", neg=f"다음에 나랑 또 만나면 어떤 걸 하고 싶니?",
                                   act_bhv="do_question_L", act=f"다음에 나랑 또 만나면 어떤 걸 하고 싶니?")

        answer = cm.responses_proc(pos_bhv="do_agree", pos=f"이야기 해줘서 고마워!",
                                   neu_bhv="do_agree", neu=f"이야기 해줘서 고마워!",
                                   neg_bhv="do_agree", neg=f"이야기 해줘서 고마워!",
                                   act_bhv="do_agree", act=f"이야기 해줘서 고마워!")

        cm.tts(bhv="do_joy_A", string=f"우리 모두 다음에 만나는 날까지 쑥쑥 자라도록 하자. 안녕~!")


if __name__ == "__main__":
    
    say = Say()
    say.Goodbye()   
