# -*- coding: utf-8 -*-

# 사회기술-박물관의 전시물을 만지지 않아요

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


class Etiquette():    
    
    def __init__(self): 
        self.user_name = '다영'
        self.correct = ['친구', '행동', '싫어', '계속']
        self.ox = ''
                
        
    def Friend1(self):
        
        # 2.1 카드 대화
        cm.tts(bhv="do_question_L", string="이 카드의 어린이는 무엇을 잘못했을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="이 카드의 어린이는 무엇을 잘못했을까?",
                                   neg_bhv="do_suggestion_S", neg="같이 다시 한번 볼까?",
                                   neu_bhv="do_suggestion_S", neu="같이 다시 한번 볼까?")             
        
        if answer[0] == "action":            
            
            for i in range(len(self.correct)):
                if self.correct[i] in answer[1]:
                    self.ox = "(right)"                    
            if len(self.ox) == 0:
                self.ox = "(wrong ㅠㅠ)"
              
            if self.ox == "(right)":
                print(self.ox)
                cm.tts(bhv="do_compliment_S", string="맞아! 아주 똑똑한 걸?")
            else:
                print(self.ox)
                cm.tts(bhv="do_suggestion_S", string="또 무엇을 잘못했을까?")
                answer = cm.responses_proc(re_bhv="do_suggestion_S", re_q="또 무엇을 잘못했을까?")
                
                if answer[0] == "action":        
                                
                    for i in range(len(self.correct)):
                        if self.correct[i] in answer[1]:
                            self.ox = "(right)"                    
                    if len(self.ox) == 0:
                        self.ox = "(wrong ㅠㅠ)"
                    
                    if self.ox == "(right)":
                        print(self.ox)
                        cm.tts(bhv="do_compliment_S", string="맞아! 아주 똑똑한 걸?")
                    else:
                        print(self.ox)
                        cm.tts(bhv="do_suggestion_S", string="같이 다시 한번 볼까?")
        
        cm.tts(bhv="do_explain_A", string="이 카드의 어린이는 친구가 싫어하는 행동을 계속 하네.")
     
        # 2.2 경험 질문
        cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}는 어떤 행동을 싫어하니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}는 어떤 행동을 싫어하니?",
                                   act_bhv="do_agree", act="그 행동을 싫어하는구나!")

        if answer[0] == "action":   # '그 행동' 이길래 그냥 옵션 답변으로 변경함 (22/12/09)
            cm.tts(bhv="do_question_L", string=f"친구가 그 행동을 계속하면 {wm.word(self.user_name, 0)}는 기분이 어때?")
            answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}는 기분이 어때?",
                                    act_bhv="do_agree", act="나도 그렇게 생각해!")
            
        cm.tts(bhv="do_question_L", string="싫어하는 행동을 계속 하는 친구와 같이 놀고 싶을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="싫어하는 행동을 계속 하는 친구와 같이 놀고 싶을까?",
                                   neg_bhv="do_agree", neg="그렇지? 나도 그렇게 생각해~",
                                   act_bhv="do_agree", act="그렇지? 나도 그렇게 생각해~")

        # 2.3 문제 인식
        cm.tts(bhv="do_question_L", string="싫어하는 행동은 사람마다 다 달라. 친구가 싫어하는 행동을 계속하면 친구는 어떤 기분일까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="전시물을 만져서 망가지면 어떤 일이 일어날까?",
                                   pos_bhv="do_agree", pos="그 친구는 화가 날 수도 있겠지?",
                                   neu_bhv="do_explain_A", neu="괜찮아 모를 수도 있어~ 그 친구는 화가 날 수도 있겠지?",
                                   neg_bhv="do_agree", neg="그 친구는 화가 날 수도 있겠지?",
                                   act_bhv="do_agree", act="그 친구는 화가 날 수도 있겠지?")
    
        # 3.1 마무리 대화
        cm.tts(bhv="do_joy_A", string="다른 친구가 싫어하는 행동을 하는 건 좋지 않은 것 같아. 친구랑 사이좋게 지낼 수 있도록 노력하자~")
    
        
        
        
if __name__ == "__main__":
    
    etq = Etiquette()
    etq.Friend1()