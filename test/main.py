from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message" : "안녕하세요? 테스트 중입니다."}