import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlmodel import SQLModel

from app.db import engine
from app.routers import langserve, chat_with_history, format, ocr, user
from config import settings

SQLModel.metadata.create_all(engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(langserve.router)
app.include_router(chat_with_history.router)
app.include_router(format.router)
app.include_router(ocr.router)
app.include_router(user.router)
app.mount("/static", StaticFiles(directory="static"), name="static")


def run():
    uvicorn.run(
        app=app,
        host=settings.HOST,
        port=settings.PORT,
    )


if __name__ == "__main__":
    run()
