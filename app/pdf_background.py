import pymupdf  # PyMuPDF
from PIL import Image
import io


def add_background_to_pdf(pdf_bytes, image_bytes):
    # Carregar o PDF a partir dos bytes
    pdf_document = pymupdf.open(stream=pdf_bytes, filetype="pdf")

    # Abrir a imagem e verificar suas dimensões
    image = Image.open(io.BytesIO(image_bytes))
    image_width, image_height = image.size

    # Iterar pelas páginas do PDF e adicionar a imagem como fundo
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        rect = page.rect  # Dimensões da página
        # Redimensionar a imagem para as dimensões da página
        pil_image_resized = image.resize((int(rect.width), int(rect.height)))
        image_bytes_resized = io.BytesIO()
        pil_image_resized.save(image_bytes_resized, format='PNG')
        image_bytes_resized = image_bytes_resized.getvalue()

        # Adicionar a imagem como fundo da página
        img = pymupdf.Pixmap(image_bytes_resized)
        page.insert_image(rect, pixmap=img)

    # Salvar o PDF modificado em um byte stream
    pdf_output_stream = io.BytesIO()
    pdf_document.save(pdf_output_stream)
    pdf_document.close()

    return pdf_output_stream.getvalue()
