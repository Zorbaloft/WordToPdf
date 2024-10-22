# routes.py
# Author: Zorbaloft (Miguel Gaspar)
# Created on: 2024-10-21
# Description: This script handles the conversion of DOCX files to PDF and the signing of PDF files.
from flask import Flask, request, send_file, jsonify
import os
from .pdf_converter import convert_file_to_Pdf
from .pdf_signer import sign_PDF_file
from .pdf_validate import validate_pdf_signatures
from .pdf_background import add_background_to_pdf
from datetime import datetime
import io
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

    @app.route('/api/v1/validate', methods=['POST'])
    def validate_pdf():
        try:
            # Obter o arquivo PDF enviado pelo usuário
            file = request.files['file']
            file_path = os.path.join(PROJECT_TEMP_DIR, file.filename)

            # Salvar o arquivo temporariamente
            file.save(file_path)

            # Validar as assinaturas
            result, status_code = validate_pdf_signatures(file_path)

            # Deletar o arquivo temporário após a validação
            os.remove(file_path)

            return jsonify(result), status_code

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/api/v1/add-background', methods=['POST'])
    def add_background():
        try:
            # Verificar se o arquivo foi enviado
            if 'file' not in request.files or 'image' not in request.files:
                return jsonify({'error': 'PDF or image file missing'}), 400

            # Pegar o PDF e a imagem dos arquivos enviados
            pdf_file = request.files['file']
            image_file = request.files['image']

            if not pdf_file.filename.endswith('.pdf'):
                return jsonify({'error': 'Invalid file type, only PDF is allowed'}), 400

            # Converter o PDF e imagem em bytes
            pdf_bytes = pdf_file.read()
            image_bytes = image_file.read()

            # Chamar a função que adiciona o fundo ao PDF
            modified_pdf_bytes = add_background_to_pdf(pdf_bytes, image_bytes)

            # Enviar o PDF modificado de volta ao cliente
            return send_file(io.BytesIO(modified_pdf_bytes),
                             download_name='pdf_with_background.pdf',
                             as_attachment=True,
                             mimetype='application/pdf')

        except Exception as e:
            return jsonify({'error': str(e)}), 500


# Call the setup_routes function to register the routes
setup_routes(app)
