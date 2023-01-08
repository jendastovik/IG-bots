import pyautogui, time, sys
print('Press Ctrl-C to quit.')
while True:
    CurserPos = pyautogui.position()
    print(CurserPos)
    time.sleep(2)
    sys.stdout.flush()