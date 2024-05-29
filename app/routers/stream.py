import app.generate.ernie as generate
from fastapi.responses import StreamingResponse
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/api/stream",
    tags=["stream"],
    responses={404: {"description": "Not found"}},
)


class Req(BaseModel):
    prompt: str
    style: str = None
    word_count: int = None
    lang: str = None


@router.post("/completion")
async def completion(req: Req) -> StreamingResponse:
    p = req.prompt.strip()
    async def gen():
        async for chunk in generate.complete_stream(p):
            yield f"data: {chunk}\n\n"
        yield "event: finished\n\n"
    return StreamingResponse(gen(), media_type="text/event-stream")

@router.post("/abstract")
async def abstract(req: Req) -> StreamingResponse:
    p = req.prompt.strip()
    word_count = req.word_count
    async def gen():
        async for chunk in generate.abstract_stream(p, word_count):
            yield f"data: {chunk}\n\n"
        yield "event: finished\n\n"
    return StreamingResponse(gen(), media_type="text/event-stream")

@router.post("/translate")
async def translate(req: Req) -> StreamingResponse:
    p = req.prompt.strip()
    lang = req.lang.strip()
    async def gen():
        async for chunk in generate.translate_stream(p, lang):
            yield f"data: {chunk}\n\n"
        yield "event: finished\n\n"
    return StreamingResponse(gen(), media_type="text/event-stream")

@router.post("/polish")
async def polish(req: Req) -> StreamingResponse:
    p = req.prompt.strip()
    style = req.style.strip()
    async def gen():
        async for chunk in generate.polish_stream(p, style):
            yield f"data: {chunk}\n\n"
        yield "event: finished\n\n"
    return StreamingResponse(gen(), media_type="text/event-stream")

@router.post("/fix")
async def fix(req: Req) -> StreamingResponse:
    p = req.prompt.strip()
    async def gen():
        async for chunk in generate.fix_stream(p):
            yield f"data: {chunk}\n\n"
        yield "event: finished\n\n"
    return StreamingResponse(gen(), media_type="text/event-stream")
