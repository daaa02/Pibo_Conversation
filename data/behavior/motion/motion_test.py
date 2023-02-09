# motion test

# python module
import os
import sys
import time

# openpibo module
import openpibo
from openpibo.oled import Oled
from openpibo.motion import Motion

# my module
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

oled = Oled()
motion = Motion()

def motion_test():
    """
    <현재 사용 방법>
    /usr/local/lib/python3.7/.../openpibo/motion.py 에서
    사용할 모션 파일 경로를 /home/pi/AI_pibo2/data/motion_db.json 로 지정하고
    set_motion(name="", cycle=n) 함수 사용해서 모션 실행

    <다른 방법>
    (example.json 이라는 새로운 모션 파일을 만든다는 가정 하에)
    motion.set_motion("<name>", path="/path/to/example.json") 으로
    라이브러리에 설정된 경로 말고 내 임의의 경로에서 모션 파일 실행 및 동작 가능할 듯
    """

    def display(text):
        disp.set_font(size=20)
        disp.draw_text((10, 10), text)
        disp.show()
        time.sleep(2)
        disp.clear()

    display("질문하기_L")
    oled.o_question()
    eye.e_question()
    while True: 
        audio.play(filename="/home/pi/Pibo_Conversation/data/audio/물음표소리1.wav", out='local', volume=-1500, background=True)
        motion.set_motion(name="m_question_L", cycle=1)
        break
    disp.clear()

    time.sleep(2)

    display("질문하기_S")
    oled.o_question()
    eye.e_question()
    while True:
        audio.play(filename="/home/pi/Pibo_Conversation/data/audio/물음표소리1.wav", out='local', volume=-1500, background=True)
        motion.set_motion(name="m_question_S", cycle=1)
        break
    disp.clear()

    time.sleep(2)

    display("제안하기_L")
    oled.o_suggestion()
    eye.e_suggestion()
    while True:
        motion.set_motion(name="m_suggestion_L", cycle=1)
        break
    disp.clear()

    time.sleep(2)

    display("제안하기_S")
    oled.o_suggestion()
    eye.e_suggestion()
    while True:
        motion.set_motion(name="m_suggestion_S", cycle=1)
        break
    disp.clear()

    time.sleep(2)

    display("설명하기_A")
    oled.o_explain()
    eye.e_explain()
    while True:
        motion.set_motion(name="m_explain_A", cycle=1)
        break
    disp.clear()

    time.sleep(2)

    display("설명하기_B")
    oled.o_explain()
    eye.e_explain()
    while True:
        motion.set_motion(name="m_explain_B", cycle=1)
        break
    disp.clear()

    time.sleep(2)

    display("사진찍기")
    oled.o_photo()
    eye.e_photo()
    while True:
        motion.set_motion(name="m_photo-1", cycle=1)
        break
    audio.play(filename="/home/pi/Pibo_Conversation/data/audio/사진기소리.mp3", out='local', volume=-1500, background=True)
    while True:
        motion.set_motion(name="m_photo-2", cycle=1)
        break
    disp.clear()

    time.sleep(2)

    display("스탬프찍기")
    oled.o_stamp()
    eye.e_stamp()
    while True:
        motion.set_motion(name="m_stamp-1", cycle=1)        
        break
    audio.play(filename="/home/pi/Pibo_Conversation/data/audio/스탬프소리2.wav", out='local', volume=-1500, background=True)
    while True:
        motion.set_motion(name="m_stamp-2", cycle=1)        
        break
    disp.clear()

    time.sleep(2)
    display("기다리기_A")
    oled.o_waiting()
    eye.e_waiting()
    while True:
        motion.set_motion(name="m_waiting_A", cycle=1)
        break
    disp.clear()

    time.sleep(2)

    display("기다리기_B")
    oled.o_waiting()
    eye.e_waiting()
    while True:
        motion.set_motion(name="m_waiting_B", cycle=1)
        break
    disp.clear()

    time.sleep(2)

    display("기다리기_C")
    oled.o_waiting()
    eye.e_waiting()
    while True:
        motion.set_motion(name="m_waiting_C", cycle=1)
        break
    disp.clear()

    time.sleep(2)

    display("기상하기")
    oled.o_compliment()
    eye.e_compliment()
    while True:
        audio.play(filename="/home/pi/Pibo_Conversation/data/audio/경쾌한음악.wav", out='local', volume=-1500, background=True)
        motion.set_motion(name="m_wakeup", cycle=1)
        break
    disp.clear()

    time.sleep(2)

    display("칭찬하기_L")
    oled.o_compliment()
    eye.e_compliment()
    while True:
        audio.play(filename="/home/pi/Pibo_Conversation/data/audio/경쾌한음악.wav", out='local', volume=-1500, background=True)
        motion.set_motion(name="m_compliment_L", cycle=1)
        break
    disp.clear()

    time.sleep(2)

    display("칭찬하기_S")
    oled.o_compliment()
    eye.e_compliment()
    while True:
        audio.play(filename="/home/pi/Pibo_Conversation/data/audio/경쾌한음악.wav", out='local', volume=-1500, background=True)
        motion.set_motion(name="m_compliment_S", cycle=1)
        break
    disp.clear()

    time.sleep(2)

    display("동의하기")
    oled.o_agree
    eye.e_agree()
    while True:
        audio.play(filename="/home/pi/Pibo_Conversation/data/audio/딩동댕3.wav", out='local', volume=-1500, background=True)
        motion.set_motion(name="m_agree", cycle=1)
        break
    disp.clear()

    time.sleep(2)

    display("기쁨-A")
    oled.o_joy()
    eye.e_joy()
    while True:
        audio.play(filename="/home/pi/Pibo_Conversation/data/audio/기분좋음.wav", out='local', volume=-1500, background=True)
        motion.set_motion(name="m_joy_A", cycle=1)
        break
    disp.clear()

    time.sleep(2)
    
    display("기쁨-B")
    oled.o_joy()
    eye.e_joy()
    while True:
        audio.play(filename="/home/pi/Pibo_Conversation/data/audio/기분좋음.wav", out='local', volume=-1500, background=True)
        motion.set_motion(name="m_joy_B", cycle=1)
        break
    disp.clear()

    time.sleep(2)

    display("슬픔")
    oled.o_sad()
    eye.e_sad()
    while True:
        audio.play(filename="/home/pi/Pibo_Conversation/data/audio/슬픈소리.wav", out='local', volume=-1500, background=True)
        motion.set_motion(name="m_sad", cycle=1)
        break
    disp.clear()

    time.sleep(2)

    disp.set_font(size=20)
    disp.draw_text((10, 10), "끝.")
    disp.show()
    time.sleep(2)
    disp.clear()


if __name__ == "__main__":
    motion_test()
