from typing import Any
from pydantic import BaseModel

class Res(BaseModel):
    code: int = 200
    data: Any = None
    msg: str = "success"

    def __init__(self, **data: Any):
        super().__init__(**data)
