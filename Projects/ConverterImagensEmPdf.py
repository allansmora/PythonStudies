import os
import img2pdf

# Diretório onde estão as imagens
directory_path = "C:\\Users\\Allan\\Documents\\GitHub\\PythonStudies\\Projects"

# Busca apenas os arquivos do tipo JPEG
image_files = [i for i in os.listdir(directory_path) if i.endswith(".jpg")]

# Converte as imagens em PDF
pdf_data = img2pdf.convert(image_files)

# Coloca o conteúdo no pdf
with open("output.pdf", "wb") as file:
    file.write(pdf_data)