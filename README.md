# Pibo_Conversation
파이보 대화 시나리오

## 0. 개발 환경
* Ubuntu 18.04 -> Raspberry Pi 4
* Python 3.7
* 동작&화면 기본 실행: `터미널에서 start 입력`

      pi@raspberrypi:~ $ start     # 안되면 python3 start.py 

## 1. 일상 대화
* 경로: Pibo_Conversation/Daily/~
* 실행 방법: `터미널에서 daily 입력`

      pi@raspberrypi:~ $ daily

* 요일에 따라 바뀜, 현재 '수요일'로 고정
* 유치원 ➡ 장소 입력 가능하도록 변경 (이름, 장소 입력 후 대화 실행)
* "오늘" 뭐 배웠? ➡ "어제" 뭐 배웠?
* 문제 사항:

## 2. 동화 대화
* 경로: Pibo_Conversation/Fairytale/~
* 실행 방법: `터미널에서 fairytale 입력`
  
       pi@raspberrypi:~ $ fairytale

* 안내에 따라 1 또는 2 입력하면 동화 읽어주고 대화시작
* 문제 사항: 
  - ~~동화 데이터가 없음(현재 교육용 라이브러리 사용)~~ ➡ 받음
  - 따옴표 안의 대사는 다른 목소리로? ➡ 그냥 한 줄씩 tts 걸었음(다음엔 X)

## 3. 역할 놀이 대화
* 경로: Pibo_Conversation/Roleplay/~
* 실행 방법: `터미널에서 roleplay 입력`

       pi@raspberrypi:~ $ roleplay

* rp1, rc1, rc2, rc3 고정
* 문제 사항: ~~효과음 길이가 제각각~~ ➡ trim to 3sec, .mp3 to .wav

## 4. 파이보 대화
* 경로: Pibo_Conversation/Solution/~
* 실행 방법: `터미널에서 solution 입력`

       pi@raspberrypi:~ $ solution

* ~~NER 이용하여 이름 또는 동물이름 구분하는 기능 추가~~ NER 하는 중  !!
* 문제 사항: NER 적용 안 해서 {친구이름} ➡ '그 친구' 로 대체

## 5. 업데이트
* 실행 방법: `터미널에서 update 입력`

       pi@raspberrypi:~ $ update

## 6. 체크리스트
* 개발 진척이나 확인 필요한 것들 등등
  - [x] 개체명 인식(NER) 모델 
  - [ ] 시나리오 하면서 NER 바로바로 되는지?
  - [x] 명사 + 은/는/이/가 맞추기
  - [x] STT 모듈 timeout 기능 구현(?) ➡ 10초를 기준으로, 3번 기회 제공
  - [ ] 코드 단순화 작업: STT 실행 및 대답 처리, 대응 등을 하나의 모듈로
  - [ ] 코드 단순화 작업: TTS 와 인터랙션을 하나의 모듈로

