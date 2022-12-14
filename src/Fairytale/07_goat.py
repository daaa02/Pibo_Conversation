# -*- coding: utf-8 -*-

# 동화-새끼염소와 늑대

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
                
        
    def Goat(self):
        
        # 1. 동화 줄거리 대화
        cm.tts(bhv="do_joy_A", string=f"정말 재미있는 이야기였어! {wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?")
        answer = cm.responses_proc(re_bhv="do_joy_A", re_q=f"{wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?",
                                   neu_bhv="do_agree", neu=f"그럴 수 있지~")
        
        cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}는 어떤 동물을 좋아하니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}는 어떤 동물을 좋아하니?", 
                                   pos_bhv="do_question_L", pos=f"그 동물은 어떻게 생겼는지 말해줄래?", 
                                   neu_bhv="do_agree", neu=f"몰라도 괜찮아~", 
                                   act_bhv="do_question_L", act=f"그 동물은 어떻게 생겼는지 말해줄래?")

        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"그 동물은 어떻게 생겼는지 말해줄래?", 
                                       neu_bhv="do_agree", neu=f" 몰라도 괜찮아~")

        cm.tts(bhv="do_question_S", string=f"염소랑 늑대가 달리기를 하면 누가 더 빠를 것 같니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"염소랑 늑대가 달리기를 하면 누가 더 빠를 것 같니?")

        cm.tts(bhv="do_question_S", string=f"사냥개 몇 마리가 늑대를 쫓아갔을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"사냥개 몇 마리가 늑대를 쫓아갔을까?", 
                                   act_bhv="do_agree", act=f"그렇게 생각하는구나!")
        
        # 2. 등장인물 공감 대화
        cm.tts(bhv="do_question_S", string=f"새끼염소가 늑대한테 쫓겼을 때 무서웠을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"새끼염소가 늑대한테 쫓겼을 때 무서웠을까?", 
                                   pos_bhv="do_question_L", pos=f"{wm.word(self.user_name, 0)}가 최근에 무섭다고 느낀 적이 있다면 말해줄래?", 
                                   act_bhv="do_question_L", act=f"{wm.word(self.user_name, 0)}가 최근에 무섭다고 느낀 적이 있다면 말해줄래?")

        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}가 최근에 무섭다고 느낀 적이 있다면 말해줄래?",
                                       pos_bhv="do_agree", pos=f"그랬구나! 정말 무서웠겠다!", 
                                       act_bhv="do_agree", act=f"그랬구나! 정말 무서웠겠다!")

        cm.tts(bhv="do_question_L", string=f"사냥개들이 새끼 염소를 구해줬을 때 새끼 염소 기분이 기뻤을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"사냥개들이 새끼 염소를 구해줬을 때 새끼 염소 기분이 기뻤을까?", 
                                   pos_bhv="do_question_L", pos=f"{wm.word(self.user_name, 0)}가 도움을 받고 기뻤던 적이 있다면 이야기해 줄래?", 
                                   neu_bhv="do_agree", neu=f" 몰라도 괜찮아~", 
                                   act_bhv="do_question_L", act=f"{wm.word(self.user_name, 0)}가 도움을 받고 기뻤던 적이 있다면 이야기해 줄래?")

        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}가 도움을 받고 기뻤던 적이 있다면 이야기해 줄래?", 
                                       pos_bhv="do_agree", pos=f"그런 일이 있었구나! 정말 기뻤겠다!", 
                                       act_bhv="do_agree", act=f"그런 일이 있었구나! 정말 기뻤겠다!")


        # 3. 마무리 대화
        cm.tts(bhv="do_question_L", string=f"만약 {wm.word(self.user_name, 0)}가 늑대를 무서워하는 새끼 염소를 만난다면 뭐라고 해줄 수 있을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}가 다양한 모험을 하고 집으로 돌아온 엄지 둥이 에게 위로를 해줘볼까?",  
                                   pos_bhv="do_agree", pos=f"그렇구나!",
                                   neu_bhv="do_agree", neu=f"괜찮아~ 모를 수 있지~",
                                   neg_bhv="do_agree", neg=f"그렇구나!",
                                   act_bhv="do_agree", act=f"그렇구나!")
        
        cm.tts(bhv="do_explain_C", string=f"다음에 또 재미있는 동화를 들려줄게~")
            
        


if __name__ == "__main__":    
    
    fat = Fairytale()
    fat.Goat()