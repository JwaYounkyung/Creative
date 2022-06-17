# Creative

### Outcome 1
* 실행 : python Outcome1/code/dataCrawling.py
* output : Outcome1/result 
    * category별 크롤링한 데이터

### Outcome 2
* 실행 : python Outcome2/code/train.py
* input : Outcome2/data
    * train 4500개, test 500개, label 6종류
* output : Outcome2/result
    * result.csv : test accuracy를 얻기 위한 파일
    * result.pt : 학습한 model

### Outcome 3 
* 실행 
    * python Outcome3/code/autoLabeling.py
        * autoLabeling을 위해 dataCrawling 수정
    * python Outcome3/code/autoLabeling.py
* input : Outcome3/data
    * morpholgy_fixed.csv : autoLabeling에 맞춰 수정된 데이터
* output : Outcome3/result
    * labeled_morphology.csv : labeled data
