import subprocess
import os
import platform
from datetime import datetime

def get_timestamp():
    return datetime.now().strftime('%Y%m%d_%H%M%S')


def convert_docx_to_pdf(docx_path, output_dir):
    # Determine o comando correto do LibreOffice dependendo do sistema operacional
    if platform.system() == 'Windows':
        libreoffice_command = 'soffice'  # Windows uses soffice.exe
    else:
        libreoffice_command = 'libreoffice'  # Linux/Unix uses libreoffice

    # Executar o LibreOffice via linha de comando para converter o DOCX em PDF
    subprocess.run([
        libreoffice_command, '--headless', '--convert-to', 'pdf', docx_path,
        '--outdir', output_dir
    ], check=True)

    # Determinar o caminho do PDF gerado
    output_pdf_path = os.path.join(output_dir, os.path.splitext(os.path.basename(docx_path))[0] + '.pdf')

    print(f"Converting {docx_path} to {output_pdf_path} using {libreoffice_command}")
    os.remove(docx_path)  # Remover o arquivo DOCX original
    return output_pdf_path
