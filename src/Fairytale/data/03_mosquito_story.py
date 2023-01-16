# -*- coding: utf-8 -*-

import io
import os
import requests
import json
import wave
import time
import urllib.request


def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


class TextToSpeech:

    def tts_connection(self, voice, text, filename):
        # CLOVA auth-key
        client_id = "3qz5jqx2r0"
        client_secret = "zwB0Yb4UONPKaOKCjZkhsSl8REuKvJTYK2Esvr41"
        encText = urllib.parse.quote(text)
        data = f"speaker={voice}&volume=0&speed=1&pitch=0&format=wav&text=" + encText
        url = "https://naveropenapi.apigw.ntruss.com/tts-premium/v1/tts"
        request = urllib.request.Request(url)
        request.add_header("X-NCP-APIGW-API-KEY-ID",client_id)
        request.add_header("X-NCP-APIGW-API-KEY",client_secret)
        response = urllib.request.urlopen(request, data=data.encode('utf-8'))
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            with open(filename, 'wb') as f:
                f.write(response_body)
        else:
            print("Error Code:" + rescode)            
            

    # tts, 효과음 등 모든 오디오를 플레이하는 함수
    def play(self, filename, out='local', volume='-1000', background=True):
        if not os.path.isfile(filename):
            raise Exception(f'"{filename}" does not exist')

        if not filename.split('.')[-1] in ['mp3', 'wav']:
            raise Exception(f'"{filename}" must be (mp3|wav)')

        if not out in ['local', 'hdmi', 'both']:
            raise Exception(f'"{out}" must be (local|hdmi|both)')

        if not isNumber(volume):
            raise Exception(f'"{volume}" is not Number')

        if type(background) != bool:
            raise Exception(f'"{background}" is not bool')

        opt = '&' if background else ''
        os.system(f'omxplayer -o {out} --vol {volume} {filename} {opt}')
        
    
def text_to_speech(voice, text):
    tts = TextToSpeech()  
    
    filename = "tts.wav"
    print("\n" + text + "\n")
    tts.tts_connection(voice, text, filename)
    tts.play(filename, 'local', '-800', False)
    
    
if __name__ == "__main__":
    tts = TextToSpeech()          
    
    text_to_speech(voice="nhajun", text="내가 재미있는 이야기를 들려 줄게. 동화 제목은 모기와 사자야.")

    # 스토리: nara, 모기: ndain    
    text_to_speech(voice="nara", text="어느 날, 모기 한마리가 사자보고 대뜸 이렇게 말했어요.")
    time.sleep(1)
    text_to_speech(voice="ndain", text="난 네가 두렵지 않아. 힘도 겁나지 않는다고. 사자는 싸울 때 발톱으로 할퀴고 이빨로 물기나 하겠지. ")
    text_to_speech(voice="ndain", text="난 사자 너보다 더 강하다고. 못 믿겠으면, 어디 나랑 한 번 대결해볼까?")
    time.sleep(1)
    text_to_speech(voice="nara", text="모기는 자신의 뿔피리를 불고선, 힘차게 사자에게로 돌진하더니 사자의 콧구멍과 얼굴을 마구 물었어요.")
    text_to_speech(voice="nara", text="사자는 모기를 때릴 작정으로 자신의 얼굴을 때렸다가 심각한 상처만 입고 말았어요.")
    text_to_speech(voice="nara", text="이로써 모기가 사자를 이겼어요.")
    time.sleep(1)
    text_to_speech(voice="ndain", text="윙윙!!")
    text_to_speech(voice="nara", text="모기는 승리의 노래를 부르며 날아갔답니다.")
    time.sleep(1)
    text_to_speech(voice="nara", text="그런데 모기는 그만 거미집에 걸려 바로 거미에게 잡아먹히고 말았어요.")
    text_to_speech(voice="nara", text="모기가 자신의 죽음을 크게 슬퍼하며 말했어요.")
    time.sleep(1)
    text_to_speech(voice="ndain", text="아! 용맹한 사자도 때려눕힌 내가 기껏 거미같은 곤충한테 당하다니! 정말 슬프구나")
    text_to_speech(voice="nara", text="모기는 발버둥을 치며 살려달라고 했지만 아무 소용이 없었답니다.")
    time.sleep(1)
    text_to_speech(voice="nhajun", text="이야기 끝!")
    
    
    
    
    
    
