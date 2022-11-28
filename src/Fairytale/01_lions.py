# -*- coding: utf-8 -*-

# 모기와 사자 시나리오

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
        text_to_speech("\n정말 재미있는 이야기였어!")
        text_to_speech(f"{name}이는 어떤 장면이 재미있었니?")
        user_said = input("입력: ")
        print("\n")

        text_to_speech(fb(option="act") +f"{name}이는 모기에 물린 적이 있니?")
        user_said = input("입력: ")
        print("\n")

        text_to_speech(fb(option="act") + "모기에 물리면 어떻게 해?")
        user_said = input("입력: ")
        print("\n")

        text_to_speech(fb(option="act") + f"{name}이가 모기라면 누굴 물고 싶니?")
        user_said = input("입력: ")
        print("\n")
        
        text_to_speech(fb(option="act") +"모기한테 마구 물린 사자 얼굴은 어떻게 생겼을까?")
        user_said = input("입력: ")
        print("\n")
        
        text_to_speech(fb(option="act") +"모기랑 사자는 친구가 될 수 없을까?")
        user_said = input("입력: ")
        print("\n")
        
        text_to_speech(fb(option="act") +"만약에 사자가 거미줄에 걸린 모기를 본다면 구해줄까?")
        user_said = input("입력: ")
        print("\n")
        
        text_to_speech(fb(option="act") + "사자는 그럴 수 있겠구나.")  
        print("\n")   

        return FT.sympathy(name)
    
    
    def sympathy(self, name):
        text_to_speech("거미줄에 걸린 모기는 움직일 수 없었을 때 기분이 어땠을까? 무서웠을까?")
        user_said = input("입력: ")
        print("\n")
        
        text_to_speech(fb(option="act") + f"{name}이는 최근에 무섭다고 느낀 일이 있니?")
        user_said = input("입력: ")  
        user_said = nlp.nlp_answer(user_said=user_said, dic=Dic)      
        print("\n")
        
        if user_said == "positive":
            text_to_speech(fb(option="pos") + "어떤 일이 있었니?")
            user_said = input("입력: ")
            print("\n")
            
            text_to_speech(fb(option="act") + "정말 무서웠겠다!")
            print("\n")
        
        elif user_said == "negative":
            text_to_speech(fb(option="neg"))
            print("\n")
        
        else:
            text_to_speech(fb(option="neu"))
            print("\n")
        
        text_to_speech("모기가 큰 사자랑 싸워서 이겼을 때는 기분이 어땠을까? 기뻤을까?")
        user_said = input("입력: ")
        print("\n")
        
        text_to_speech(fb(option="act") + f"{name}이는 최근에 놀이에서 이겨서 기뻤던 적이 있니? 이야기해줄래?")
        user_said = input("입력: ")
        user_said = nlp.nlp_answer(user_said=user_said, dic=Dic)
        print("\n")
        
        if user_said == "positive":
            text_to_speech(fb(option="pos") + "정말 기분이 좋았겠다!")
            print("\n")
        
        elif user_said == "negative":
            text_to_speech(fb(option="neg"))
            print("\n")
        
        else:
            text_to_speech(fb(option="neu"))
            print("\n")
            
        return FT.end(name)
    
        
    def end(self, name):        
        text_to_speech(f"동화 속 모기를 만난다면 무슨 말을 해주고 싶니?")
        user_said = input("입력: ")    
        print("\n")   
        
        print(fb(option="act"))
            
        text_to_speech("오늘 동화 재미있었니? 다음에 또 재미있는 동화 들려줄게~\n")
        

if __name__ == "__main__":
    FT = FairyTale()
    
    name = input("\nuser_name: ")
    FT.story(name=name)
