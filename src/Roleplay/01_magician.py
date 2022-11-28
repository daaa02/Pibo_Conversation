# -*- coding: utf-8 -*-

# 마법을 부리는 존재 시나리오

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


class RolePlaying():
    
    def roleplay_1(self, name):
        tts.play("Pibo_Conversation/Roleplay/Sound/01_magic.wav")
        text_to_speech(f"\n이제 우리는 하늘에 사는 마법사야~")
        text_to_speech(f"파이보가 먼저 주문을 걸어볼게. 천둥아 쳐라 얍!")
        tts.play("Pibo_Conversation/Roleplay/Sound/01_magic.wav")
        tts.play("Pibo_Conversation/Roleplay/Sound/04_thunder.wav")
        print("\n")
        
        text_to_speech(f"{name}도 날씨 주문을 걸어봐!")
        text_to_speech(f"먼저 비, 바람, 천둥 등 날씨를 말하고 얍! 을 외치면 돼~")
        weather = ["비", "바람", "천둥", "눈", "해", "맑"]
        
        user_said = input("입력: ")
        print("\n")
        for i in range(len(weather)):
            if weather[i] in user_said:    
                if "비" in user_said:   # "비바람" 도 여기 들어감
                    tts.play("Pibo_Conversation/Roleplay/Sound/01_magic.wav")
                    tts.play("Pibo_Conversation/Roleplay/Sound/02_rain.wav")
                    
                elif "바람" in user_said:
                    tts.play("Pibo_Conversation/Roleplay/Sound/01_magic.wav")
                    tts.play("Pibo_Conversation/Roleplay/Sound/05_wind.wav")
                    
                elif "천둥" in user_said:
                    tts.play("Pibo_Conversation/Roleplay/Sound/01_magic.wav")
                    tts.play("Pibo_Conversation/Roleplay/Sound/04_thunder.wav")
                
                elif "눈" in user_said:
                    tts.play("Pibo_Conversation/Roleplay/Sound/01_magic.wav")
                    tts.play("Pibo_Conversation/Roleplay/Sound/06_snow.wav")                
                
                elif "해" or "맑" in user_said:
                    tts.play("Pibo_Conversation/Roleplay/Sound/01_magic.wav")
                    tts.play("Pibo_Conversation/Roleplay/Sound/03_clear.wav")                
                    
                text_to_speech("우와~ 주문을 잘 거는 걸?")
                print("\n")
            
        else:
            pass
        
        text_to_speech("이번에는 소풍가는 날에 원하는 날씨 주문을 걸어봐~")
        user_said = input("입력: ")
        print("\n")
        
        for i in range(len(weather)):
            if weather[i] in user_said:    
                if "비" in user_said:   # "비바람" 도 여기 들어감
                    tts.play("Pibo_Conversation/Roleplay/Sound/01_magic.wav")
                    tts.play("Pibo_Conversation/Roleplay/Sound/02_rain.wav")
                    
                elif "바람" in user_said:
                    tts.play("Pibo_Conversation/Roleplay/Sound/01_magic.wav")
                    tts.play("Pibo_Conversation/Roleplay/Sound/05_wind.wav")
                    
                elif "천둥" in user_said:
                    tts.play("Pibo_Conversation/Roleplay/Sound/01_magic.wav")
                    tts.play("Pibo_Conversation/Roleplay/Sound/04_thunder.wav")
                
                elif "눈" in user_said:
                    tts.play("Pibo_Conversation/Roleplay/Sound/01_magic.wav")
                    tts.play("Pibo_Conversation/Roleplay/Sound/06_snow.wav")                
                
                elif "해" or "맑" in user_said:
                    tts.play("Pibo_Conversation/Roleplay/Sound/01_magic.wav")
                    tts.play("Pibo_Conversation/Roleplay/Sound/03_clear.wav") 
                    
                text_to_speech("빨리 소풍 가고 싶다!")
                print("\n")
            
        else:
            pass
        
        role = "마법사"
        return conversation(name, role)


    def roleplay_2(self, name):
        tts.play("Pibo_Conversation/Roleplay/Sound/01_magic.wav")
        text_to_speech("\n이제 우리는 숲속의 도깨비야!")
        text_to_speech("파이보가 먼저 주문을 걸어 볼게. 뻐꾸기야 나타나라 얍!")
        tts.play("Pibo_Conversation/Roleplay/Sound/01_magic.wav")
        tts.play("Pibo_Conversation/Roleplay/Sound/07_owl.wav")
        print("\n")
        
        text_to_speech(f"{name}이도 마법 주문을 걸어서 동물을 불러봐! 동물 이름을 말하고 얍! 을 외치면 돼~")
        text_to_speech("먼저 늑대를 불러보자!")
        animal = ["늑대", "코끼리"]
        
        user_said = input("입력: ")
        print("\n")
        
        if "늑대" in user_said:
            tts.play("Pibo_Conversation/Roleplay/Sound/01_magic.wav")
            tts.play("Pibo_Conversation/Roleplay/Sound/08_wolf.wav")
            print("늑대가 나타났다~")
        else:
            pass
        
        text_to_speech("이번에는 코끼리를 불러보자!")
        user_said = input("입력: ")
        
        if "코끼리" in user_said:
            tts.play("Pibo_Conversation/Roleplay/Sound/01_magic.wav")
            tts.play("Pibo_Conversation/Roleplay/Sound/09_elephant.wav")
            print("우와~ 주문을 잘 거는 걸?")            
        else:
            pass      
        
        role = "도깨비"
        return conversation(name, role)
        
    
    def roleplay_3(self, name):
        tts.play("Pibo_Conversation/Roleplay/Sound/10_water.wav")
        text_to_speech("\n이제 우리는 물에 사는 요정이야~")
        text_to_speech("파이보가 먼저 주문을 걸어 볼게. 바다 갈매기야 나타나라 얍!")
        tts.play("Pibo_Conversation/Roleplay/Sound/01_magic.wav")
        tts.play("Pibo_Conversation/Roleplay/Sound/11_seagull.wav")
        print("\n")
        
        text_to_speech(f"{name}이도 마법 주문을 걸어서 동물을 불러봐! 동물 이름을 말하고 얍! 을 외치면 돼.")
        text_to_speech("물가에 사는 오리를 불러보자~")
        animal = ["오리", "개구리"]
        
        user_said = input("입력: ")
        print("\n")
        

        if "오리" in user_said:
            tts.play("Pibo_Conversation/Roleplay/Sound/01_magic.wav")
            tts.play("Pibo_Conversation/Roleplay/Sound/12_duck.wav")
            text_to_speech("귀여운 오리가 나타났다~")
        else:
            pass
        
        text_to_speech("이번에는 개구리를 불러보자!")
        user_said = input("입력: ")
        print("\n")
        
        if "개구리" in user_said:
            tts.play("Pibo_Conversation/Roleplay/Sound/01_magic.wav")
            tts.play("Pibo_Conversation/Roleplay/Sound/13_frog.wav")
            text_to_speech("우와~ 주문을 잘 거는 걸?")           
        else:
            pass             
        
        role = "요정"
        return conversation(name, role)
  
    
class RoleConversation():
    
    def conversation_1(self, name, role):
        if role == "요정":
            role_p = role + "이"
        else:
            role_p = role + "가"
            
        text_to_speech(f"\n{name}이는 {role_p} 되면 무슨 일을 하고 싶니? 이루고 싶은 소원이 있니?")
        user_said = input("입력: ")
        user_said = nlp.nlp_answer(user_said=user_said, dic=Dic)
        print("\n")
        
        if user_said == "positive":
            text_to_speech(fb(option="pos") + "어떤 소원인지 말해줄래?")
            user_said = input("입력: ")
            print("\n")
            
            text_to_speech(fb(option="act") + "소원이 이루어지면 정말 좋겠다~")
            print("\n")
        
        elif user_said == "negative":
            text_to_speech(fb(option="neg"))
            print("\n")
        
        else:
            text_to_speech(fb(option="neu"))
            print("\n")
        
        # return end(name)
        return RC.conversation_2(name, role)
        
        
    def conversation_2(self, name, role):
        if role == "요정":
            role_p = role + "이"
        else:
            role_p = role + "가"
            
        text_to_speech(f"\n{name}이는 {role_p} 되면 변신해보고 싶은 모습이 있니?")
        user_said = input("입력: ")
        user_said = nlp.nlp_answer(user_said=user_said, dic=Dic)
        print("\n")
        
        if user_said == "positive":
            text_to_speech(fb(option="pos") + "왜 변신하고 싶니?")
            user_said = input("입력: ")
            print("\n")
            
            text_to_speech(fb(option="act") + "변신하면 멋지겠는걸?")
            print("\n")
        
        elif user_said == "negative":
            text_to_speech(fb(option="neg"))
            print("\n")
        
        else:
            text_to_speech(fb(option="neu"))
            print("\n")
        
        # return end(name)
        return RC.conversation_3(name, role)
        
        
    def conversation_3(self, name, role):
        if role == "요정":
            role_p = role + "은"
        else:
            role_p = role + "는"
            
        text_to_speech(f"\n{role_p} 시간 마법을 써서 가장 기뻤던 시간으로 갈 수 있어. {name}이는 다시 돌아가고 싶은 시간이 있니?")
        user_said = input("입력: ")
        user_said = nlp.nlp_answer(user_said=user_said, dic=Dic)
        print("\n")
        
        if user_said == "positive":
            text_to_speech(fb(option="pos") + "왜 그 시간으로 가고 싶니?")
            user_said = input("입력: ")
            print("\n")
            
            text_to_speech(fb(option="act") + "파이보도 같이 가고 싶은 걸?")
            print("\n")
        
        elif user_said == "negative":
            text_to_speech(fb(option="neg"))
            print("\n")
        
        else:
            text_to_speech(fb(option="neu"))
            print("\n")
        
        return end(name)
    
        
    def conversation_4(self, name, role):
        if role == "요정":
            role_p = role + "이"
        else:
            role_p = role + "가"
            
        text_to_speech(f"\n{role_p} 되면 어렵고 힘든 사람들을 도와줄 수 있는 능력이 있어. {name}이는 {role_p} 되면 누구를 도와주고 싶니?")
        user_said = input("입력: ")
        user_said = nlp.nlp_answer(user_said=user_said, dic=Dic)
        print("\n")
        
        if user_said is True:
            text_to_speech(fb(option="pos") +"어떤 도움을 주고 싶니?")
            user_said = input("입력: ")            
            print("\n")
            
            text_to_speech(fb(option="act") + "도움을 주면 정말 좋겠다!")
            print("\n")
        
        return end(name)
    
        
    def conversation_5(self, name, role):
        if role == "요정":
            role_p = role + "은"
        else:
            role_p = role + "는"
            
        text_to_speech(f"\n{role_p} 사람들의 기분을 즐겁게 만들어 줄 수 있어. {name} 주변에 즐겁게 만들어 주고 싶은 사람이 있니?")
        user_said = input("입력: ")
        user_said = nlp.nlp_answer(user_said=user_said, dic=Dic)
        print("\n")
        
        if user_said == "positive":
            text_to_speech(fb(option="pos") + "누구를 즐겁게 만들어 주고 싶니?")            
            user_said = input("입력: ")
            print("\n")
            
            text_to_speech(fb(option="act") + "즐겁게 만들어 주면 정말 좋겠다!")
            print("\n")
        
        elif user_said == "negative":
            text_to_speech(fb(option="neg"))
            print("\n")
        
        else:
            text_to_speech(fb(option="neu"))
            print("\n")
        
        return end(name)
    
        
    def conversation_6(self, name, role):
        if role == "요정":
            role_p = role + "이"
        else:
            role_p = role + "는"
            
        text_to_speech(f"\n{role_p} 원하는 곳 어느 장소든 갈 수 있어. 가보고 싶은 곳이 있니?")
        user_said = input("입력: ")
        user_said = nlp.nlp_answer(user_said=user_said, dic=Dic)
        print("\n")
        
        if user_said == "positive":
            text_to_speech(fb(option="pos") + "어디에 가고 싶니?")
            user_said = input("입력: ")
            print("\n")
            
            text_to_speech(fb(option="act") + "파이보도 같이 가고 싶은 걸?")
            print("\n")
        
        elif user_said == "negative":
            text_to_speech(fb(option="neg"))
            print("\n")
        
        else:
            text_to_speech(fb(option="neu"))
            print("\n")
        
        return end(name)
    
        
def roleplay(name):
    RP = RolePlaying()
    play = random.choice(["rp_1", "rp_2", "rp_3"])
    
    if play == "rp_1":    RP.roleplay_1(name)
    elif play == "rp_2":  RP.roleplay_2(name)
    elif play == "rp_3":  RP.roleplay_3(name)
    
    
def conversation(name, role):
    RC = RoleConversation()
    play = "rc_1"
    # play = random.choice(["rc_1", "rc_2", "rc_3", "rc_4", "rc_5", "rc_6"])
    
    if play == "rc_1":    RC.conversation_1(name, role)
    elif play == "rc_2":  RC.conversation_2(name, role)
    elif play == "rc_3":  RC.conversation_3(name, role)
    elif play == "rc_4":  RC.conversation_4(name, role)
    elif play == "rc_5":  RC.conversation_5(name, role)
    elif play == "rc_6":  RC.conversation_6(name, role)

def end(name):
    text_to_speech(f"{name}이가 원하는 행복한 일들이 모두 이루어졌으면 좋겠다.")
    text_to_speech("다음에 또 재미있는 역할놀이 하자~\n")    

    
if __name__ == "__main__":
    RP = RolePlaying()
    RC = RoleConversation()
    
    name = input("\nuser_name: ")
    text_to_speech("\n역할 놀이를 해볼까?\n")
    # roleplay(name=name)
    RP.roleplay_1(name=name)
    # RC.conversation_1(name=name, role=role)
    # RC.conversation_2(name=name, role=role)
    # RC.conversation_3(name=name, role=role)
    
    
    