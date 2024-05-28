from app.common.result import Res
import app.generate.ernie as generate
from . import main

from flask import Response, jsonify, request


@main.route("/generate/completion", methods=["POST"])
async def completion() -> Response:
    p = request.get_json().get("prompt").strip()
    response = await generate.complete(p)
    return Res(data=response).to_json()


@main.route("/generate/abstract", methods=["POST"])
async def abstract() -> Response:
    p = request.get_json().get("prompt").strip()
    word_count = request.get_json().get("word_count")
    response = await generate.abstract(p, word_count)
    return Res(data=response).to_json()


@main.route("/generate/translate", methods=["POST"])
async def translate() -> Response:
    p = request.get_json().get("prompt").strip()
    lang = request.get_json().get("lang").strip()
    response = await generate.translate(p,lang)
    return Res(data=response).to_json()

@main.route("/generate/polish", methods=["POST"])
async def polish() -> Response:
    p = request.get_json().get("prompt").strip()
    style = request.get_json().get("style").strip()
    response = await generate.polish(p,style)
    return Res(data=response).to_json() 

@main.route("/generate/fix", methods=["POST"])
async def fix() -> Response:
    p = request.get_json().get("prompt").strip()
    response = await generate.fix(p)
    return Res(data=response).to_json()



# TODO: 实现流式生成api