# -*- coding: utf-8 -*-

# 동화-소금 장수와 당나귀

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


class Fairytale():    
    
    def __init__(self): 
        self.user_name = '다영'
        
        
    def Salt(self):
        
        # 1. 동화 줄거리 대화
        cm.tts(bhv="do_joy_A", string=f"정말 재미있는 이야기였어! {wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?")
        answer = cm.responses_proc(re_bhv="do_joy_A", re_q=f"{wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?",
                                   neu_bhv="do_agree", neu=f"그럴 수 있지~")
        
        cm.tts(bhv="do_question_L", string=f"동화 속 소금 장수와 당나귀는 어디를 가는 길이었을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"동화 속 소금 장수와 당나귀는 어디를 가는 길이었을까?", 
                                   neu_bhv="do_agree", neu=f"모를 수 있지~")

        cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}도 유치원 갈 때 가방을 매고 가니? ")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}도 유치원 갈 때 가방을 매고 가니? ", 
                                   pos_bhv="do_question_S", pos=f"{wm.word(self.user_name, 0)} 가방 안에 어떤 것들이 들어있니?")
        
        if answer[0] == "positive":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)} 가방 안에 어떤 것들이 들어있니?")
                
        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}가 말한 것들 말고 유치원에 가져 가고 싶은 물건이 있다면 말해줄래?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}가 말한 것들 말고 유치원에 가져 가고 싶은 물건이 있다면 말해줄래?", 
                                   pos_bhv="do_question_S", pos=f"그거 가지고 유치원에 가서 뭐하고 싶어?", 
                                   neu_bhv="do_agree", neu=f"몰라도 괜찮아~", 
                                   act_bhv="do_question_S", act=f"그거 가지고 유치원에 가서 뭐하고 싶어?")

        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"그거 가지고 유치원에 가서 뭐하고 싶어?")            
        
        # 2. 등장인물 공감 대화
        cm.tts(bhv="do_question_L", string=f"소금 장수는 당나귀에게 속았다고 생각했을 때 소금 장수는 짜증 났을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"소금 장수는 당나귀에게 속았다고 생각했을 때 소금 장수는 짜증 났을까?", 
                                   pos_bhv="do_question_L", pos=f"{wm.word(self.user_name, 0)}도 누가 {wm.word(self.user_name, 0)}를 속여서 짜증났던 적이 있다면 이야기해 줄래?", 
                                   act_bhv="do_question_L", act=f"{wm.word(self.user_name, 0)}도 누가 {wm.word(self.user_name, 0)}를 속여서 짜증났던 적이 있다면 이야기해 줄래?")

        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_L ", re_q=f"{wm.word(self.user_name, 0)}도 누가 {wm.word(self.user_name, 0)}를 속여서 짜증났던 적이 있다면 이야기해 줄래?", 
                                       act_bhv="do_agree", act=f"그런 일이 있었구나! 정말 짜증났었겠다! ")

        cm.tts(bhv="do_question_L", string=f"당나귀가 꾀를 부려 짐이 훨씬 더 무거워 졌을 때 당나귀는 후회했겠지?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"당나귀가 꾀를 부려 짐이 훨씬 더 무거워 졌을 때 당나귀는 후회했겠지?", 
                                   pos_bhv="do_question_S", pos=f"{wm.word(self.user_name, 0)}도 후회 했던 적이 있었다면 이야기해 줄래?", 
                                   act_bhv="do_question_S", act=f"{wm.word(self.user_name, 0)}도 후회 했던 적이 있었다면 이야기해 줄래?")

        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}도 후회 했던 적이 있었다면 이야기해 줄래?", 
                                       act_bhv="do_sad", act=f"그런 일이 있었구나! 정말 속상했겠다!")

        # 3. 마무리 대화
        cm.tts(bhv="do_suggestion_L", string=f"만약 {wm.word(self.user_name, 0)}가 게으름 피우는 당나귀를 만난다면 뭐라고 해줄 수 있을까?")
        answer = cm.responses_proc(re_bhv="do_suggestion_L", re_q=f"만약 {wm.word(self.user_name, 0)}가 게으름 피우는 당나귀를 만난다면 뭐라고 해줄 수 있을까?", 
                                   pos_bhv="do_agree", pos=f"{wm.word(self.user_name, 0)}는 그렇게 말해주고 싶구나!", 
                                   neu_bhv="do_agree", neu=f"괜찮아~ 모를 수 있지~", 
                                   neg_bhv="do_agree", neg=f"{wm.word(self.user_name, 0)}는 그렇게 말해주고 싶구나!", 
                                   act_bhv="do_agree", act=f"{wm.word(self.user_name, 0)}는 그렇게 말해주고 싶구나!")
        
        cm.tts(bhv="do_explain_C", string=f"오늘 동화 재미있었지? 다음에 또 재미있는 동화 들려줄게~")
            
        


if __name__ == "__main__":    
    
    fat = Fairytale()
    fat.Salt()