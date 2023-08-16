import pyautogui, time
time.sleep(10); f = open("spamtext.txt", "r")
lines_read = 0

for line in f:
    pyautogui.typewrite(line)
    pyautogui.press("enter")
    lines_read += 1
    if lines_read >= 4563:
        lines_read = 0
        f.seek(0)
