# converter.py
import os
from docx2pdf import convert
from datetime import datetime

# Definir caminhos do projeto
PROJECT_TEMP_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'temp')

# Certificar que a pasta temp existe
if not os.path.exists(PROJECT_TEMP_DIR):
    os.makedirs(PROJECT_TEMP_DIR)


def get_timestamp():
    return datetime.now().strftime('%Y%m%d_%H%M%S')


def convert_file_to_Pdf(file):
    try:
        if not file.filename.endswith('.docx'):
            return "Invalid file format", 400

        timestamp = get_timestamp()

        # Save the DOCX file in the project's temp folder
        file_path = os.path.join(PROJECT_TEMP_DIR, file.filename)
        file.save(file_path)

        # Define the output path for the PDF
        output_pdf_path = os.path.join(PROJECT_TEMP_DIR, f"{timestamp}_output.pdf")

        # Convert the DOCX to PDF
        convert(file_path, output_pdf_path)

        # Check if the PDF was created
        if not os.path.exists(output_pdf_path):
            return "Error converting DOCX to PDF", 500

        # Clean up temporary files
        os.remove(file_path)  # Remove the DOCX
        # os.remove(output_pdf_path)  # Remove the generated PDF

        return output_pdf_path
    except Exception as e:
        return str(e), 500
