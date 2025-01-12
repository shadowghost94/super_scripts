from pdf2docx import Converter

pdf_file = 'CVYEBOUYO.pdf'
docx_file = 'cv.docx'

# Crée une instance du convertisseur
cv = Converter(pdf_file)

# Effectue la conversion
cv.convert(docx_file, start=0, end=None)  # convertit tout le PDF
cv.close()
