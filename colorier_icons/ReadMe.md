#COLORIER UNE ICON PNG
##Ce script Python permet de colorier des image/icon au format PNG. Il modifie les couleurs des pixels en fonction  de vos paramètres ou algorithmes définis, et génère une nouvelle image/icon coloriée.
### Fonctionnalités :
- Applique des couleurs personnalisées à une image/icon PNG.
- Traite rapidement des images tout en préservant leur qualité.
- Facilement adaptable pour différents styles ou palettes de couleurs.
- Permet de conserver des parties transparentes intactes.

## Prérequis
Pour utiliser ce script, vous devez disposer de Python 3.x et des bibliothèques suivantes :
- `Pillow` : pour la manipulation des images.

##Installation
- Si vous n'avez pas python déjà installer veuillez l'installer en utilisant **sudo apt-get install python3**
- Télécharger le script ci dessus (colorier_icons_png.py)
- installer virtualenv en utilisant la commande **sudo apt-get install virtualenv**
- Utiliser l'outil **virtualenv** que vous venez d'installer pour créer un environnement virtuel
- créer un environnement virtuel en utilisant la commande **virtualenv nomEnvironnement**
- accéder au répertoire du nouvel environnement crée en utilisant **cd nomEnvironnement**
- installer la bibliothèque Pillow via la commande **pip install Pillow**
- Une fois tout ces conditions remplies vous pouvez exécuter votre script via **python3 colorier_icons_png.py**

##fonctionnement du script
L'objet images suivant dans le code est utilisé pour spécifier la liste des images à colorier:
**images = {
        "appel": "appel.png",
        "linternet": "linternet.png",
        "email": "email.png",
        "pointeur-de-localisation": "pointeur-de-localisation.png"
    }**
cet objet utilise le format clé valeur. Les valeurs doivent être l'adresse de l'emplacement où se trouve les images par rapport au script colorier_icons_png.py  
(ex. si le fichier colorier_icons_png.py se trouve dans un même répertoire que les images à modifier alors il suffira 
de préciser uniquement les noms des fichiers en valeur de l'objet précédé de la clé voulu)
