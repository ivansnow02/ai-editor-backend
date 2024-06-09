from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from paddleocr import PaddleOCR
import paddle
import uvicorn
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
ocrModel = PaddleOCR(use_angle_cls=True, lang="ch")
from app.routers import generate, stream, langserve, chat_with_history, format, ocr
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(generate.router)
app.include_router(stream.router)
app.include_router(langserve.router)
app.include_router(chat_with_history.router)
app.include_router(format.router)
app.include_router(ocr.router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
