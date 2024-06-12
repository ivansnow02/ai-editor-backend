import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.log import init_log
from app.routers import langserve, chat_with_history, format, ocr
class Server:
    def __init__(self):
        init_log()
        self.app = FastAPI()
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        self.app.include_router(langserve.router)
        self.app.include_router(chat_with_history.router)
        self.app.include_router(format.router)
        self.app.include_router(ocr.router)
        self.app.mount("/static", StaticFiles(directory="static"), name="static")



