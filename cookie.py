import os
import time

score = 0

while True:  
    answer = input("wil je klikken\nja of nee\n")
    if answer == ("ja"): 
        score = score + 1
        time.sleep(1)
        os.system('cls')
        continue
    else:
        
        time.sleep(1)
        os.system('cls')
        print("jou score was", score)
        break