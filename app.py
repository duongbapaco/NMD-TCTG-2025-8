import streamlit as st
import pandas as pd
from ocr_utils import run_ocr_and_mapping

st.set_page_config(page_title="OCR Công tơ DCS/QCS", layout="wide")

st.title("📊 OCR Công tơ từ ảnh DCS/QCS")

uploaded_image = st.file_uploader("📷 Tải ảnh màn hình DCS/QCS", type=["jpg","jpeg","png"])
uploaded_excel = st.file_uploader("📑 Tải file Excel danh mục công tơ", type=["xlsx"])

if uploaded_image and uploaded_excel:
    with st.spinner("Đang xử lý OCR..."):
        df_result = run_ocr_and_mapping(uploaded_image, uploaded_excel)
    st.success("Hoàn thành OCR!")
    st.dataframe(df_result)

    # Nút tải Excel
    out_path = "ket_qua_ocr.xlsx"
    df_result.to_excel(out_path, index=False)
    with open(out_path, "rb") as f:
        st.download_button("⬇️ Tải kết quả Excel", f, file_name="ket_qua_ocr.xlsx")

else:
    st.info("Vui lòng tải lên cả Ảnh và Excel để bắt đầu.")