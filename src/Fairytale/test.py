
class Test:
  
    
    def main1(self):
        
        while True:
            bhv=input('bhv: ')
            pos_bhv=input('pos_bhv: ')
            neu_bhv=input('neu_bhv: ')
            neg_bhv=input('neg_bhv: ')
            
            string=input('string: ')
            pos=input('pos: ')
            neu=input('neu: ')
            neg=input('neg: ')
            
            # {wm.word(user_name, 0)}
                    
            print(f'cm.tts(bhv="{bhv}", string=f"{string}")')
            print(f'answer = cm.responses_proc(re_bhv="do_{bhv}", re_q=f"{string}", pos_bhv="do_{pos_bhv}", pos=f"{pos}", neu_bhv="do_{neu_bhv}", neu=f"{neu}", neg_bhv="do_{neg_bhv}", neg=f"{neg}", act_bhv="do_{pos_bhv}", act=f"{pos}")')

            print('\n')



        # 3. 피드백 수집
        time.sleep(1)                   
        pibo = cm.tts(bhv="do_question_S", string="파이보랑 노는 거 재미있었어? 재밌었는지, 별로였는지 얘기해줄래?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"파이보랑 노는 거 재미있었어?") 
              
        if answer[0][0] == "negative":
            self.score = [0.0, -0.5, 0.0, 0.0]
        
        if answer[0][0] == "positive":
            self.score = [0.0, 0.5, 0.0, 0.0]
            
        if answer[0][0] != "negative" and answer[0][0] != "positive": # if answer[0][0] == "neutral":
            self.score = [0.0, -0.25, 0.0, 0.0]
        
        cwp.writerow([today, filename, self.score[0], self.score[1], self.score[2],self.score[3]])
        
        # 4. Paradise framework 기록
        turns = sum((self.reject[i] + 1) * 2 for i in range(len(self.reject)))  
        reject = sum(self.reject) 
        
        cwc.writerow(['Turns', turns])
        cwc.writerow(['Rejections', reject])
        cwc.writerow(['Misrecognitions', ])

        cwc.writerow(['%Turns', ])
        cwc.writerow(['%Rejections', ])
        cwc.writerow(['%Misrecognitions', ])

        # 5. 활동 완료 기록
        gss.write_sheet(name=self.user_name, today=today, activities=filename)




if __name__ == "__main__":
    test = Test()
    test.main1()
    
    
    