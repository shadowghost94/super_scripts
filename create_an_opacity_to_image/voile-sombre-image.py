from PIL import Image

def add_overlay(image_path, output_path, opacity=0.6):  # Augmente l'opacité ici
    # Ouvrir l'image d'origine
    original = Image.open(image_path).convert("RGBA")

    # Créer une image pour le voile
    overlay = Image.new("RGBA", original.size, (0, 0, 0, int(255 * opacity)))

    # Combiner l'image originale et le voile
    combined = Image.alpha_composite(original, overlay)

    # Sauvegarder le résultat
    combined.save(output_path)

# Utilisation du script
input_image_path = "heading-bg.jpg"  # Remplace par le chemin de ton image
output_image_path = "heading.png"  # Chemin pour enregistrer l'image résultante

add_overlay(input_image_path, output_image_path)
