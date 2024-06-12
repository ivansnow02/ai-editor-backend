import hashlib
import io
import os

from PIL import Image
from fastapi import APIRouter, File, Query, UploadFile
from typing import Union

from app.utils import Res, ocrModel

router = APIRouter(
    prefix="/api/img",
    tags=["img"],
    responses={404: {"description": "Not found"}},
)


@router.post(path="/upload")
async def uploadImg(file: UploadFile = File(...)):
    # 保存图片
    img = Image.open(io.BytesIO(await file.read()))
    dir_path = "static/"
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    if file.filename is None:
        return Res(code=400, msg="file name is None")
    img_path = dir_path+f"{hashlib.md5(file.filename.encode()).hexdigest()}.png"
    img.save(img_path)

    return Res(data={'url':img_path})


@router.get(path="/ocr/")
async def ocrImg(img_path: Union[str, None] = Query(
    default=None, title="图片路径", description="图片路径", example="static/xxx.png", alias="img_path",pattern=r"static/.*\.png"
)):
    if img_path is None:
        return Res(code=400, msg="img_path is None")
    # file_name = img_path.split("/")[-1]
    # fpath = './../static/' + file_name
    print(img_path)
    result = ocrModel.ocr(img=img_path, cls=True)
    texts = [item[1][0] for res in result for item in res]

    return Res(data=texts)
