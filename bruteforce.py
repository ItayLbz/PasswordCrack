import random
import pyautogui

chars="abcdefghijklmnopqrstuvwxyz0123456789"

allchar = list(chars)

pwd = pyautogui.password("Enter A Password: ")



def check():
    sample_pwd = ""

    while (sample_pwd != pwd):
        sample_pwd = random.choices(allchar,k=len(pwd))
        print(f"<===== {sample_pwd} =====>")

    print(f"The Correct Password is : {sample_pwd}")


check()
    
    