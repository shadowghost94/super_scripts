from PIL import Image
import os

def resize_images(image_paths, output_size=(370, 215)):
    for img_path in image_paths:
        # Ouvrir l'image
        with Image.open(img_path) as img:
            # Redimensionner l'image
            img_resized = img.resize(output_size)
            # Créer un nom de fichier de sortie
            base_name = os.path.basename(img_path)
            output_path = f'resized_{base_name}'
            # Sauvegarder l'image redimensionnée
            img_resized.save(output_path)
            print(f'Saved resized image as {output_path}')

# Exemple d'utilisation
image_paths = [
    'flag_benin.png',  # Remplacez par le chemin de votre première image
    'chants_danses.jpg',  # Remplacez par le chemin de votre deuxième image
    'ethnies.jpg',  # Remplacez par le chemin de votre troisième image
    'langues.webp',  # Remplacez par le chemin de votre quatrième image
    'gastronomie.jpg',  # Remplacez par le chemin de votre cinquième image
    'divinites.jpeg',  # Remplacez par le chemin de votre sixième image
    'royaume.png',  # Remplacez par le chemin de votre septième image
    'patrimoine.png',  # Remplacez par le chemin de votre huitième image
    'benin.jpeg'   # Remplacez par le chemin de votre neuvième image
]

resize_images(image_paths)
