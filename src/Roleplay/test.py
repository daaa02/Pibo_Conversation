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
        
if __name__ == "__main__":
    test_2()
