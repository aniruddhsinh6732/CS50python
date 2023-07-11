import random

while True:
    n = int(input("level : "))
    if n <= 0 :
        pass
    else:
        num = random.randint(1,n)
        
        while True:
            guess = int(input("Guess : "))
            if guess <= 0 : 
                pass
            else:
                break
            
        if num > guess:
            print("Too small!")
        elif num < guess:
            print("Too large!")
        else:
            print("Just right!")
        break


