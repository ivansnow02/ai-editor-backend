from app.common.result import Res
import app.generate.ernie as generate

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/api/generate",
    tags=["generate"],
    responses={404: {"description": "Not found"}},
    
)

class Req(BaseModel):
    prompt: str
    style: str = None
    word_count: int = None
    lang: str = None


@router.post("/completion")
async def completion(req: Req) -> Res:
    p = req.prompt.strip()
    response = await generate.complete(p)
    return Res(data=response)


@router.post("/abstract")
async def abstract(req: Req) -> Res:
    p = req.prompt.strip()
    word_count = req.word_count
    response = await generate.abstract(p, word_count)
    return Res(data=response)


@router.post("/translate")
async def translate(req: Req) -> Res:
    p = req.prompt.strip()
    lang = req.lang.strip()
    response = await generate.translate(p, lang)
    return Res(data=response)


@router.post("/polish")
async def polish(req: Req) -> Res:
    p = req.prompt.strip()
    style = req.style.strip()
    response = await generate.polish(p, style)
    return Res(data=response)


@router.post("/fix")
async def fix(req: Req) -> Res:
    p = req.prompt.strip()
    response = await generate.fix(p)
    return Res(data=response)



