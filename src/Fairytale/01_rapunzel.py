# -*- coding: utf-8 -*-

# 동화-라푼젤

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


class Fairytale():    
    
    def __init__(self): 
        self.user_name = '다영'
        
        
    def Rapunzel(self):
        
        # 1. 동화 줄거리 대화
        cm.tts(bhv="do_joy_A", string=f"정말 재미있는 이야기였어! {wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?")
        answer = cm.responses_proc(re_bhv="do_joy_A", re_q=f"정말 재미있는 이야기였어! {wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?",
                                   neu_bhv="do_agree", neu=f"그럴 수 있지~")
        
        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}는 아래가 내려다 보이는 높은 곳에 가본 적이 있으면 말해줄래?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}는 아래가 내려다 보이는 높은 곳에 가본 적이 있으면 말해줄래?", 
                                   pos_bhv="do_question_S", pos=f"멋진 걸! 무섭진 않았니?", 
                                   neu_bhv="do_agree", neu=f"몰라도 괜찮아~")
        
        if answer[0] == "positive":
            answer = cm.responses_proc(bhv="do_question_S", re_q=f"무섭진 않았니?")
            
        cm.tts(bhv="do_question_S", string=f"주인공 라푼젤이 갇혀있던 탑은 얼마나 클까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"주인공 라푼젤이 갇혀있던 탑은 얼마나 클까?", 
                                   neu_bhv="do_question_S", neu=f"백화점만큼 엄청 클까?")

        if answer[0] == "neutral":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"백화점만큼 엄청 클까?",
                                       neu_bhv="do_agree", neu=f"모를 수 있지~")        
        
        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}가 라푼젤 이라면 성에서 어떤 놀이를 했을 것 같니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}가 라푼젤 이라면 성에서 어떤 놀이를 했을 것 같니?")
        
        # 2. 등장인물 공감 대화
        cm.tts(bhv="do_question_S", string=f"성에 갇혀 있던 라푼젤의 기분은 속상했을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"성에 갇혀 있던 라푼젤의 기분은 속상했을까?", 
                                   pos_bhv="do_question_S", pos=f"{wm.word(self.user_name, 0)}가 최근에 속상하다고 느낀 일이 있다면 말해줄래?",
                                   act_bhv="do_question_S", act=f"{wm.word(self.user_name, 0)}가 최근에 속상하다고 느낀 일이 있다면 말해줄래?")
        
        if answer[0] == "postive" or answer[0] == "action":
            cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}가 최근에 속상하다고 느낀 일이 있다면 말해줄래?")
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}는 최근에 속상하다고 느낀 일이 있다면 말해줄래?", 
                                       act_bhv="do_sad", act=f"그랬구나! 정말 속상했겠는 걸?")
        
        
        cm.tts(bhv="do_question_S", string=f"마법사에게 머리카락이 잘린 라푼젤의 기분은 어땠을 것 같니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"마법사에게 머리카락이 잘린 라푼젤의 기분은 어땠을 것 같니?",
                                   act_bhv="do_question_S", act=f"{wm.word(self.user_name, 0)}도 비슷한 기분을 느낀적이 있다면 이야기해 줄래?")
        
        if answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}도 비슷한 기분을 느낀적이 있다면 이야기해 줄래?", 
                                       act_bhv="do_agree", act=f"그런 일이 있었구나!")
            
        # 3. 마무리 대화
        cm.tts(bhv="do_suggestion_L", string=f"성에 갇혀 있던 라푼젤에게  {wm.word(self.user_name, 0)}가 위로를 해줘 볼까?")
        answer = cm.responses_proc(re_bhv="do_suggestion_L", re_q=f"성에 갇혀 있던 라푼젤에게  {wm.word(self.user_name, 0)}가 위로를 해줘 볼까?", 
                                   pos_bhv="do_agree", pos=f"{wm.word(self.user_name, 0)}는 그렇게 말해주고 싶구나!", 
                                   neu_bhv="do_agree", neu=f"괜찮아~ 위로를 하기 힘들 수 있어~", 
                                   act_bhv="do_agree", act=f"{wm.word(self.user_name, 0)}는 그렇게 말해주고 싶구나!")
        
        cm.tts(bhv="do_explain_C", string=f"다음에 또 재미있는 동화 들려줄게~")
            
        


if __name__ == "__main__":    
    
    fat = Fairytale()
    fat.Rapunzel()