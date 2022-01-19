# Allmytour Makers
Allmytour 기업협업 프로젝트

- [시연영상](https://www.youtube.com/watch?v=VA8rSx0cG7Q&ab_channel=%EA%B9%80%EC%98%81%ED%98%B8)
  
## Members
|이름   |Github                   |Position|
|-------|-------------------------|--------------------|
|고준영 |[jay95ko](https://github.com/jay95ko)     | 회원가입/mypage   |
|박지원 |[jiwon5304](https://github.com/jiwon5304) | 로그인/비밀번호 찾기   |
|윤현묵 |[fall031-muk](https://github.com/fall031-muk)| makers 지원하기/임시저장   |
|최현수 |[filola](https://github.com/filola) | makers/수정하기 |

## 프로젝트 내용
회사 측의 로컬 여행 가이드가 직접 여행 상품을 등록하는 웹 어플리케이션 개발 프로젝트
프로젝트 기능은 아래와 같습니다.
  - 회원가입/로그인 기능(비밀번호 찾기 포함)
  - 로그인을 진행한 사용자에 한하여 makers 지원하기 가능
  - 인적사항, 프로필 이미지, 증빙 서류 업로드 등 정보 입력
  - 정보 입력 중 임시저장 기능 가능
  - makers 제출 후 수정하기 기능 가능

</aside>

### [주요 고려 사항]
- 회원가입 관련 글
- makers 지원하기 도중 임시저장이 가능하도록 임시저장 table 따로 생성
- 이미지 및 파일 업로드를 위해 Django 내부 media 파일 전송 방식 이용

✔️ **API 상세설명**
---

- 회원가입/로그인 API
    - 비밀번호 암호화를 통한 회원가입 기능
    - 기본적인 로그인 기능과 로그인 유지 기능
    - 이메일을 인증을 통한 비밀번호 찾기 기능
- makers 지원하기/임시저장 API
    - 로그인을 진행한 이후 지원하기 가능
    - 필수 입력사항과 추가 입력사항 구분
    - 프로필 이미지 파일, 신분증, 통장사본, 증빙서류 등 파일 업로드
    - 지원하기 작성 중 임시저장 가능
- makers 수정하기 API
    - 수정하기 버튼 입력시 기존 데이터 출력
    - 출력시 저장된 이미지 파일들을 공통 ASCII 영역의 문자로 인코딩하여 전송
    - 이미지 파일 업로드
 
## 모델링
![image](https://user-images.githubusercontent.com/80630313/148648043-01315681-64ba-490a-a066-38b16c34a4ef.png)
  
## 구현 기능
### 회원가입
- 이름, 비밀번호, 이메일, 핸드폰번호, 마케팅 및 서비스 동의 항목을 입력받아 회원가입을 진행
- 이메일과 비밀번호는 정규표현식을 사용한 유효성 검사를 진행
- 비밀번호는 암호화를 적용하여 데이터베이스에 저장

### 로그인
- 로그인 유지값을 True or False로 받아 사용자가 로그인 유지를 요청시 30일동안 토큰값이 유지되도록 구현하였고, 기본적으로는 2시간으로 설정

### 비밀번호 찾기
- 이메일 인증을 통한 비밀번호 찾기 기능 구현
- 입력받은 이메일 정보로 10000~99999의 임의의 숫자를 발송하여 데이터베이스에 저장된 인증번호와 동일한지 확인
- 인증번호 확인이 되면 새로운 비밀

### maksers 지원하기/임시저장
- 필수 정보와 추가 정보를 입력받아 makers 지원하기(지원하기 시 필수 입력 값 미입력 시 지원할 수 없음)
- Django 내부 media 파일 전송 방식을 이용하여 프로필 이미지, 신분증, 통장사본, 증빙서류 등의 파일을 업로드
- 임시저장 table을 따로 작성하여 임시저장된 정보를 저장(필수 입력 값 미입력 시에도 임시저장 가능)

### maksers 수정하기
- 기존에 지원하기에서 입력된 정보들 출력
- base64를 통해 서버의 이미지 파일을 공통 ASCII 영역의 문자로 인코딩하여 전송(프론트에서 이를 받은 후 파일 출력)
- 기존 입력된 makers가 없다면 임시저장된 데이터를 출력
- 새롭게 입력된 데이터를 받아오기 전 기존의 데이터를 삭제하고 새롭게 데이터를 저장
- 언어, 지역, 투어와 같은 경우 검색을 통해 기존의 데이터를 넣을 수 있지만 기타를 통해 새로운 데이터 또한 입력가능

## 기술 스택
- Back-End : python, django, Mysql, 
- Tool     : Git, Gitlab, Slack, Flow

## 실행 방법(endpoint 호출방법)

### ENDPOINT

| Method | endpoint | Request Header | Request Body | Remark |
|:------:|-------------|-----|------|--------|
|POST|/users|access_token||마이페이지 기능|
|POST|/users/login||email,password,token_status|로그인 기능|
|POST|/users/signup||name,email,password,phone,agree(service,marketing)|회원가입 기능|
|POST|/users/sendemail||email|인증번호 이메일 전송 기능|
|POST|/users/auth||email,auth_number|인증번호 확인 기능|
|POST|/users/newpw|access_token|newpw|새로운 비민번호 설정 기능|
|POST|/makers/apply|access_token||makers 지원하기 기능(정보, 파일 등 업로드)|
|POST|/makers/draft|access_token||makers 임시저장 기능|
|POST|/makers/revise|access_token||makers 수정하기 기능|


## 폴더 구조
```
├── config
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── makers
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── media
│   ├── bankbook
│   │   ├── 투어메이커스_1차.pdf
│   ├── evidence
│   │   └── wecode.jpeg
│   ├── idcard
│   │   └── wecode_AwIsSIl.jpeg
│   └── profile
│       ├── wecode.jpeg
├── my_settings.py
├── requirement.txt
└── users
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── decorator.py
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── 0002_user_auth_number.py
    │   ├── __init__.py
    ├── tests.py
    ├── urls.py
    └── views.py

```
