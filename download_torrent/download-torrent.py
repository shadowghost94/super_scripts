from deluge_client import DelugeRPCClient
import time

def download_torrent_with_deluge(magnet_link, host="127.0.0.1", port=58846, username="user", password="password"):
    try:
        # Connexion au client Deluge
        client = DelugeRPCClient(host, port, username, password)
        client.connect()
        print("Connexion réussie au client Deluge.")

        # Ajouter le torrent
        torrent_id = client.call("core.add_torrent_magnet", magnet_link, {})
        print(f"Lien magnet ajouté. ID du torrent : {torrent_id}")

        # Suivi de la progression
        print("Suivi du téléchargement...")
        while True:
            status = client.call("core.get_torrent_status", torrent_id, ["progress", "download_payload_rate", "num_peers"])
            progress = status["progress"]
            download_rate = status["download_payload_rate"]
            num_peers = status["num_peers"]

            print(f"""
            Progression : {progress:.2f}%
            Vitesse de téléchargement : {download_rate / 1000:.2f} kB/s
            Nombre de pairs connectés : {num_peers}
            """)

            if progress >= 100:
                print("Téléchargement terminé !")
                break

            time.sleep(1)

    except Exception as e:
        print(f"Erreur : {e}")

# Lien magnet
magnet = "magnet:?xt=urn:btih:6cfd745520d9e8d79448014dd4597621ff7182c4&tr=udp://tracker.opentrackr.org:1337/announce&tr=udp://open.stealth.si:80/announce&tr=udp://explodie.org:6969/announce&tr=udp://exodus.desync.com:6969/announce&tr=udp://tracker.internetwarriors.net:1337/announce&tr=udp://ipv4.tracker.harry.lu:80/announce&tr=udp://tracker.tiny-vps.com:6969/announce&tr=udp://9.rarbg.to:2740/announce&tr=udp://9.rarbg.com:2770/announce&tr=http://1337.abcvg.info/announce&tr=http://open.acgnxtracker.com/announce&tr=udp://tracker.torrent.eu.org:451/announce&tr=udp://zephir.monocul.us:6969/announce&tr=http://tracker.bt4g.com:2095/announce&tr=udp://opentor.org:2710/announce"

download_torrent_with_deluge(magnet, username="votre_nom_utilisateur", password="votre_mot_de_passe")
