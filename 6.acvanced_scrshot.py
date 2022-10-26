import keyboard
from PIL import ImageGrab
import time

def scrshot() :
    cur_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(cur_time))  # image_20200618_034650 형식으로 출력

keyboard.add_hotkey("F9", scrshot)   # F9 키 실행값 등록
keyboard.wait("Esc")                 # 반복 종료키 설정
