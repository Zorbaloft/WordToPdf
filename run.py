# Author: Zorbaloft (Miguel Gaspar)
# Created on: 2024-10-21
# Description: This script handles the conversion of DOCX files to PDF and the signing of PDF files.
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
