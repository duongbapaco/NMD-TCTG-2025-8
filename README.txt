# OCR Công tơ từ ảnh DCS/QCS (Streamlit App)

## Cài đặt
1. Cài Python 3.9+
2. Cài các thư viện:
   ```bash
   pip install -r requirements.txt
   ```
3. Cài đặt Tesseract OCR:
   - Windows: tải tại https://github.com/UB-Mannheim/tesseract/wiki
   - Ubuntu: sudo apt-get install tesseract-ocr

## Chạy ứng dụng
```bash
streamlit run app.py
```

Ứng dụng chạy tại http://localhost:8501

## Tính năng
- Upload ảnh màn hình DCS/QCS
- Upload file Excel danh mục công tơ
- OCR nhận dạng mã công tơ từ ảnh
- Mapping với file Excel
- Hiển thị kết quả + tải Excel
