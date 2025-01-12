import yt_dlp

def download_video(url, save_path="."):
    ydl_opts = {
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Entrez l'URL de la vidéo YouTube : ")
    destination = input("Entrez le dossier de sauvegarde (ou laissez vide pour le répertoire courant) : ")
    if not destination.strip():
        destination = "."
    download_video(video_url, destination)
