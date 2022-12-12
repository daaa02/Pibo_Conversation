# -*- coding: utf-8 -*-

# 사회기술-가위나 칼은 손잡이가 있는 쪽으로 물건을 줘요

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
        self.correct = ['친구', '가위', '날', '주', '줄']
        self.ox = ''
                
        
    def Object2(self):
        
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
        
        cm.tts(bhv="do_explain_A", string="이 카드의 어린이는 날카로운 가위의 날 쪽을 다른 친구에게 주고 있어")
     
        # 2.2 경험 질문
        cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}는 가위나 칼을 사용하여 만들기를 해본 적이 있니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}는 가위나 칼을 사용하여 만들기를 해본 적이 있니?",
                                   pos_bhv="do_question_S", pos="어떤 걸 만들었니?")
        
        if answer[0] == "positive":
            answer = cm.responses_proc(re_bhv="do_question_S", re_q="어떤 걸 만들었니?",
                                       act_bhv="do_joy_A", act="그걸 만들었구나!")
            
            cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}는 다른 친구들에게 가위를 어떻게 건네 주니?")
            answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}는 다른 친구들에게 가위를 어떻게 건네 주니?",
                                       neu_bhv="do_explain_A", neu="몰라도 괜찮아~ 가위의 손잡이 부분이 친구를 향하도록 건네줘야 겠지?",
                                       neg_bhv="do_explain_A", neg="가위의 손잡이 부분이 친구를 향하도록 건네줘야 겠지?",
                                       act_bhv="do_explain_A", act="가위의 손잡이 부분이 친구를 향하도록 건네줘야 겠지?")
        
            cm.tts(bhv="do_question_S", string="칼은 어떻게 건네 주니?")
            answer = cm.responses_proc(re_bhv="do_question_L", re_q="어른들께 물건을 드릴 땐, 어떻게 드리는게 좋을까?",
                                       pos_bhv="do_explain_B", pos="사람이 다치지 않도록 칼 심을 넣어서 조심스럽게 전달해 줘야겠지?",
                                       neu_bhv="do_explain_B", neu="몰라도 괜찮아~ 사람이 다치지 않도록 칼 심을 넣어서 조심스럽게 전달해 줘야겠지?",
                                       neg_bhv="do_explain_B", neg="사람이 다치지 않도록 칼 심을 넣어서 조심스럽게 전달해 줘야겠지?",
                                       act_bhv="do_explain_B", act="사람이 다치지 않도록 칼 심을 넣어서 조심스럽게 전달해 줘야겠지?")
        
        # 2.3 문제 인식
        cm.tts(bhv="do_question_L", string="가위와 칼은 날카로운 물건이야. 날 쪽으로 건네주면 다른 사람이 다치게 될 수 있겠지?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="가위와 칼은 날카로운 물건이야. 날 쪽으로 건네주면 다른 사람이 다치게 될 수 있겠지?",
                                   pos_bhv="do_explain_C", pos="다른 사람들과 사용할 땐 조심스럽게 건네줘야 해!",
                                   neu_bhv="do_explain_C", neu="괜찮아. 모를 수도 있어~ 다른 사람들과 사용할 땐 조심스럽게 건네줘야 해!",
                                   act_bhv="do_explain_C", act="다른 사람들과 사용할 땐 조심스럽게 건네줘야 해!")
    
        # 3.1 마무리 대화
        cm.tts(bhv="do_joy_A", string=f"다른 사람들에게 가위나 칼을 전달해 줄 땐 친구가 손잡이를 잡을 수 있도록 잘 건네줘야 해~ 다칠 수 있으니 항상 조심하도록 하자!")
    
        
        
        
if __name__ == "__main__":
    
    etq = Etiquette()
    etq.Object2()