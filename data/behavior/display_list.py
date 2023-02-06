#!/usr/bin/python3

import time

# openpibo module
import openpibo
from openpibo.oled import Oled

o = Oled()

# draw_image 하고 바로 show 해야 안 사라짐

def run():
    o.draw_image("/home/pi/Pibo_conversation/data/behavior/icon/아이콘_물음표1.png")
    o.show()


def o_question():
    o.draw_image("/home/pi/Pibo_conversation/data/behavior/icon/아이콘_물음표1.png")
    o.show()


def o_suggestion():
    o.draw_image("/home/pi/Pibo_conversation/data/behavior/icon/아이콘_물음표1.png")    # 물음표2.png size error
    o.show()


def o_explain():
    o.draw_image("/home/pi/Pibo_conversation/data/behavior/icon/아이콘_현재단계1.png")
    o.show(); time.sleep(1)
    o.draw_image("/home/pi/Pibo_conversation/data/behavior/icon/아이콘_현재단계2.png")
    o.show(); time.sleep(1)
    o.draw_image("/home/pi/Pibo_conversation/data/behavior/icon/아이콘_현재단계3.png")
    o.show(); time.sleep(1)


def o_photo():
    o.draw_image("/home/pi/Pibo_conversation/data/behavior/icon/아이콘_카메라.png")
    o.show()


def o_stamp():
    o.draw_image("/home/pi/Pibo_conversation/data/behavior/icon/아이콘_스탬프1.png")
    o.show()


def o_waiting():
    o.draw_image("/home/pi/Pibo_conversation/data/behavior/icon/아이콘_시계.png")
    o.show()


def o_cheer():
    o.draw_image("/home/pi/Pibo_conversation/data/behavior/icon/아이콘_음표1.png")
    o.show()


def o_compliment():
    o.draw_image("/home/pi/Pibo_conversation/data/behavior/icon/아이콘_엄지1.png")
    o.show()


def o_concil():
    o.draw_image("/home/pi/Pibo_conversation/data/behavior/icon/아이콘_default2.png")
    o.show()


def o_search():
    o.draw_image("/home/pi/Pibo_conversation/data/behavior/icon/아이콘_감지1.png")
    o.show()


def o_sleep():
    o.draw_image("/home/pi/Pibo_conversation/data/behavior/icon/아이콘_잠자기1.png")
    o.show()


def o_wakeup():
    o.draw_image("/home/pi/Pibo_conversation/data/behavior/icon/아이콘_날씨.png")
    o.show()


def o_agree():
    o.draw_image("/home/pi/Pibo_conversation/data/behavior/icon/아이콘_긍정.png")
    o.show()


def o_deny():
    o.draw_image("/home/pi/Pibo_conversation/data/behavior/icon/아이콘_부정.png")
    o.show()


def o_joy():
    o.draw_image("/home/pi/Pibo_conversation/data/behavior/icon/아이콘_default1.png")
    o.show()


def o_angry():
    o.draw_image("/home/pi/Pibo_conversation/data/behavior/icon/아이콘_default2.png")
    o.show()


def o_sad():
    o.draw_image("/home/pi/Pibo_conversation/data/behavior/icon/아이콘_default2.png")
    o.show()


def o_tired():
    o.draw_image("/home/pi/Pibo_conversation/data/behavior/icon/아이콘_배터리1.png")
    o.show()
