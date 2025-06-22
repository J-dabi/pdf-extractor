import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from utils.parser import extract_info
from utils.generate_excel import generate_excel  # ⬅ Word → Excel로 변경
import tempfile

# 페이지 설정
st.set_page_config(page_title="PDF → 자사 양식 변환기", layout="centered")

st.header("📄 데이터시트 → 자사 양식 자동 변환기")

uploaded = st.file_uploader("PDF 파일을 업로드하세요", type="pdf")

if uploaded:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded.read())
        text = extract_text_from_pdf(tmp.name)
        info = extract_info(text)

        st.subheader("🔍 추출된 정보")
        for k, v in info.items():
            st.markdown(f"- **{k}**: {v}")

        if st.button("📥 Excel 파일로 저장"):
            output_path = "result.xlsx"
            generate_excel(info, output_path)
            with open(output_path, "rb") as f:
                st.download_button("📎 다운로드", f, file_name="result.xlsx")