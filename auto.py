import random, pyautogui, pyauto
while True:
    h=random.randint(0,1080)
    w=random.randint(0,1920)
    pyauto.click(h,w,duration=0.3)
    