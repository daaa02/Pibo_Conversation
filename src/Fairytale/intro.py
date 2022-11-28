# -*- coding: utf-8 -*-

import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


if __name__ == "__main__":
    print("\n-----------------")
    print("1. 모기와 사자\n2. 개미와 베짱이")
    print("-----------------")
    choice = input("번호 입력: ")
    
    if choice == "1":
        os.system("python3 /home/pi/Pibo_Conversation/Fairytale/data/01_lions_story.py")
        os.system("python3 /home/pi/Pibo_Conversation/Fairytale/01_lions.py")
        
    elif choice == "2":
        os.system("python3 /home/pi/Pibo_Conversation/Fairytale/data/02_ants_story.py")
        os.system("python3 /home/pi/Pibo_Conversation/Fairytale/02_ants.py")
    