from urllib import response

from app.generate.llm import generate
from . import main

from flask import Response, jsonify, request


@main.route("/completion", methods=["POST"])
async def completion() -> Response:
    if request.json is not None:
        response = await generate(request)
        return jsonify({"response": response})
    else:
        return jsonify({"error": "Invalid request."})
