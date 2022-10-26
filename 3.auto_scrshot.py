from PIL import ImageGrab
import time

# 프로그램 실행 후, 5초 기다렸다가 2초 간격으로 10개 이미지 자동 캡쳐
time.sleep(5)
for i in range(1,11) :                 # 이미지 개수 10개
    img = ImageGrab.grab()             # 현재 스크린 이미지를 캡쳐
    img.save("Image{}.png".format(i))  
    time.sleep(2)                      # 2초 간격!!