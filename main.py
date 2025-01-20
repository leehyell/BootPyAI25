#uvicorn: 톰캣 서버 같은거
from http.client import responses
from idlelib.help_about import version


#파이썬 웹개발 API
from fastapi import FastAPI

#유효성 검사용 판다틱
from pydantic import BaseModel

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
#요청(request), 응답(response) 사이에 특정 작업을 수행.
#미들웨어는 모든 요청에 대해 실행 되며, 요청을 처리하기 전이나 응답을 반환하기 전에 특정 작업을 수행.
#예를 들어 로깅, 인증, cors 처리, 압축 등.

#로그 출력용(console 같은)
import logging

from starlette.requests import Request
from starlette.responses import Response

#fastAPI() 객체를 생성해서 app 변수에 넣음.
app = FastAPI(
    title = "MBC AI 프로젝트 test",
    description = "Python과 JAVA BOOT를 연동한 AI 앱",
    version = "1.0.0",
    #안 쓸 때는 활성화, 사용할거면 주석(http://localhost:8001/docs)
    docs_url = None,
    #안 쓸 때는 활성화, 사용할거면 주석(http://localhost:8001/redoc)
    redoc_url = None
    #생성자를 통해 포스트맨을 대체하는 내장 문서화 툴.
    #보안상 None처리
)

#로그를 콘솔에 출력하는 용도.
class LoggingMiddleware(BaseHTTPMiddleware):
    #로그 출력 추가
    logging.basicConfig(level=logging.INFO)
    async def dispatch(self, request, call_next):
        logging.info(f"Req: {request.method}{request.url}")
        response = await call_next(request)
        logging.info(f"Status Code: {response.status_code}")
        return  response

#모든 요청에 대해 로그를 남기는 미들웨어 클래스를 사용.
app.add_middleware(LoggingMiddleware)

#컨트롤러 검증은 postman으로 활용해봄.
#내장된 백 검증 툴도 있음.

#아이템 객체 생성(BaseModel;객체 연결 → 상속)
class Item(BaseModel):
    #필드1;상품명    문자열
    name: str
    #필드2;설명     문자열
    description : str = None
    #필드3;가격     실수형
    price : float
    #필드4;세금     실수형
    tax : float = None

#http://ip주소:포트번호/루트컨텍스트
@app.get("/")
async  def read_root():
    return {"HELLO" : "world"}

#http://ip주소:포트번호/items/
#포스트 메소드용 응답.
@app.post("/items/")
async def create_item(item : Item):
    #BaseModel은 데이터 모델링을 쉽게 도와주며 유효성 검사를 수행.
    #잘 못된 데이터가 들어오면 422 오류 코드를 반환.
    return item

#http://ip주소:포트번호/items/n
@app.get("/items/{item_id}")
async def read_item(item_id : int, q : str = None):
    return {"item_id" : item_id, "q" : q}
#item_id  :  상품 번호      (경로 매개변수)
#q        :  기본값 None    (쿼리 매개변수)


#더 공부하고 싶으면
#https://wikidocs.net/book/8531