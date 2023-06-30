import os, sys
import time

from openpibo.device import Device
from openpibo.oled import Oled
from openpibo.motion import Motion

sys.path.append('/home/pi/Pibo_Conversation')

motion = Motion()
device = Device()
oled = Oled()

motion.set_motion("m_wakeup", 1)

os.system("python3 /home/pi/Pibo_Conversation/src/start_touch.py")