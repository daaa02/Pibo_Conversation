# -*- coding: utf-8 -*-

# 친구랑 친하게 지내고 싶어 시나리오

import random
import wave
import os
import sys

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
    
class Solution():
            
    def getalong(self, name):
        text_to_speech(f"친구들이랑 친하게 지내고 싶어. 어떻게 하면 좋을까?")
        user_said = input("입력: ")
        print("\n")
        
        text_to_speech(fb(option="act") + f"{name}의 가장 친한 친구는 누구니? 한 명만 말해봐.")
        user_said = input("입력: ") 
        print("\n")
        
        text_to_speech(fb(option="act") + "어떻게 친해지게 됐니?")
        user_said = input("입력: ")
        print("\n")
        
        text_to_speech(fb(option="act")+ f"그 친구랑 뭐하고 놀 때가 가장 재밌어?")
        user_said = input("입력: ")
        print("\n")
        
        text_to_speech(fb(option="act") + "그렇게 생각하는구나!")
        print("\n")
        
        text_to_speech("또 친해지고 싶은 친구가 있니?")
        user_said = input("입력: ")
        print("\n")
        
        text_to_speech(fb(option="act") + "새로운 친구와 어떻게 하면 친해질 수 있을까?")
        user_said = input("입력: ")
        print("\n")
        
        text_to_speech(fb(option="act") + "친구들과 어떻게 사이좋게 지낼 수 있을까?")
        user_said = input("입력: ")
        print("\n")
        
        text_to_speech(fb(option="act") + "파이보도 친구들이랑 사이좋게 잘 지내야겠다~ 알려줘서 정말 고마워!\n")
    
    
if __name__ == "__main__":
    sol = Solution()
    name = input("\nuser_name: ")
    sol.getalong(name)