#!/usr/bin/python3

# python module
import time

# openpibo module
from openpibo.device import Device

"""
NEOPIXEL(20) -> ex) #20:255,255,255:!

# 20: 색 변경
# 21: 속도 d(ms)만큼 천천히 변경
# 22: 밝기 조절(기본 64)
# 25: 무지개 눈, d(ms)의 속도로 색 변화

"""

device = Device()


def e_question():
    device.send_cmd(20, '108,209,239')


def e_suggestion():
    device.send_cmd(20, '108,209,239')


def e_explain():
    # device.send_cmd(21, '108,209,239,100')
    device.send_cmd(20, '108,209,239')


def e_photo():
    device.send_cmd(20, '153,255,51')


def e_stamp():
    device.send_cmd(20, '255,51,255')


def e_waiting():
    # device.send_cmd(21, '108,209,239,10')
    device.send_cmd(20, '108,209,239')


def e_compliment():
    device.send_cmd(20, '255,180,232')
    time.sleep(0.5)
    device.send_cmd(20, '120,230,208')
    time.sleep(0.5)
    device.send_cmd(20, '251,245,155')


def e_agree():
    device.send_cmd(20, '108,209,239')


def e_joy():
    device.send_cmd(21, '255,180,232,5')
    time.sleep(0.1)
    device.send_cmd(21, '120,230,208,5')
    time.sleep(0.1)
    device.send_cmd(21, '251,245,155,5')


def e_sad():
    # device.send_cmd(21, '186,147,223,10')
    device.send_cmd(20, '152,66,186')


if __name__ == "__main__":
    e_compliment()