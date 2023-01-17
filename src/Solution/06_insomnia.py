# -*- coding: utf-8 -*-

# 문제해결-잠이 안와

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


class Solution():    
    
    def __init__(self): 
        self.user_name = '다영'
                
        
    def Insomnia(self):
        
        # 1.1 문제 제시
        cm.tts(bhv="do_sad", string="요즘 밤에 잠이 안 와.")
        
        # 1.2 경험 질문
        cm.tts(bhv="do_sad", string=f"{wm.word(self.user_name, 0)}는 보통 몇 시에 잠을 자니?")
        answer = cm.responses_proc(re_bhv="do_sad", re_q=f"{wm.word(self.user_name, 0)}는 보통 몇 시에 잠을 자니?")    
    
        cm.tts(bhv="do_question_L", string="키가 크려면 몇시에 자야 할까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="키가 크려면 몇시에 자야 할까?",
                                   pos_bhv="do_explain_A", pos="일찍자면 키가 커지겠지?",
                                   neu_bhv="do_explain_A", neu="몰라도 괜찮아~ 아마 일찍자면 키가 커지겠지?",
                                   act_bhv="do_explain_A", act="일찍자면 키가 커지겠지?",)

        cm.tts(bhv="do_question_L", string="잠을 많이 못자면 다음날 기분이 어떠니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="잠을 많이 못자면 다음날 기분이 어떠니?",
                                   pos_bhv="do_agree", pos="많이 못자면 피곤하겠지?",
                                   neu_bhv="do_agree", neu="괜찮아~ 생각이 나지 않을 수 있어~ 많이 못자면 피곤하겠지?",
                                   act_bhv="do_agree", act="많이 못자면 피곤하겠지?")

        cm.tts(bhv="do_question_S", string=f"양을 세면 잠이 온다던데, {wm.word(self.user_name, 0)}는 잠이 안 올 때 어떻게 하니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"양을 세면 잠이 온다던데, {wm.word(self.user_name, 0)}는 잠이 안 올 때 어떻게 하니?",
                                   pos_bhv="do_compliment_S", pos="좋은 방법인 걸?",
                                   neu_bhv="do_agree", neu="괜찮아~ 모를 수도 있어~",
                                   act_bhv="do_agree", act="좋은 방법인 걸?")
            
        cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}는 평소에 어떤 꿈을 꾸니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}는 평소에 어떤  꿈을 꾸니?",
                                   pos_bhv="do_agree", pos="신기한 걸?",
                                   neu_bhv="do_agree", neu="괜찮아~ 생각이 나지 않을 수 있어~",
                                   act_bhv="do_agree", act="신기한 걸")
        
        cm.tts(bhv="do_question_L", string="눈을 계속 감고 상상을 하면 잠이 올까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="눈을 계속 감고 상상을 하면 잠이 올까?",
                                   pos_bhv="do_agree", pos="왠지 잠이 올 것만 같아!",
                                   neu_bhv="do_agree", neu="괜찮아~ 모를 수도 있어~ 눈을 감고 상상을 하면 왠지 잠이 올 것만 같아!",
                                   act_bhv="do_agree", act="왠지 잠이 올 것만 같아!")
        # 2.1 문제 해결
        cm.tts(bhv="do_joy_A", string="파이보도 이제 일찍 자도록 노력해야겠다~ 알려줘서 정말 고마워!")
                            
        
        
        
if __name__ == "__main__":
    
    sol = Solution()
    sol.Insomnia()