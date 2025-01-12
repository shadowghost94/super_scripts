from PIL import Image

def recolor_png(image_path, output_path, target_color):
    """
    Recolore une image PNG avec la couleur spécifiée pour tous les pixels non transparents.

    :param image_path: Chemin de l'image PNG source.
    :param output_path: Chemin de sauvegarde de l'image recolorée.
    :param target_color: Couleur cible sous la forme d'un code hexadécimal (ex : "#f5a425").
    """
    # Ouvrir l'image et la convertir en mode RGBA
    img = Image.open(image_path).convert("RGBA")
    data = img.getdata()
    new_data = []

    # Convertir la couleur hexadécimale en RGBA
    target_color_rgba = tuple(int(target_color[i:i+2], 16) for i in (1, 3, 5)) + (255,)

    # Modifier chaque pixel
    for item in data:
        if item[3] > 0:  # Si le pixel n'est pas transparent
            new_data.append(target_color_rgba)
        else:  # Conserver les pixels transparents
            new_data.append(item)

    # Appliquer les modifications à l'image
    img.putdata(new_data)
    img.save(output_path, "PNG")
    print(f"Image recolorée sauvegardée à : {output_path}")

# Exemple d'utilisation
if __name__ == "__main__":
    # Chemins des fichiers
    images = {
        "appel": "appel.png",
        "linternet": "linternet.png",
        "email": "email.png",
        "pointeur-de-localisation": "pointeur-de-localisation.png"
    }
    # Couleur cible
    couleur = "#f5a425"

    # Recolorer chaque image
    for nom, chemin in images.items():
        output = chemin.replace(".png", "_colored.png")
        try:
            recolor_png(chemin, output, couleur)
        except Exception as e:
            print(f"Erreur lors du traitement de {nom} : {e}")
