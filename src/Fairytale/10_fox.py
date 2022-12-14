# -*- coding: utf-8 -*-

# 동화-여우와 나무꾼

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
                
        
    def Fox(self):
        
        # 1. 동화 줄거리 대화
        cm.tts(bhv="do_joy_A", string=f"정말 재미있는 이야기였어! {wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?")
        answer = cm.responses_proc(re_bhv="do_joy_A", re_q=f"{wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?",
                                   neu_bhv="do_agree", neu=f"그럴 수 있지~")
        
        cm.tts(bhv="do_question_L", string=f"나무꾼에게 도움을 청한 여우를 왜 숨겨주었다고 생각하니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"나무꾼에게 도움을 청한 여우를 왜 숨겨주었다고 생각하니?")

        cm.tts(bhv="do_question_L", string=f"나무꾼이 여우를 숨겨주지 않았다면 어떤 일이 일어났을까? ")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"나무꾼이 여우를 숨겨주지 않았다면 어떤 일이 일어났을까? ", 
                                   pos_bhv="do_agree", pos=f"그랬겠구나! ", 
                                   neu_bhv="do_agree", neu=f"몰라도 괜찮아~", 
                                   act_bhv="do_agree", act=f"그랬겠구나! ")

        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}도 숨바꼭질 같이 숨는 놀이를 해본 적이 있다면 이야기해줄래?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}도 숨바꼭질 같이 숨는 놀이를 해본 적이 있다면 이야기해줄래?", 
                                   pos_bhv="do_agree", pos=f"재밌었니?", 
                                   neu_bhv="do_agree", neu=f"괜찮아~ 대답하기 어려울 수 있어~", 
                                   act_bhv="do_agree", act=f"재밌었니?")

        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}도 숨바꼭질 같이 숨는 놀이를 해본 적이 있다면 이야기해줄래?", 
                                       pos_bhv="do_question_S", pos=f"그랬구나!", 
                                       act_bhv="do_question_S", act=f"그랬구나!")

        # 2. 등장인물 공감 대화
        cm.tts(bhv="do_question_S", string=f"사냥꾼과 사냥개 에게 쫓기고 있던 여우의 마음은 무서웠을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"사냥꾼과 사냥개 에게 쫓기고 있던 여우의 마음은 무서웠을까?", 
                                   pos_bhv="do_question_S", pos=f"{wm.word(self.user_name, 0)}는 무서웠던 적이 있니?", 
                                   neu_bhv="do_agree", neu=f"모를 수 있지~",
                                   act_bhv="do_question_S", act=f"{wm.word(self.user_name, 0)}는 무서웠던 적이 있니?")

        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}는 무서웠던 적이 있니?", 
                                       pos_bhv="do_agree", pos=f"그런일이 있었구나!", 
                                       act_bhv="do_agree", act=f"그런일이 있었구나!")

        cm.tts(bhv="do_question_L", string=f"잘 숨겨준 줄 알았던 나무꾼의 손짓을 보며 여우는 나무꾼이 미웠을까? ")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"잘 숨겨준 줄 알았던 나무꾼의 손짓을 보며 여우는 나무꾼이 미웠을까? ", 
                                   pos_bhv="do_question_L", pos=f"{wm.word(self.user_name, 0)}도 믿었지만 속상한 경험이 있었다면 이야기해 줄래?",
                                   act_bhv="do_question_L", act=f"{wm.word(self.user_name, 0)}도 믿었지만 속상한 경험이 있었다면 이야기해 줄래?")

        if answer[0] == "positive" or answer[0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}도 믿었지만 속상한 경험이 있었다면 이야기해 줄래?", 
                                       pos_bhv="do_agree", pos=f"그런 일이 있었구나!", 
                                       act_bhv="do_agree", act=f"그런 일이 있었구나!")


        # 3. 마무리 대화
        cm.tts(bhv="do_question_L", string=f"만약 {wm.word(self.user_name, 0)}가 여우를 속인 나무꾼을 만난다면 뭐라고 해줄 수 있을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"만약 {wm.word(self.user_name, 0)}가 여우를 속인 나무꾼을 만난다면 뭐라고 해줄 수 있을까?",  
                                   pos_bhv="do_agree", pos=f"그렇구나!",
                                   neu_bhv="do_agree", neu=f"괜찮아~ 대답하기 어려울 수 있어~ ",
                                   neg_bhv="do_agree", neg=f"그렇구나!",
                                   act_bhv="do_agree", act=f"그렇구나!")
        
        cm.tts(bhv="do_explain_C", string=f"다음에 또 재미있는 동화를 들려줄게~")
            
        


if __name__ == "__main__":    
    
    fat = Fairytale()
    fat.Fox()