# Moim으로 모임  💜

<br>

혼자  /  친구 / 연인과 어디서 놀지 모르시겠다구요?

카페, 맛집, 술집 등 다양한 엔터테인먼트를 추천해주는 서비스 'Moim으로 모임'이 있습니다.

<br><br>

#### 서비스 사용 방법 
<br>

:key: 저희 서비스는 로그인을 **꼭** 하셔야 이용하실 수 있습니다.

<br>

👭 로그인을 하셨다면, 모임을 생성해주세요!  

> 누구와 함께하는 모임인지, 나이대는 어느 정도인지 입력해주세요.

<br>

👀 우리는 당신의 모임들의 취향을 추천해줄게요!

> 나이대에 맞는, 성별에 맞는, 모임에 맞는 장소 선택은 저희에게 맡기시고 놀 준비만 해주세요

<br>



####  개발 진행 상황

- 김민주 : 풀스택 개발 (약속 생성, 수정, 확인 페이지 개발)
- 김성웅 : DB 설계 및 풀스택 개발 (회원가입, 로그인, 유저 정보, 음식점 정보 페이지 구현)
- 김수현 : DB 설계 및 데이터 크롤링 / 협업 필터링 알고리즘 고도화
- 박수철 : 풀스택 개발 (회원가입, 로그인, 유저 정보, 음식점 정보 페이지 구현)
- 박재림 : 팀장 및 리뷰데이터에서 가게 키워드 추출 (TF-IDF모델 기반) 및 풀스택 개발(모임 페이지 구현)


<br><br>


#### 실행방법

**Backend**

```sh
cd findstore
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py initialize
python manage.py initialize2
python manage.py initialize3
python manage.py runserver

```

**Frontend**

```sh
cd findstore_vue
npm install
npm run serve
```
