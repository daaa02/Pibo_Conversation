import os, sys
import time

sys.path.append("/home/kiro/workspace/Conversation_Scenarios/data")

from conversation_manage import ConversationManage
from text_to_speech import text_to_speech

# import motion.behavior_list

stt = ConversationManage()


a = stt.responses_proc(re_q="10초 후 재질문")
if a == "positive":
    behavior_list.do_question_L("dd")

# behavior_list.do_question_L("안녕")

# behavior_list.do_joy_A("안녕! 우리가 드디어 만나게 되었구나! 나는 파이보야, 너는 이름이 뭐니? ")
# stt.responses_proc(re_q="너는 이름이 뭐니? ")
