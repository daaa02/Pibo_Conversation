import random



if __name__ == '__main__':
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
        

