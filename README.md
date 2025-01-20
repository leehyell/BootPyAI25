# BootPyAI25
<br/>
스프링부트, 파이썬, AI 협업 모듈
<br/><br/>
◆ 개발환경 구축
<br/>
└ 파이썬 인터프리터
<br/>
  └ http://www.python.org/
<br/>
└ 3.12 버전 설치(3.8 이상 필수)

<br/><br/>
◆ IDE 설치
<br/>
└ https://www.jetbrains.com/pycharm/download/?section=windows
<br/>
└ 커뮤니티 설치

<br/><br/>
◆ FastAPI 설치
<br/>
└ pip install fastapi uvicorn uvicorn : ASGI(Asynchronus Server Gateway Interface)
<br/>
  └ 파이썬에서 비동기 웹서버와 웹 애플리케이션 간의 인터페이스 표준 ASGI는 기존 WSGI(Web Server Gateway Interface)의 비동기 버전.
<br/>
  └ 파이썬에서 비동기 처리를 지원하는 웹 애플리케이션을 구축하기 위함.
<br/>
  └ https://velog.io/@hwaya2828/WSGI-ASGI

<br/><br/>
◆ ASGI 특징
<br/>
└ 비동기 지원
<br/>
  └ ASGI는 비동기 코드 실행을 지원하며 높은 성능과 동시성을 제공, 웹 소켓이나 서버 푸시와 같은 비동기 통신이 필요한 애플리케이션에 유용.
<br/>
  └ 범용성
<br/>
    └ HTTP 뿐만 아니라 WebSocket, gRPC와 같은 다른 프로토콜로 지원.
<br/>
  └ 유연성
<br/>
    └ ASGI 애플리케이션은 다양한 서버 및 프레임 워크와 호환되며 모듈식으로 구성

<br/><br/>
◆ FAST API와 ASGI
<br/>
└ FASTAPI는 ASGI 표준을 따르는 웹 프레임 워크.
<br/>
└ FASTAPI 애플리케이션은 비동기 처리를 기본으로 Uvicorn과 같은 ASGI 서버를 사용해 높은 성능 제공.
<br/>
└ FASTAPI 서버 실행

<br/><br/>
◆ main.py 실행
<br/><br/>
![image](https://github.com/user-attachments/assets/8283e9d3-b02a-40f2-b6d6-d1581ce01f02)

└ Terminal에서 D:\phthonWorkSpace > uviconr main:app --reload --port 8001(위치 확인)

<br/><br/>
2025.01.17 ~
