# ce script vous aidera a transformer un pdf de plusieurs pdf en un pdf de une seule page

import fitz  # PyMuPDF

# Charger le PDF
pdf_path = "DEVOIR DU 3ÈME TRIMESTRE MATHEMATIQUES 6ÈME 2021-2022 COLLEGE CATHOLIQUE PERE AUPIAIS.pdf"
doc = fitz.open(pdf_path)

# Vérifier qu'il y a au moins deux pages
if len(doc) < 2:
    print("Le PDF doit contenir au moins deux pages.")
    exit()

# Récupérer les dimensions des pages
page1 = doc[0]
page2 = doc[1]
width = page1.rect.width
height = page1.rect.height + page2.rect.height  # Hauteur totale = somme des deux

# Créer un nouveau document et une page avec la bonne taille
new_doc = fitz.open()
new_page = new_doc.new_page(width=width, height=height)

# Coller les deux pages sur la nouvelle page
new_page.show_pdf_page(fitz.Rect(0, 0, width, page1.rect.height), doc, 0)  # Première page
new_page.show_pdf_page(fitz.Rect(0, page1.rect.height, width, height), doc, 1)  # Deuxième page en dessous

# Sauvegarder le nouveau PDF fusionné
output_path = "DEVOIR_DU_3ÈME_TRIMESTRE_MATHEMATIQUES_6ÈME_2021-2022_COLLEGE_CATHOLIQUE_PERE_AUPIAIS.pdf"
new_doc.save(output_path)
new_doc.close()

print(f"PDF fusionné enregistré sous : {output_path}")
