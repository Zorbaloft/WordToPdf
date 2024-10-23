# PDF Conversion and Signing API

## Description

This API allows converting DOCX files to PDF and signing PDF files. The API is built using Flask and offers several endpoints:

1. `/api/v1/convertAndSign`: Converts a DOCX file to PDF and then signs the PDF.
2. `/api/v1/convert`: Converts a DOCX file to PDF.
3. `/api/v1/sign`: Signs an existing PDF file.
4. `/api/v1/validate`: Validates the signatures in a PDF file.
5. `/api/v1/add-background`: Adds a background image to a PDF file.

## Endpoints

### 1. `/api/v1/convertAndSign`

**Description:** Converts a DOCX file to PDF and signs the resulting PDF.

**Method:** POST

**Parameters:**

- `file`: DOCX file to be converted and signed.

**Response:**

- Signed PDF as a downloadable file.

### 2. `/api/v1/convert`

**Description:** Converts a DOCX file to PDF.

**Method:** POST

**Parameters:**

- `file`: DOCX file to be converted.

**Response:**

- Converted PDF as a downloadable file.

### 3. `/api/v1/sign`

**Description:** Signs an existing PDF file.

**Method:** POST

**Parameters:**

- `file`: PDF file to be signed.

**Response:**

- Signed PDF as a downloadable file.

### 4. `/api/v1/validate`

**Description:** Validates the signatures in a PDF file.

**Method:** POST

**Parameters:**

- `file`: PDF file to be validated.

**Response:**

- JSON response with validation results.

### 5. `/api/v1/add-background`

**Description:** Adds a background image to a PDF file.

**Method:** POST

**Parameters:**

- `file`: PDF file to which the background will be added.
- `image`: Image file to be used as the background.

**Response:**

- PDF with the background added as a downloadable file.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Zorbaloft/pythonPDFsign.git
    cd pythonPDFsign
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies (talvez tenha que resolver alguns problemas de dependencias(verificar a compatiblidade)):
    ```sh
    pip install -r requirements.txt
    ```

4. Run the application:
    ```sh
    flask run
    ```
   

Eng-eng:
Notes: The use of this API is not recommended for production use without first being reviewed and tested by an information security professional.
The background will add a layer over the content, so it is advisable to use it in documents that do not contain information. Alternatively, use an image with a transparent background.
Pt-pt:
Notas: O uso desta API nao e aconselhavel para uso de producao sem antes ser revista e testada por um profissional de seguranca da informacao.
O background vai adicionar uma camada por cima do conteudo o que e aconselhavel utilizar em documentos que nao tenham informacao.Ou utilizar uma imagem com um background transparente. 
Autor
Zorbaloft (Miguel Gaspar)

## Project Structure

```plaintext
pythonPDFsign/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── pdf_converter.py
│   ├── pdf_signer.py
│   └── pdf_background.py
├── venv/
├── requirements.txt
└── README.md
