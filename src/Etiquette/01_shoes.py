# -*- coding: utf-8 -*-

# 사회기술-신발을 신고 의자에 올라가지 않아요

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
        self.user_name = "다영"
        self.ox = ''
        
        
    def Shoes(self):
        
        # 2.1 카드 대화
        # 정/오답과 부정/중립 답변을 가리는 방법, 정답과 오답을 가리는 방법은 아직 구체적이지 않음(221207)
        cm.tts(bhv="do_question_L", string="이 카드의 어린이는 무엇을 잘못했을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="이 카드의 어린이는 무엇을 잘못했을까?",
                                   neg_bhv="do_suggestion_S", neg="같이 다시 한번 볼까?",
                                   neu_bhv="do_suggestion_S", neu="같이 다시 한번 볼까?")

        correct = ['의자', '신발']        
        
        if answer[0] == "action":            
            
            for i in range(len(correct)):
                if correct[i] in answer[1]:
                    self.ox = "right"                    
            if len(self.ox) == 0:
                self.ox = "wrong ㅠㅠ"
              
            if self.ox == "right":
                print(self.ox)
                cm.tts(bhv="do_compliment_S", string="맞아! 아주 똑똑한 걸?")
            else:
                print(self.ox)
                cm.tts(bhv="do_suggestion_S", string="또 무엇을 잘못했을까?")
                answer = cm.responses_proc(re_bhv="do_suggestion_S", re_q="또 무엇을 잘못했을까?")
                
                if answer[0] == "action":        
                                
                    for i in range(len(correct)):
                        if correct[i] in answer[1]:
                            self.ox = "right"                    
                    if len(self.ox) == 0:
                        self.ox = "wrong ㅠㅠ"
                    
                    if self.ox == "right":
                        print(self.ox)
                        cm.tts(bhv="do_compliment_S", string="맞아! 아주 똑똑한 걸?")
                    else:
                        print(self.ox)
                        cm.tts(bhv="do_suggestion_S", string="같이 다시 한번 볼까?")
        
        cm.tts(bhv="do_explain_A", string="이 카드의 어린이는 신발을 신고 의자에 올라갔어.")
     
        # 2.2 경험 질문
        cm.tts(bhv="do_question_L", string="모두가 함께 사용하는 의자에는 어떤 것이 있을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="모두가 함께 사용하는 의자에는 어떤 것이 있을까?",
                                   neu_bhv="do_explain_B", neu="괜찮아. 생각이 안 날 수도 있어~ 버스나 지하철 의자도 모두가 함께 쓰는 의자야!")

        cm.tts(bhv="do_question_L", string="의자에 신발을 신고 올라가면 어떻게 될까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="의자에 신발을 신고 올라가면 어떻게 될까?",
                                   neu_bhv="do_explain_C", neu="괜찮아. 모를 수도 있어~ 의자가 더러워지겠지?",
                                   act_bhv="do_agree", act="의자가 더러워지겠지?")

        cm.tts(bhv="do_question_L", string="신발을 신고 의자에 올라간 사람을 본 적이 있니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="신발을 신고 의자에 올라간 사람을 본 적이 있니?",
                                   pos_bhv="do_agree", pos="본 적이 있구나!",
                                   neu_bhv="do_agree", neu="괜찮아. 기억이 안 날 수도 있어~")
        
        cm.tts(bhv="do_question_L", string="신발을 신고 의자에 올라가면 다른 사람들이 어떻게 생각할까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="신발을 신고 의자에 올라가면 다른 사람들이 어떻게 생각할까?",
                                   neu_bhv="do_explain_B", neu="괜찮아. 모를 수도 있어~ 아마 다른 사람들은 지저분해진 의자에 앉지 못해서 속상할거야.",
                                   act_bhv="do_agree", act="다른 사람들은 지저분해진 의자에 앉지 못해서 속상할거야.")
        
        # 3.1 마무리 대화
        cm.tts(bhv="do_joy_A", string="모두가 함께 쓰는 의자는 깨끗하게 써야 해. 잘 기억해 두자!")
                            
                            
                            
                            
if __name__ == "__main__":
    
    etq = Etiquette()
    etq.Shoes()