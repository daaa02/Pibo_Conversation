# -*- coding: utf-8 -*-

import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


if __name__ == "__main__":
    print("\n-----------------")
    print("1. 모기와 사자\n2. 개미와 베짱이")
    print("-----------------")
    choice = input("번호 입력: ")
    
    if choice == "1":
        os.system("python3 /home/pi/Pibo_Conversation/src/Fairytale/data/03_mosquito_story.py")
        os.system("python3 /home/pi/Pibo_Conversation/src/Fairytale/data/03_mosquito.py")
        
    elif choice == "2":
        os.system("python3 /home/pi/Pibo_Conversation/src/Fairytale/data/05_ants_story.py")
        os.system("python3 /home/pi/Pibo_Conversation/src/Fairytale/data/05_ants.py")
    