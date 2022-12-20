import random
import time

if __name__ == "__main__":
    
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
        
    
