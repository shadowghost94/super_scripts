from PIL import Image

def combine_images(image_paths, output_path):
    # Ouvrir les images
    images = [Image.open(img_path) for img_path in image_paths]

    # Trouver la taille maximum pour redimensionner les images
    max_width = max(img.width for img in images)
    max_height = max(img.height for img in images)

    # Créer une nouvelle image avec la taille appropriée
    combined_image = Image.new('RGB', (max_width * 2, max_height * 2))

    # Coller les images dans la nouvelle image
    for index, img in enumerate(images):
        # Redimensionner l'image pour s'adapter à la grille
        img = img.resize((max_width, max_height))
        x = index % 2 * max_width
        y = index // 2 * max_height
        combined_image.paste(img, (x, y))

    # Sauvegarder l'image combinée
    combined_image.save(output_path)

# Exemple d'utilisation
image_paths = [
    '1.png',  # Remplacez par le chemin de votre première image
    '2.webp',  # Remplacez par le chemin de votre deuxième image
    '3.webp',  # Remplacez par le chemin de votre troisième image
    '4.webp'   # Remplacez par le chemin de votre quatrième image
]

output_path = 'combined_image.jpg'  # Chemin de sauvegarde pour l'image combinée
combine_images(image_paths, output_path)
