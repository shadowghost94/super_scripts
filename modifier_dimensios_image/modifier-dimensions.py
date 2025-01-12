from PIL import Image

def redimensionner_image(chemin_image, nouvelle_largeur, nouvelle_hauteur, chemin_sortie):
    # Ouvrir l'image
    image = Image.open(chemin_image)

    # Redimensionner l'image
    image_redimensionnee = image.resize((nouvelle_largeur, nouvelle_hauteur))

    # Sauvegarder l'image redimensionnée
    image_redimensionnee.save(chemin_sortie)

    print(f"L'image a été redimensionnée et sauvegardée sous {chemin_sortie}.")

# Exemple d'utilisation :
chemin_image = "prime.webp"
nouvelle_largeur = 1600  # Remplacer par la largeur souhaitée
nouvelle_hauteur = 428  # Remplacer par la hauteur souhaitée
chemin_sortie = "heading-bg.jpg"

redimensionner_image(chemin_image, nouvelle_largeur, nouvelle_hauteur, chemin_sortie)
