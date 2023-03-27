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
    tts.play(filename, 'local', '-1000', False)
    
    
        # 3. 피드백 수집
        time.sleep(1)                   
        cm.tts(bhv='do_question_S', string="활동 어땠어? 재밌었는지, 별로였는지 얘기해줄래?")
        answer = cm.responses_proc()  
              
        if answer[0][0] == "negative":
            self.score = [0.0, -0.5, 0.0, 0.0]
        
        if answer[0][0] == "positive":
            self.score = [0.0, 0.5, 0.0, 0.0]
            
        else: # if answer[0][0] == "neutral":
            self.score = [0.0, -0.25, 0.0, 0.0]
        
        cwp.writerow([today, filename, self.score[0], self.score[1], self.score[2],self.score[3]])
        
        # 4. Paradise framework 기록
        turns = [(self.reject[i] + 1) * 2 for i in range(len(self.reject))]      
        reject = sum(self.reject) 
        
        cwc.writerow(['Turns', turns])
        cwc.writerow(['Rejections', reject])
        cwc.writerow(['Misrecognitions', ])




if __name__ == "__main__":
    tts = TextToSpeech()          
    
    text_to_speech(voice="nhajun", text="내가 재미있는 이야기를 들려 줄게. 동화 제목은 개미와 베짱이야.")

    # 스토리: nara, 개미: ndain, 베짱이: nhajun
    text_to_speech(voice="nara", text="어느 활짝 갠 겨울날에 개미들은 여름에 모아놓은 곡식들을 말리고 있었어요.")
    text_to_speech(voice="nara", text="그때, 굶주림에 다 죽어가는 베짱이 한 마리가 지나가다")
    text_to_speech(voice="nhajun", text="먹을 걸 조금만 나눠주겠니?")
    text_to_speech(voice="nara", text="라며 빌었어요.")
    time.sleep(1)
    text_to_speech(voice="nara", text="개미들이 베짱이에게 물었어요.")
    text_to_speech(voice="ndain", text="그럼 넌 여름에 음식을 모아두지 않고 뭘 한거니?")
    time.sleep(1)
    text_to_speech(voice="nara", text="베짱이가 대답했어요.")
    text_to_speech(voice="nhajun", text="놀 시간도 부족하던 걸. 매일같이 노래하느라 다 보냈지.")
    time.sleep(1)
    text_to_speech(voice="nara", text="그러자 개미들이 혼내며 말했어요. ")
    text_to_speech(voice="ndain", text="여름 내내 노래나 하고 있을 정도로 어리석다면, 겨울엔 춤만 추면 되겠네")
    time.sleep(1)
    text_to_speech(voice="nara", text="배가 고픈 베짱이는 놀기만 한 자신의 잘못을 뉘우쳤답니다. ")
    time.sleep(1)
    text_to_speech(voice="nhajun", text="이야기 끝!")
     