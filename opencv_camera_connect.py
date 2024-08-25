#
# opencv python 코딩
# 카메라 연결 코드
#

import cv2

# opencv python 코딩 기본 틀
# 카메라 영상을 받아올 객체 선언 및 설정(영상 소스, 해상도 설정)
capture = cv2.VideoCapture(0) # 웹캠을 2개 사용하는 경우 0 or 1
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = capture.read()     # 카메라로부터 현재 영상을 받아 frame에 저장, 잘 받았다면 ret가 참
    cv2.imshow("original", frame)   # frame(카메라 영상)을 original 이라는 창에 띄어줌
    if cv2.waitKey(1) == ord('q'):  # 키보드의 q 를 누르면 무한루프에서 탈출
        break

capture.release()   # 캡처 객체를 없애줌
cv2.destroyAllWindows() # 모든 영상 창을 닫아줌