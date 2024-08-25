#
#
# 노이즈 필터링 코드
#

import cv2
import numpy as np

# 카메라 영상을 받아올 객체 선언 및 설정(영상 소스, 해상도 설정)
capture = cv2.VideoCapture(0) # 웹캠을 2개 사용하는 경우 0 or 1
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = capture.read() 
    # 영상에 사용할 노이즈 생성. 이런 노이즈를 salt & pepper 노이즈라 함
    noise = np.uint8(np.ramdom.normal(loc=0, scale=0.4, size=[480, 640, 3]))
    noised_img = cv2.add(frame, noise) # 현재 영상에 노이즈를 더함
    # 노이즈 필터링1 : 화면을 흐리게(blur) 해줌
    # blur = cv2.blur(noised_img,(5,5))
    # 노이즈 필터링2 : 가우시안 필터를 이용해 blur, blur 필터에 비해 외곽선이 살아남
    # gaussian = cv2.GaussianBlur(noised_img,(5,5), 0)
    # 노이즈 필터링3 : bilateral 필터를 적용. 가우시안 필터보다 외각선을 더 살림
    # bilateral = cv2.bilateralFilter(noised_img,9,75,75)
    # 노이즈 필터링4 : 메디안 필터. salt & pepper 노이즈 제거에 탁월하며, 외곽선도 잘 살림
    # median_filtered = cv2.medianBlur(noised_img, 5)
    cv2.imshow("original", frame)
    cv2.imshow("noised", noised_img)
    # cv2.imshow("blur", blur)
    # cv2.imshow("gaussian", gaussian)
    # cv2.imshow("bilateral", bilateral)
    # cv2.imshow("median", median_filtered)

    #여러 영상을 하나로 합칠 때 사용
    # total = cv2.hconcat([cv2.vconcat([frame, noised_img]), cv2.vconcat([blur, gaussian]), cv2.vconcat([
    #     bilateral, median_filtered])])
    # cv2.imshow("total", total)

    if cv2.waitKey(1) == ord('q'):
        break

capture.release()   # 캡처 객체를 없애줌
cv2.destroyAllWindows() 
