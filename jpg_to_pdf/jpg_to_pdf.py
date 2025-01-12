from PIL import Image
import os

def convert_jpg_to_pdf(jpg_path, pdf_path):
    try:
        # Ouvrir l'image
        image = Image.open(jpg_path)

        # Vérifier si l'image est en mode RGB (nécessaire pour le PDF)
        if image.mode != 'RGB':
            image = image.convert('RGB')

        # Sauvegarder en PDF
        image.save(pdf_path, "PDF", resolution=100.0)
        print(f"L'image {jpg_path} a été convertie avec succès en {pdf_path}.")
    except Exception as e:
        print(f"Erreur lors de la conversion : {e}")

# Exemple d'utilisation
if __name__ == "__main__":
    # Spécifier le chemin de l'image JPG
    jpg_path = "IMG_1792-min.jpg"

    # Chemin de sauvegarde du fichier PDF
    pdf_path = os.path.splitext(jpg_path)[0] + ".pdf"

    # Appeler la fonction
    convert_jpg_to_pdf(jpg_path, pdf_path)
