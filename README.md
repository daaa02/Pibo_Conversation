# Pibo_Conversation
파이보 대화 시나리오

## 0. 개발 환경
* Ubuntu 18.04 -> Raspberry Pi 4
* Python 3.7
* 동작&화면 기본 실행: `터미널에서 start 입력`

      pi@raspberrypi:~ $ start     # 안되면 python3 start.py 

## 1. 일상 대화
* 경로: Pibo_Conversation/src/Daily/~
* 실행 방법: ~~`터미널에서 daily 입력`~~

      pi@raspberrypi:~ $ daily

## 2. 동화 대화
* 경로: Pibo_Conversation/src/Fairytale/~
* 실행 방법: ~~`터미널에서 fairytale 입력`~~
  
       pi@raspberrypi:~ $ fairytale

* 문제 사항: 
  - 따옴표 안의 대사는 다른 목소리로? ➡ 그냥 한 줄씩 tts 걸었음(다음엔 X)

## 3. 역할 놀이 대화
* 경로: Pibo_Conversation/src/Roleplay/~
* 실행 방법: ~~`터미널에서 roleplay 입력`~~

       pi@raspberrypi:~ $ roleplay

## 4. 파이보 대화
* 경로: Pibo_Conversation/src/Solution/~
* 실행 방법: ~~`터미널에서 solution 입력`~~

       pi@raspberrypi:~ $ solution

* 문제 사항: NER 적용 안 해서 {친구이름} ➡ '그 친구' 로 대체

## 5. 업데이트
* 실행 방법: `터미널에서 update 입력`

       pi@raspberrypi:~ $ update

## 6. 체크리스트
* 해야할 것이나 확인 필요한 것들 등등
  - [ ] 답변 유형 수정 필요: positve ,action ➡ positive+action
  - [ ] NER 적용
  - [ ] 비전 인식 되는지 확인

