# -*- coding: utf-8 -*-

# 문제해결-모르는게 많아

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
                
        
    def Idk(self):
        
        # 1.1 문제 제시
        cm.tts(bhv="do_sad", string="파이보는 모르는게 너무 많은 것 같아서 슬퍼.")
        
        # 1.2 경험 질문
        cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}도 잘 몰라서 속상했던 적이 있니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}도 잘 몰라서 속상했던 적이 있니?",
                                   pos_bhv="do_sad", pos=f"{wm.word(self.user_name, 0)}도 속상했겠다.",
                                   neu_bhv="do_agree", neu="괜찮아~ 생각이 나지 않을 수 있어~")                

        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}는 다른 친구들보다 어떤 걸 잘 모른다고 생각하니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}는 다른 친구들보다 어떤 걸 잘 모른다고 생각하니?")

        cm.tts(bhv="do_question_S", string="모르는게 생길 땐 주위 사람들에게 물어보는 것이 좋을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="모르는게 생길 땐 주위 사람들에게 물어보는 것이 좋을까?",
                                   neu_bhv="do_explain_C", neu="괜찮아~ 모를 수도 있어~")
        
        cm.tts(bhv="do_question_S", string="누구에게 물어보는것이 좋을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="누구에게 물어보는것이 좋을까?",
                                   pos_bhv="do_agree", pos="나도 그렇게 생각해!",
                                   neu_bhv="do_agree", neu="괜찮아~ 생각이 나지 않을 수 있어~",
                                   act_bhv="do_agree", act="나도 그렇게 생각해!")
        
        cm.tts(bhv="do_question_L", string=f"그럼 {wm.word(self.user_name, 0)}가 다른 친구들보다 어떤 걸 잘 안다고 생각하니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"그럼 {wm.word(self.user_name, 0)}가 다른 친구들보다 어떤 걸 잘 안다고 생각하니?",
                                   pos_bhv="do_agree", pos="그렇게 생각하는구나!",
                                   neu_bhv="do_agree", neu="괜찮아~ 모를 수도 있어~",
                                   act_bhv="do_agree", act="그렇게 생각하는구나!")
        
        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}가 잘 아는 부분은 친구들이 물어볼 때 가르쳐주면 좋겠지?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}가 잘 아는 부분은 친구들이 물어볼 때 가르쳐주면 좋겠지?",
                                   pos_bhv="do_compliment_S", pos=f"파이보는 {wm.word(self.user_name, 0)}가 잘 가르쳐 줄 거라고 생각해!",
                                   neu_bhv="do_explain_C", neu=f"몰라도 괜찮아~ 파이보는 {wm.word(self.user_name, 0)}가 잘 가르쳐 줄 거라고 생각해!",
                                   act_bhv="do_compliment_S", act=f"파이보는 {wm.word(self.user_name, 0)}가 잘 가르쳐 줄 거라고 생각해!")
        
        # 2.1 문제 해결
        cm.tts(bhv="do_joy_A", string="파이보도 이제 잘 모르는 것이 생기면 배우면 되니까 속상해하지 않아야겠다~ 알려줘서 정말 고마워!")
                            
        
        
        
if __name__ == "__main__":
    
    sol = Solution()
    sol.Idk()