import uvicorn
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlmodel import SQLModel

from app.db import engine
from app.dependencies import get_current_user
from app.routers import auth, chat_with_history, format, langserve, ocr, user
from config import settings
from dotenv import load_dotenv

load_dotenv()

SQLModel.metadata.create_all(engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    langserve.router,
    dependencies=[Depends(get_current_user)],
)
app.include_router(
    chat_with_history.router,
    dependencies=[Depends(get_current_user)],
)
app.include_router(
    format.router,
    dependencies=[Depends(get_current_user)],
)
app.include_router(
    ocr.router,
    dependencies=[Depends(get_current_user)],
)
app.include_router(
    user.router,
    dependencies=[Depends(get_current_user)],
)
app.include_router(auth.router)
app.mount("/static", StaticFiles(directory="static"), name="static")


def run():
    uvicorn.run(
        app=app,
        host=settings.HOST,
        port=settings.PORT,
    )


if __name__ == "__main__":
    run()
