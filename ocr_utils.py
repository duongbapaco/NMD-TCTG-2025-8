# Tự động dò tìm tesseract
if platform.system() == "Windows":
    # Đường dẫn mặc định Windows (có thể đổi tùy máy bạn)
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
else:
    # Trên Linux/Streamlit Cloud: giả định tesseract đã cài qua apt-get
    if shutil.which("tesseract") is not None:
        pytesseract.pytesseract.tesseract_cmd = shutil.which("tesseract")
    else:
        raise RuntimeError("Tesseract OCR chưa được cài trong hệ thống!")
import pytesseract
import platform
import shutil

import cv2
import pytesseract
import numpy as np
import pandas as pd
from PIL import Image
import tempfile

# Cấu hình pytesseract (nếu cần, chỉnh đường dẫn nếu chạy Windows)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def run_ocr_and_mapping(image_file, excel_file):
    # Lưu ảnh tạm
    tmp = tempfile.NamedTemporaryFile(delete=False)
    tmp.write(image_file.read())
    tmp.close()
    img = cv2.imread(tmp.name)

    # Chuyển sang grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Dùng adaptive threshold để làm rõ text
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                   cv2.THRESH_BINARY, 15, 10)

    # OCR toàn ảnh
    custom_oem_psm_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(thresh, config=custom_oem_psm_config)

    # Tách dòng
    lines = [l.strip() for l in text.splitlines() if l.strip() != ""]

    # Đọc file Excel danh mục công tơ
    df_ref = pd.read_excel(excel_file)

    # Mapping: lọc những dòng có mã công tơ
    results = []
    for line in lines:
        for code in df_ref['TAG NAME']:
            if str(code) in line:
                results.append({
                    "TAG NAME": code,
                    "LINE": line
                })

    df_result = pd.DataFrame(results)
    return df_result