# PDF Conversion and Signing API

## Descrição

Esta API permite converter arquivos DOCX para PDF e assinar arquivos PDF. A API é construída usando Flask e oferece três endpoints principais:

1. `/api/v1/convertAndSign`: Converte um arquivo DOCX para PDF e, em seguida, assina o PDF.
2. `/api/v1/convert`: Converte um arquivo DOCX para PDF.
3. `/api/v1/sign`: Assina um arquivo PDF existente.

## Endpoints

### 1. `/api/v1/convertAndSign`

**Descrição:** Converte um arquivo DOCX para PDF e assina o PDF resultante.

**Método:** POST

**Parâmetros:**

- `file`: Arquivo DOCX a ser convertido e assinado.

**Resposta:**

- PDF assinado como um arquivo para download.

### 2. `/api/v1/convert`

**Descrição:** Converte um arquivo DOCX para PDF.

**Método:** POST

**Parâmetros:**

- `file`: Arquivo DOCX a ser convertido.

**Resposta:**

- PDF convertido como um arquivo para download.

### 3. `/api/v1/sign`

**Descrição:** Assina um arquivo PDF existente.

**Método:** POST

**Parâmetros:**

- `file`: Arquivo PDF a ser assinado.

**Resposta:**

- PDF assinado como um arquivo para download.

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/Zorbaloft/pythonPDFsign.git
    cd pythonPDFsign
    ```

2. Crie e ative um ambiente virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Execute a aplicação:
    ```sh
    flask run
    ```

## Estrutura do Projeto

```plaintext
pythonPDFsign/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── pdf_converter.py
│   └── pdf_signer.py
├── venv/
├── requirements.txt
└── README.md
Autor
Zorbaloft (Miguel Gaspar)