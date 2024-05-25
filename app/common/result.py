from typing import Any

from flask import jsonify


class Res:
    code: int
    data: Any
    message: str

    def __init__(self, code: int = 200, data: Any = None, message: str = "success"):
        self.code = code
        self.data = data
        self.message = message

    def to_json(self):
        return jsonify({"code": self.code, "data": self.data, "message": self.message})
