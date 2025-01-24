import streamlit as st
import os
import subprocess

def convert_numbers_to_excel(uploaded_file):
  """Converts .numbers files to .xlsx files using libreoffice."""
  try:
    # Save the uploaded file temporarily
    with open("temp.numbers", "wb") as f:
      f.write(uploaded_file.getbuffer())

    # Use libreoffice to convert the file
    # Ensure libreoffice is installed and in your system's PATH
    command = ["libreoffice", "--headless", "--convert-to", "xlsx", "temp.numbers"]
    subprocess.run(command, check=True, capture_output=True, text=True)

    # Provide download link for the converted file
    with open("temp.xlsx", "rb") as f:
        st.download_button(
            label="Descargar archivo Excel",
            data=f,
            file_name="converted_file.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    # Clean up temporary files
    os.remove("temp.numbers")
    os.remove("temp.xlsx")
    
  except FileNotFoundError:
    st.error("LibreOffice no se encontró. Asegúrate de que esté instalado y en tu PATH.")
  except subprocess.CalledProcessError as e:
    st.error(f"Error al convertir el archivo: {e.stderr}")
  except Exception as e:
    st.error(f"Ocurrió un error: {e}")


st.title("Conversor de archivos .numbers a Excel")

uploaded_file = st.file_uploader("Sube tu archivo .numbers", type=["numbers"])

if uploaded_file is not None:
  if uploaded_file.name.endswith(".numbers"):
    convert_numbers_to_excel(uploaded_file)
  else:
    st.error("Por favor, sube un archivo .numbers.")
