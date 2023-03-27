# -*- coding: utf-8 -*-

import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


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
    