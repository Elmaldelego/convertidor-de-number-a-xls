import streamlit as st
from PIL import Image
from io import BytesIO
from fpdf import FPDF

st.set_page_config(page_title="JPG a PDF", layout="centered")

st.title("🖼️ Convertidor de JPG a PDF")

uploaded_files = st.file_uploader(
    "Sube una o varias imágenes JPG", type=["jpg", "jpeg"], accept_multiple_files=True
)

if uploaded_files:
    images = []
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file).convert("RGB")
        images.append(image)

    if st.button("Convertir a PDF"):
        pdf_bytes = BytesIO()
        images[0].save(pdf_bytes, format="PDF", save_all=True, append_images=images[1:])
        pdf_bytes.seek(0)

        st.success("✅ Conversión exitosa.")
        st.download_button(
            label="📥 Descargar PDF",
            data=pdf_bytes,
            file_name="imagenes_convertidas.pdf",
            mime="application/pdf"
        )
