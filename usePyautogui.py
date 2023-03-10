import pyautogui

# pyautogui.FAILSAFE = False 

width, height = pyautogui.size() # 显示器分辨率 1980 1080
print(width, height)

pyautogui.moveTo(100, 300, duration = 1) # 移动到指定位置（绝对坐标） duration是移动时间 1s
# pyautogui.click()
# pyautogui.moveRel(500, 100, duration = 1) # 相对移动，第一个是左右，第二个参数是向下移动
pyautogui.click()

pyautogui.typewrite("114514\n\b\b\b666",0.5)

#im = pyautogui.screenshot()
# im = pyautogui.screenshot(region=(0, 0, 300, 400)) # 左上角 右下角
# im.save('./image/screenshot.jpg')