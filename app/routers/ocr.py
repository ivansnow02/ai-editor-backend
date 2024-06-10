import hashlib
import io
import os
import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile
from unittest import result

import numpy as np
from PIL import Image
from fastapi import APIRouter, File, UploadFile

from . import ocrModel
from ..common.result import Res

router = APIRouter(
    prefix="/api/ocr",
    tags=["ocr"],
    responses={404: {"description": "Not found"}},
)


@router.post(path="/uploadimg")
async def uploadimg(file: UploadFile = File(...)):
    try:
        if file is None:
            return {"error": "file is None"}

        # Read the file as bytes
        file_bytes = await file.read()

        # Convert the bytes to a numpy array
        image = Image.open(io.BytesIO(file_bytes))
        img_array = np.array(image)

        result = ocrModel.ocr(img_array, cls=True)
        texts = [item[1][0] for res in result for item in res]
    finally:
        file.file.close()
    return Res(data=texts)
