
#
#  영상 조정 코드
#

import cv2
import numpy as np
from opencv_scene_functions import *


capture = cv2.VideoCapture(0) # 웹캠을 2개 사용하는 경우 0 or 1
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = capture.read()     # 카메라로부터 현재 영상을 받아 frame에 저장, 잘 받았다면 ret가 참
    cv2.imshow("original", frame)   # frame(카메라 영상)을 original 이라는 창에 띄어줌
    filtered = color_filter(frame, 'red', 1.2)  # 원본 영상에서 빨간색을 강조
    cv2.imshow("red", filtered)     # 색감을 바꾼 영상 출력
    brightness = set_brightness(frame, 20)      # 밝기를 전체적으로 20픽셀 밝게 해줌
    cv2.imshow("brightness", brightness)    # 밝기를 바꾼 영상 출력
    constrast = set_contrast(frame, 0.9)    # 대비를 0.9만큼 변경
    cv2.imshow("constrast", constrast)      # 대비를 바꾼 영상 출력
    big_size = set_size(frame, 2)
    cv2.imshow("bigsize", big_size)

    if cv2.waitKey(1) == ord('q'):  # 키보드의 q 를 누르면 무한루프에서 탈출
        break

capture.release()   # 캡처 객체를 없애줌
cv2.destroyAllWindows() # 모든 영상 창을 닫아줌