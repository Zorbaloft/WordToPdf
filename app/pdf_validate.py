from pyhanko.keys import load_cert_from_pemder
from pyhanko_certvalidator import ValidationContext
from pyhanko.pdf_utils.reader import PdfFileReader
from pyhanko.sign.validation import validate_pdf_signature

# Caminho do certificado
CERT_PATH = 'C:/Users/aedl/Desktop/pythonPDFsign/certificados/cert_91452.crt'


def validate_pdf_signatures(file_path):
    try:
        # Carregar o certificado raiz de confiança a partir da pasta certificados
        root_cert = load_cert_from_pemder(CERT_PATH)

        # Criar o contexto de validação
        vc = ValidationContext(trust_roots=[root_cert])

        # Abrir o arquivo PDF
        with open(file_path, 'rb') as doc:
            reader = PdfFileReader(doc)

            # Verificar se o PDF contém assinaturas
            if not reader.embedded_signatures:
                return {'error': 'O PDF não contém assinaturas'}, 400

            # Lista para armazenar informações das assinaturas
            signatures_info = []

            # Validar cada assinatura
            for sig in reader.embedded_signatures:
                status = validate_pdf_signature(sig, vc)

                # Verificar se a assinatura é válida
                if not status.docmdp_ok or not status.valid:
                    return {'error': 'Assinatura inválida'}, 400

                # Adicionar detalhes da assinatura
                sig_info = {
                    'certificado': sig.signer_cert.subject.human_friendly,
                    'serialNumber': sig.signer_cert.serial_number,
                    'assinante': sig.signer_cert.issuer.human_friendly,
                    # 'dataAssinatura': sig.signing_time.isoformat(),
                    'dataValidade': sig.signer_cert.not_valid_after.isoformat()
                }
                signatures_info.append(sig_info)
                # print(dir(sig.signer_cert)) (returns all the methods and attributes of the object)

            return signatures_info, 200

    except Exception as e:
        return {'error': str(e)}, 500
