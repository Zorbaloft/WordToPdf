# routes.py
# Author: Zorbaloft (Miguel Gaspar)
# Created on: 2024-10-21
# Description: This script handles the conversion of DOCX files to PDF and the signing of PDF files.
from flask import Flask, request, send_file
import os
from .pdf_converter import convert_file_to_Pdf
from .pdf_signer import sign_PDF_file
from datetime import datetime
import pythoncom
app = Flask(__name__)

# Definir caminhos
PROJECT_TEMP_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'temp')

# Certificar que a pasta temp existe
if not os.path.exists(PROJECT_TEMP_DIR):
    os.makedirs(PROJECT_TEMP_DIR)

def get_timestamp():
    return datetime.now().strftime('%Y%m%d_%H%M%S')



# Rota para converter DOCX para PDF e assinar
def setup_routes(app):
    @app.route('/api/v1/convertAndSign', methods=['POST'])
    def convert_and_sign():
        # Inicializar pythoncom
        pythoncom.CoInitialize()
        try:
            file = request.files['file']
            timestamp = get_timestamp()

            # Converter arquivo para PDF
            result_Pdf = convert_file_to_Pdf(file)

            if isinstance(result_Pdf, tuple):
                return result_Pdf  # Error message and status code

            # Assinar PDF
            result_Pdf_sign = sign_PDF_file(result_Pdf)

            if isinstance(result_Pdf_sign, tuple):
                return result_Pdf_sign  # Error message and status code

            # Enviar o PDF assinado
            return send_file(result_Pdf_sign, as_attachment=True, download_name=f"{timestamp}_Signed.pdf")

        finally:
            # Garantir que o CoUninitialize seja chamado
            pythoncom.CoUninitialize()

    @app.route('/api/v1/convert', methods=['POST'])
    def convert():
        # Inicializar pythoncom
        pythoncom.CoInitialize()
        try:
            file = request.files['file']
            timestamp = get_timestamp()

            # Converter arquivo para PDF
            result_Pdf = convert_file_to_Pdf(file)

            if isinstance(result_Pdf, tuple):
                return result_Pdf  # Error message and status code


            # Enviar o PDF assinado
            return send_file(result_Pdf, as_attachment=True, download_name=f"{timestamp}_Convertido.pdf")

        finally:
            # Garantir que o CoUninitialize seja chamado
            pythoncom.CoUninitialize()

    @app.route('/api/v1/sign', methods=['POST'])
    def sign():
        # Inicializar pythoncom
        pythoncom.CoInitialize()
        try:
            file = request.files['file']
            timestamp = get_timestamp()

            # Converter arquivo para PDF

            # Assinar PDF
            result_Pdf_sign = sign_PDF_file(file)

            if isinstance(result_Pdf_sign, tuple):
                return result_Pdf_sign  # Error message and status code

            # Enviar o PDF assinado
            return send_file(result_Pdf_sign, as_attachment=True, download_name=f"{timestamp}_Signed.pdf")

        finally:
            # Garantir que o CoUninitialize seja chamado
            pythoncom.CoUninitialize()

# Call the setup_routes function to register the routes
setup_routes(app)