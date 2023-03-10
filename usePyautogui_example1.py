import pyautogui

pyautogui.FAILSAFE = True

distance = 80
pyautogui.moveTo(600,600,duration=1)
pyautogui.click()
while distance > 0:
    pyautogui.drag(distance, 0, duration = 0.5)
    distance -= 5
    pyautogui.drag(0, distance, duration = 0.5)
    pyautogui.drag(-distance, 0, duration = 0.5)
    distance -= 5
    pyautogui.drag(0, -distance, duration = 0.5)