
import cv2
import datetime
from PIL import ImageFont, ImageDraw, Image
import numpy as np

# opencv python 코딩 기본 틀
# 카메라 영상을 받아올 객체 선언 및 설정(영상 소스, 해상도 설정)
capture = cv2.VideoCapture(0) # 웹캠을 2개 사용하는 경우 0 or 1
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 글꼴 파일을 불러옴
font = ImageFont.truetype('fonts/SCDream6.otf', 20)

while True:
    now = datetime.datetime.now()
    nowDateTime = now.strftime('%Y-%m-%d %H:%M:%S')

    ret, frame = capture.read()     # 카메라로부터 현재 영상을 받아 frame에 저장, 잘 받았다면 ret가 참
    # 글자가 잘보이도록 배경을 넣어줌
    # img는 사각형을 넣을 이미지, pt1, pt2는 사각형의 시작점과 끝점, color는 색상(파랑, 초록, 빨강) thickness는 선굵기(-1은 내부를 채움)
    cv2.rectangle(img=frame, pt1=(10, 15), pt2=(340, 35), color=(0,0,0), thickness=-1)

    # 아래 4줄은 글자를 영상에 더해주는 역할
    frame = Image.fromarray(frame)
    draw = ImageDraw.Draw(frame)
    # xy는 텍스트 시작 위치, text는 출력할 문자열, font는 글꼴, fill은 글자색
    draw.text(xy=(10, 15), text="웹캠 " + nowDateTime, font=font, fill=(255, 255, 255))
    frame =np.array(frame)

    cv2.imshow("text", frame)   # 현재 시간을 표시하는 글자를 써준 영상 출력
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

