import hashlib
import io
import os
import base64
from sqlmodel import SQLModel
import numpy as np
from PIL import Image
from fastapi import APIRouter, Depends, File, Query, UploadFile

from app import crud
from app.dependencies import get_current_user
from app.models import ImageModel, UserPublic
from app.utils.ocr import init_ocr
from app.utils.result import Res
from config import settings

BASE_URL = f"http://{settings.HOST}:{settings.PORT}"
router = APIRouter(
    prefix="/api/img",
    tags=["img"],
    responses={404: {"description": "Not found"}},
)

ocrModel = init_ocr()


# @router.post(path="/upload")
# async def upload_img(
#     file: UploadFile = File(...),
#     user: UserPublic = Depends(get_current_user),
# ):
#     # 保存图片
#     img = Image.open(io.BytesIO(await file.read()))
#     dir_path = "static/"
#     p = f"{dir_path}{user.id}/"
#     if file.filename is None:
#         return Res(code=400, msg="file name is None")
#     if not os.path.exists(p):
#         os.makedirs(p)
#     img_path = f"{p}{hashlib.md5(file.filename.encode()).hexdigest()}.{file.filename.split('.')[-1]}"
#     img.save(img_path)
#
#     image = crud.create_img(
#         img=ImageModel(path=f"{BASE_URL}/{img_path}", user_id=user.id)
#     )
#
#     return Res(data=image.model_dump())


# @router.get(path="/{img_id}")
# async def get_img(
#     session: Session = Depends(dependency=get_db),
#     img_id: int = Path(
#         ..., title="图片id", description="图片id", example=1, alias="img_id"
#     ),
#     user: UserPublic = Depends(get_current_user),
# ):
#     image = crud.get_img(session=session, pk=img_id)
#     if image is None:
#         return Res(code=400, msg="img is None")
#     if image.user_id != user.id:
#         return Res(code=400, msg="img is not belong to you")
#     return Res(data=image.model_dump())
#

class ImgIn(SQLModel):
    img_b64: str


@router.post(path="/ocr")
async def ocr_img(imgIn: ImgIn):
    img_b64 = imgIn.img_b64
    if img_b64 is None:
        return Res(code=400, msg="img is None")

    img_b64 = img_b64.split(",")[-1]
    # Base64 to image
    img = Image.open(io.BytesIO(base64.b64decode(img_b64)))
    # Convert PIL Image to numpy array
    img_np = np.array(img)

    result = ocrModel.ocr(img=img_np)
    if not result:
        return Res(code=400, msg="ocr failed")
    texts = [item[1][0] for res in result for item in res]

    return Res(data=texts)
