import pyautogui
import time

pyautogui.FAILSAFE = True

def zan():
    time.sleep(0.5)    # 等待 0.5 秒
    left, top, width, height = pyautogui.locateOnScreen('image/zan.png')   # 寻找 点赞图片；
    center = pyautogui.center((left, top, width, height))    # 寻找 图片的中心
    pyautogui.click(center, duration=0.5)    # 点击
    print('点赞成功！')

try:
    while True:
        if pyautogui.locateOnScreen('image/zan.png'):
            zan()   # 调用点赞函数
        else:
            pyautogui.scroll(-500)    # 本页没有图片后，滚动鼠标；
            print('没有找到目标，屏幕下滚~')
except pyautogui.FailSafeException:
    print('已退出！')
