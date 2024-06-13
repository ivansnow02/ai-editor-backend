from paddleocr import PaddleOCR


def init_ocr() -> PaddleOCR:
    return PaddleOCR(use_angle_cls=True, lang="ch")
