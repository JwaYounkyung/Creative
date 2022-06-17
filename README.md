# Creative

설치 방법 python3 -m pip install -r requirements.txt

실행 명령어 python3 JetsonYolo.py 실행시, bounding box가 그려진 이미지와, Grid Map이 보여집니다. 실행 중 'q'를 누르면 실행을 정지합니다.

옵션 -v : "cam" or "video path", (예시 : python3 JetsonYolo.py -v ./video/test_video.mp4) "cam" 옵션은 calibration이 맞추어진 Jetson Nano에서 동작함을 확인했습니다.

-who : "student" or "professor" (전컴 C동 주차장은 교수전용 주차장이 정해져 있습니다. 위 옵션으로 교수전용, 학생용 주차공간을 보여줍니다.)

데이터셋 학습 모델은 coco dataset으로 pre-train한 weight를 사용하였습니다. https://cocodataset.org/ 추가로 중간과정에 사용한 주차공간 데이터셋은 아래와 같습니다. http://cnrpark.it/ https://public.roboflow.com/object-detection/pklot