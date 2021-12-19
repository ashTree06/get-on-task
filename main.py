import time
import os

def timer(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    os.system("TASKKILL /F /IM firefox.exe")  #insert any application that you want to close
        
        

t = input("Enter the time in seconds: ")
  
# function call
timer(int(t))