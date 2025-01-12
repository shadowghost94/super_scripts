import PyPDF2

def split_pdf(input_pdf_path, output_pdf1_path, output_pdf2_path):
    # Ouvrir le fichier PDF en lecture binaire
    with open(input_pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Vérifier si le PDF contient au moins deux pages
        if len(pdf_reader.pages) < 2:
            print("Le PDF doit contenir au moins deux pages.")
            return

        # Créer deux fichiers PDF de sortie
        pdf_writer1 = PyPDF2.PdfWriter()
        pdf_writer2 = PyPDF2.PdfWriter()

        # Ajouter la première page au premier fichier
        pdf_writer1.add_page(pdf_reader.pages[0])
        with open(output_pdf1_path, "wb") as output_pdf1:
            pdf_writer1.write(output_pdf1)

        # Ajouter la seconde page au second fichier
        pdf_writer2.add_page(pdf_reader.pages[1])
        with open(output_pdf2_path, "wb") as output_pdf2:
            pdf_writer2.write(output_pdf2)

        print("Les pages ont été séparées avec succès.")

# Utilisation de la fonction
split_pdf("EXTRAIT_D'ACTE_DE_NAISSANCE.pdf", "maman.pdf", "papa.pdf")
