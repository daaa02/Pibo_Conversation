
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



if __name__ == "__main__":
    test = Test()
    test.main1()
    
    
    