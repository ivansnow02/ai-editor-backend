from ..common.result import Res
import app.generate.ernie as generate
from . import main

from flask import Response, jsonify, request



@main.route("/generate/completion", methods=["POST"])
async def completion() -> Response:
    p = request.json.get("prompt").strip()
    response = await generate.complete(p)
    return Res(data=response).to_json()


@main.route("/generate/abstract", methods=["POST"])
async def abstract() -> Response:
    p = request.json.get("prompt").strip()
    word_count = request.json.get("word_count")
    response = await generate.abstract(p, word_count)
    return Res(data=response).to_json()


@main.route("/generate/translate", methods=["POST"])
async def translate() -> Response:
    p = request.json.get("prompt").strip()
    lang = request.json.get("lang").strip()
    response = await generate.translate(p,lang)
    return Res(data=response).to_json()

@main.route("/generate/polish", methods=["POST"])
async def polish() -> Response:
    p = request.json.get("prompt").strip()
    style = request.json.get("style").strip()
    response = await generate.polish(p,style)
    return Res(data=response).to_json() 

@main.route("/generate/fix", methods=["POST"])
async def fix() -> Response:
    p = request.json.get("prompt").strip()
    response = await generate.fix(p)
    return Res(data=response).to_json()


# @main.route("/stream/completion", methods=["POST"])
# async def completion_sse():
#     p = request.json.get("prompt").strip()
#     response = await generate.complete(p)
#     res = Response(response, mimetype="text/event-stream")
#     res.headers["Cache-Control"] = "no-cache"
#     res.headers["Connection"] = "keep-alive"
#     return res
