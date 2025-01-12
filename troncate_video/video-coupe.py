from moviepy.video.io.VideoFileClip import VideoFileClip

# Chemin vers la vidéo source
video_path = "teke_batonnum.mp4"  # Remplacez par le chemin de votre vidéo
# Chemin vers la vidéo de sortie
output_path = "teke1.mp4"

# Charger la vidéo
video = VideoFileClip(video_path)

# Définir le début et la fin de la coupe
start_time = 285  # 30 secondes
duration = 18    # 18 secondes
end_time = start_time + duration

# Couper la vidéo
video_coupee = video.subclipped(start_time, end_time)

# Enregistrer la vidéo coupée
video_coupee.write_videofile(output_path, codec="libx264", audio_codec="aac")

# Libérer les ressources
video.close()
video_coupee.close()

print("La vidéo a été coupée avec succès !")
