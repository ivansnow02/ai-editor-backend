import paddle
from paddleocr import PaddleOCR

ocrModel = PaddleOCR(use_angle_cls=True, lang="ch")
