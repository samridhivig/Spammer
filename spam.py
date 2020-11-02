import pyautogui, time
time.sleep(5)
fh = open("script",'r')

for word in fh:
    pyautogui.typewrite(word)
    pyautogui.press("enter")He won't do it.





