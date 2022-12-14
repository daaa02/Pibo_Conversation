import os, sys
import re
import time
import random
import socket
from threading import Thread

sys.path.append('/home/kiro/workspace/Conversation_Scenarios/data')

import google
from speech_to_text import speech_to_text
from text_to_speech import text_to_speech

# import openpibo
# import behavior.behavior_list as behavior

"""
STT 모듈이랑 답변 처리 모듈 통합하고 있는 파일
    * class Dictionary: 답변 성격(Pos/Neu/Neg), 숫자 후보들
    * class ConversationManage: STT 모듈 -> 답변 처리 및 다음 발화+행동
    * class Socket_tr: socket 통신 모듈
"""

# transmit
# 클라이언트가 보내고자 하는 서버의 IP와 PORT
server_ip = "192.168.13.215"
server_port = 3000
server_addr_port = (server_ip, server_port)
buffersize = 2048

# receive
# 서버가 보내고자 하는 클라이언트의 IP와 PORT
client1_ip = "192.168.14.20"
client1_port = 5000
client1_addr_port = (client1_ip, client1_port)
buffersize = 2048

# UDP로 열고 서버의 IP/PORT 연결
# udp_client1_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# udp_client1_socket.bind(client1_addr_port)
# udp_client1_socket.setblocking(False)   


class Dictionary():
    
    def __init__(self):
        self.Positive = ['pos', '네', '예', '응', '있어', '좋아', '좋은', '좋다', '그래', '맞아', '알았어', '알겠어', '당연', '됐어']

        self.Negative = ['neg', '별로', '아니', '안 해', '안해', '안 할래', '안 하', '싫어', '싫', '못 하', '못 하겠어', '못해', '없었어', '없어', '없네', '없는','그만']
        
        self.Neutral = ['neu', '글쎄', '몰라', '모르', '몰라', '몰랐']    
        
        self.Again = ['again', '다시', '또', '같은', '한 번 더', '한번 더', '계속'] 
        
        self.Number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

        self.Number_word = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구', '십']



class ConversationManage():

    def __init__(self):
        self.timeout = 10
        self.none = "None"
        self.count = 0
        self.user_said = ''
        self.response = ''
        self.answer = []
        self.feedback = ''   
        self.from_msg = ''     
        self.ko = -1
        self.nb = -1
        
    
    def stt(self):
        """         
        * 정상적인 응답이 들어왔을 경우: response = speech_to_text()
        * 무응답으로 timeout 발생한 경우: response = "None"
        """
        try:
            # self.response = speech_to_text(timeout=self.timeout)
            self.response = input("input: ")
        
        except google.api_core.exceptions.DeadlineExceeded:
            self.response = self.none
        
        # 가끔 발생하는 Google API ERROR --> ignore
        except google.api_core.exceptions.Unknown as e:
            print(e)
        
        except google.api_core.exceptions.InvalidArgument as e:
            print(e)
        
        # print(self.response)
        return self.response
    
    
    def tts(self, bhv='do_breath1', string=''):
        """
        * behavior: TTS 와 함께할 동작 ex. 'do_joy'
        * string: 발화할 TTS 내용
        """
        t = Thread(target=text_to_speech, args=([string]))
        t.start()
        
        while True:
            time.sleep(1)
            # bhv()
            break    
        
        
    def responses_proc(self, 
                       re_bhv='', re_q='', 
                       pos_bhv='', pos='', 
                       neu_bhv='', neu='', 
                       neg_bhv='', neg='', 
                       act_bhv='', act=''):
        """
        * re_q: 무응답인 경우, 재질문할 내용(최대 3번)
        * pos/neu/neg: 긍정/중립/부정 답변 인식 시, 발화할 내용
        * 사용자가 발화한 내용 중 Dictionary에 포함되는 단어 있으면 return answer
            => Positive/Neutral/Negative
        """                
        self.answer = []    # 마지막 answer가 'action'일 경우 초기화 안 되는 것 같아서  
        
        while True:
            self.response = cm.stt()
            
            if self.response != "None":
                self.user_said = self.response
                break
            
            else:   # 무응답인 경우, 두 번 더 물어봐주고 3번째에도 무응답이면 탈출
                self.count += 1
                cm.tts(bhv=re_bhv, string=re_q)
                   
                if self.count < 3:
                    continue 
                
                elif self.count == 3:
                    print("다음에 이야기하자~")
                    break        
        
        """
        사용자가 발화한 내용에 포함되는 단어가 있다면 return answer '_'
        ex. input: 좋은 것 같아 ==> Yes=[..'좋은'..] ==> answer: Positive
        """
        
        for i in range(len(dic.Positive)):
            if dic.Positive[i] in self.user_said:     
                self.answer = ["positive", self.user_said]

        for j in range(len(dic.Negative)):
            if dic.Negative[j] in self.user_said:
                self.answer = ["negative", self.user_said]
                
        for k in range(len(dic.Neutral)):
            if dic.Neutral[k] in self.user_said:
                self.answer = ["neutral", self.user_said]
        
        if len(self.answer) == 0:
            self.answer = ["action", self.user_said]    # pos -> neg -> neu 에도 없으면 act
        
        print("=>", self.answer)
        """
        self.answer 결과에 맞는 feedback 답변을 TTS로 출력
        """             
        if self.answer[0] == "positive":     # 긍정 답변 옵션
            feedback_list = ["정말? ", "그래? ", "오호~ "]
            self.feedback = random.choice(feedback_list)
            cm.tts(bhv=pos_bhv, string=self.feedback + pos)
            # text_to_speech(self.feedback + pos)
            
        elif self.answer[0] == "negative":   # 부정 답변 옵션
            feedback_list = ["그래? ", "음~ "]
            self.feedback = random.choice(feedback_list)
            cm.tts(bhv=neg_bhv, string=self.feedback + neg)
            # text_to_speech(self.feedback + neg)
            
        elif self.answer[0] == "neutral":   # 중립 답변 옵션
            feedback_list = ["그래? "]
            self.feedback = random.choice(feedback_list)
            cm.tts(bhv=neu_bhv, string=self.feedback + neu)
            # text_to_speech(self.feedback + neu)
            
        elif self.answer[0] == "action":
            feedback_list = ["그래? ", "정말? "]
            self.feedback = random.choice(feedback_list)
            cm.tts(bhv=act_bhv, string=self.feedback + act)
            # text_to_speech(self.feedback + act)
            
        #     # connect with chit-chat model
        #     self.from_msg = soc.transmit(send_msg=self.response)             
                
        return self.answer


class Socket_tr():
    
    def transmit(self, send_msg):
        # Message from Client
        msg_from_client1 = send_msg
        msg_from_client1 = msg_from_client1.encode("utf-8")
        
        # UDP 열고 서버의 IP/PORT로 메시지를 보낸다.
        udp_client1_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        udp_client1_socket.sendto(msg_from_client1, server_addr_port)
        
        soc.receive()
    
    def receive(self):
        # Message from Server -> tts
        while True:
            try:
                byte_addr_pair = udp_client1_socket.recvfrom(buffersize)
            except BlockingIOError:
                continue
          
            msg_from_server  = byte_addr_pair[0].decode("utf-8")
            break
        
        text_to_speech(msg_from_server)
        
        return msg_from_server
    
    
class WordManage():
        
    def postposition(self, word):
        """
        'word' 가 종성으로 끝나는지 판별 (=받침이 있는지 없는지)
        """
        m = re.search("[가-힣]+", word)
        if m:
            k = m.group()[-1]
            return (ord(k) - ord("가")) % 28 > 0
        else:
            return
        
    
    def word(self, word, type):
        """
        type0: '다영'이 / '파이보'
        type1: '다영'이 / '파이보'가
        type2: '다영'은 / '파이보'는
        type3: '다영'을 / '파이보'를
        type4: '다영'아 / '파이보'야
        type4: '다영'과 / '파이보'와
        * 주의: 띄워쓰기 없어야 함 (ex. '작은 개구리' => '작은'의 영향 받는 듯;;)
        """
        if type == 0:
            name = f"{word}이" if wm.postposition(word) else f"{word}"
        if type == 1:
            name = f"{word}이" if wm.postposition(word) else f"{word}가"                    
        if type == 2:
            name = f"{word}은" if wm.postposition(word) else f"{word}는"              
        if type == 3:
            name = f"{word}을" if wm.postposition(word) else f"{word}를"
        if type == 4:
            name = f"{word}아" if wm.postposition(word) else f"{word}야"
        if type == 5:
            name = f"{word}과" if wm.postposition(word) else f"{word}와"

        return name
    
    
dic = Dictionary()
cm = ConversationManage()
soc = Socket_tr()
wm = WordManage()
