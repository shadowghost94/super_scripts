from PyPDF2 import PdfReader, PdfWriter
import os

def compress_pdf(input_pdf, output_pdf, target_size_kb=500):
    try:
        # Lire le fichier PDF source
        reader = PdfReader(input_pdf)
        writer = PdfWriter()

        # Ajouter toutes les pages au nouveau PDF
        for page in reader.pages:
            writer.add_page(page)

        # Sauvegarder le nouveau fichier PDF (les métadonnées sont omises pour gagner de l'espace)
        with open(output_pdf, "wb") as out_file:
            writer.write(out_file)

        # Vérifier la taille finale
        file_size_kb = os.path.getsize(output_pdf) / 1024
        if file_size_kb > target_size_kb:
            print(f"Le fichier compressé est encore supérieur à {target_size_kb} Ko ({file_size_kb:.2f} Ko).")
        else:
            print(f"Compression réussie ! Taille finale : {file_size_kb:.2f} Ko")

    except Exception as e:
        print(f"Erreur lors de la compression : {e}")

# Exemple d'utilisation
if __name__ == "__main__":
    input_pdf = "IMG_1792-min.pdf"
    output_pdf = "IMG-1792-compressé.pdf"
    compress_pdf(input_pdf, output_pdf)
