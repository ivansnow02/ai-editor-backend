import hashlib
import io
import os

from PIL import Image
from fastapi import APIRouter, Depends, File, Path, UploadFile
from sqlmodel import Session

from app import crud
from app.dependencies import get_current_user, get_db
from app.models import ImageModel, UserPublic
from app.utils.ocr import init_ocr
from app.utils.result import Res

router = APIRouter(
    prefix="/api/img",
    tags=["img"],
    responses={404: {"description": "Not found"}},
)

ocrModel = init_ocr()


@router.post(path="/upload")
async def upload_img(
    session: Session = Depends(dependency=get_db),
    file: UploadFile = File(...),
    user: UserPublic = Depends(get_current_user),
):
    # 保存图片
    img = Image.open(io.BytesIO(await file.read()))
    dir_path = "static/"
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    if file.filename is None:
        return Res(code=400, msg="file name is None")
    img_path = dir_path + f"{hashlib.md5(file.filename.encode()).hexdigest()}.png"
    img.save(img_path)

    image = crud.create_img(
        session=session, img=ImageModel(path=img_path, user_id=user.id)
    )

    return Res(data=image.model_dump())


@router.get(path="/{img_id}")
async def get_img(
    session: Session = Depends(dependency=get_db),
    img_id: int = Path(
        ..., title="图片id", description="图片id", example=1, alias="img_id"
    ),
    user: UserPublic = Depends(get_current_user),
):
    image = crud.get_img(session=session, pk=img_id)
    if image is None:
        return Res(code=400, msg="img is None")
    if image.user_id != user.id:
        return Res(code=400, msg="img is not belong to you")
    return Res(data=image.model_dump())


@router.get(path="/ocr/{img_id}")
async def ocr_img(
    img_id: int = Path(
        ..., title="图片id", description="图片id", example=1, alias="img_id"
    ),
    session: Session = Depends(dependency=get_db),
    user: UserPublic = Depends(get_current_user),
):
    img = crud.get_img(session=session, pk=img_id)
    if img is None:
        return Res(code=400, msg="img is None")
    if img.user_id != user.id:
        return Res(code=400, msg="img is not belong to you")
    img_path = img.path
    if img_path is None:
        return Res(code=400, msg="img_path is None")
    # file_name = img_path.split("/")[-1]
    # fpath = './../static/' + file_name
    print(img_path)
    result = ocrModel.ocr(img=img_path, cls=True)
    texts = [item[1][0] for res in result for item in res]

    return Res(data=texts)
