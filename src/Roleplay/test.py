import random
import time


def test_1():
    
    rand = random.sample(range(0,3), 2)
    print(rand)

    count = 0
    while True:
        for i in range(len(rand)):
            
            if rand[i] == 0:
                print("0")
                count += 1
                continue
            
            elif rand[i] == 1:
                print("1")
                count += 1
                continue
                
            elif rand[i] == 2:
                print("2")
                count += 1
                continue
                
        if count < 2:
            print("ss")
            time.sleep(2)
            continue     

        elif count == 2:
            print("end")
            break 
        
    
def test_2():
    
    print("ㄱㄱㄱㄱㄱ")
    said = input("input: ")

    genre_list = ['ㅋㅋ', 'ㅌㅌ', 'ㅊㅊ']
    genre = random.choice(genre_list)

    while True:
        
        if said == "no" or "123":
            
            
            genre_list.remove(genre)
            genre = random.choice(genre_list)
            print(genre_list, genre)
            
            
            print("ㄴㄴㄴㄴㄴ")
            said = input("input: ")
            continue
        
        if said == "yes":
            print("yessss")
            break
        
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
    test_2()
