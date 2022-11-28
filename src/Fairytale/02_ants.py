# -*- coding: utf-8 -*-

# 개미와 베짱이 시나리오 

import os
import sys
import random

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from NLP import NLP, Dictionary
from text_to_speech import TextToSpeech
# from speech_to_text import speech_to_text

nlp = NLP()
Dic = Dictionary()
tts = TextToSpeech()


def text_to_speech(text):
    filename = "tts.wav"
    print("\n" + text + "\n")
    tts.tts_connection(text, filename)
    tts.play(filename, 'local', '-800', False)
    
    
def fb(option):
    if option == "pos":     # 긍정 답변 옵션
        feedback_list = ["정말? ", "그래? ", "그렇구나. ", "그랬구나. "]
        feedback = random.choice(feedback_list)
        
    elif option == "neg":   # 부정 답변 옵션
        feedback_list = ["그래? ", "그렇구나. ", "그랬구나. "]
        feedback = random.choice(feedback_list)
        
    elif option == "neu":   # 중립 답변 옵션
        feedback_list = ["그래? ", "음~"]
        feedback = random.choice(feedback_list)
        
    elif option == "act":   # 행동 답변 옵션
        feedback_list = ["정말? ", "그래? ", "그렇구나. ", "그랬구나. "]
        feedback = random.choice(feedback_list)

    return feedback

class FairyTale():
    
    def story(self, name):        
        text_to_speech("\n이 동화는 개미와 베짱이가 나오는 동화였어")
        text_to_speech(f"{name}이는 어떤 장면이 기억에 남니?")
        user_said = input("입력: ")
        print("\n")

        text_to_speech(fb(option="act") +"개미는 어디에서 살까?")
        user_said = input("입력: ")
        print("\n")

        text_to_speech(fb(option="act") + "개미는 어떤 일을 했을까?")
        user_said = input("입력: ")
        print("\n")

        text_to_speech("열심히 일한 개미는 추운 겨울에 뭘 했을까?")
        user_said = input("입력: ")
        print("\n")

        text_to_speech(fb(option="act") + f"베짱이는 기타를 매고 무슨 노래를 불렀을까? {name}이는 어떤 노래를 부를 수 있어? 한번 불러볼래?")
        user_said = input("입력: ")
        print("\n")

        text_to_speech(fb(option="act") + f"베짱이는 어떤 포즈로 노래를 불렀을까? {name}이가 베짱이의 포즈를 한 번 흉내내볼래?")
        user_said = input("입력: ")
        print("\n")

        return FT.sympathy(name)
    
    
    def sympathy(self, name):
        text_to_speech("추운 겨울 먹을 것이 없던 베짱이의 기분은 어땠을까?")
        user_said = input("입력: ")
        print("\n")
        
        text_to_speech(fb(option="act") + "노래를 부르는 베짱이를 보면서 일하는 개미의 마음은 어땠을까?")
        user_said = input("입력: ")
        print("\n")
        
        text_to_speech(fb(option="act") + f"{name}이가 개미라면 겨울에 베짱이에게 먹을 것을 나누어줬을 것 같니?")
        user_said = input("입력: ")
        print("\n")
        
        text_to_speech(fb(option="act"))
        print("\n")
        
        return FT.end(name)
    
        
    def end(self, name):
        obj = random.choice(["베짱이", "개미"])
        
        text_to_speech(f"{obj}에게 해주고 싶은 말이 있니?")
        user_said = input("입력: ") 
        user_said = nlp.nlp_answer(user_said=user_said, dic=Dic)
        print("\n")      
        
        if user_said == "positive":
            text_to_speech(fb(option="pos") + "뭐라고 해주고 싶어?")
            user_said = input("입력: ")
            print("\n")
            
            text_to_speech(fb(option="act"))
            print("\n")
        
        elif user_said == "negative":
            text_to_speech(fb(option="neg"))
            print("\n")
        
        else:
            text_to_speech(fb(option="neu"))
            print("\n")
            
        text_to_speech("다음에 또 재미있는 동화 들려줄게~\n")
        

if __name__ == "__main__":
    FT = FairyTale()
    
    name = input("\nuser_name: ")
    FT.story(name=name)
