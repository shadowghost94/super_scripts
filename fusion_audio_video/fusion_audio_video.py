import subprocess
import os

def merge_video_audio(video_file, audio_file, output_file):
    """
    Fusionne un fichier vidéo MP4 et un fichier audio AAC en un fichier MP4 unique.

    :param video_file: Chemin du fichier vidéo MP4.
    :param audio_file: Chemin du fichier audio AAC.
    :param output_file: Chemin du fichier de sortie MP4.
    """
    # Vérification de l'existence des fichiers
    if not os.path.exists(video_file):
        print(f"Le fichier vidéo {video_file} n'existe pas.")
        return

    if not os.path.exists(audio_file):
        print(f"Le fichier audio {audio_file} n'existe pas.")
        return

    # Commande FFmpeg pour fusionner la vidéo et l'audio
    command = [
        "ffmpeg",
        "-i", video_file,
        "-i", audio_file,
        "-c:v", "copy",  # Copier la vidéo sans ré-encodage
        "-c:a", "aac",  # S'assurer que l'audio est en AAC
        "-strict", "experimental",  # Permet d'utiliser certains codecs expérimentaux
        output_file
    ]

    try:
        print("Fusion en cours...")
        subprocess.run(command, check=True)
        print(f"Fusion terminée. Fichier de sortie : {output_file}")
    except subprocess.CalledProcessError as e:
        print("Une erreur est survenue lors de la fusion.")
        print(e)

if __name__ == "__main__":
    # Remplacez ces chemins par ceux de vos fichiers
    video_file_path = "Evergreen _ Two Steps From Hell Live _ The Bands of HM Royal Marines.mp4"
    audio_file_path = "audio.audio aac"
    output_file_path = "output.mp4"

    merge_video_audio(video_file_path, audio_file_path, output_file_path)
