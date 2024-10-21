import os
from weakref import finalize

from pypdf import PdfReader, PdfWriter
from pyhanko.sign import signers
from pyhanko.pdf_utils.incremental_writer import IncrementalPdfFileWriter
from datetime import datetime
def get_timestamp():
    return datetime.now().strftime('%Y%m%d_%H%M%S')

def sign_PDF_file(file):
    timestamp = get_timestamp()
    PDF_Output_Path = os.path.join(os.path.dirname(file), f"{timestamp}_Assinado.pdf")

    # 1. Adicionar metadados ao PDF
    reader = PdfReader(file)
    writer = PdfWriter()

    # Copiar páginas do PDF original para o novo PDF
    for page in reader.pages:
        writer.add_page(page)

        # Adicionando os metadados

        writer.add_metadata({
            '/Title': "Meu Título",
            '/Subject': "Meu Assunto",
            '/Keywords': "MeuToken"  # Usando Keywords para armazenar o token
        })

    # Escreve o novo PDF com os metadados adicionadosfile
    with open(PDF_Output_Path, 'wb') as out_file:
        writer.write(out_file)

    # 2. Assinar o PDF
    cms_signer = signers.SimpleSigner.load(
        'C:/Users/aedl/Desktop/pythonPDFsign/certificados/chave_privada.pem',
        'C:/Users/aedl/Desktop/pythonPDFsign/certificados/cert_91452.crt',
        ca_chain_files=(),
        key_passphrase=None
    )

    with open(PDF_Output_Path, 'rb') as doc:
        w = IncrementalPdfFileWriter(doc)
        sig_metadata = signers.PdfSignatureMetadata(
            field_name='AssinaturaAEDL',
            location='Matosinhos',
            reason='Test Reason',

        )
        out = signers.PdfSigner(
            sig_metadata,
            signer=cms_signer,
        ).sign_pdf(w)

        # Clean up temporary files

        with open(PDF_Output_Path, 'wb') as out_file:
            out_file.write(out.getbuffer())


        os.remove(file)  # Remove the generated PDF


    return PDF_Output_Path
