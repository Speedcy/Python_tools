# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 08:07:31 2024

@author: cnco
"""

import subprocess
import json
import os
import ffmpeg

##############################################################################
#                                GET INFO ON VIDEO                           #
##############################################################################

# Spécifiez le chemin complet vers ffmpeg
ffprobe_path = r"C:\Users\cnco\Downloads\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\ffprobe.exe"

# Vérifiez que ffprobe.exe existe
if not os.path.exists(ffprobe_path):
    raise FileNotFoundError(f"ffprobe.exe introuvable : {ffprobe_path}")

# Fichier vidéo à analyser
input_file = "House of Dragons Ep1.mkv"

# Vérifiez que le fichier d'entrée existe
if not os.path.exists(input_file):
    raise FileNotFoundError(f"Le fichier spécifié est introuvable : {input_file}")

try:
    # Commande pour exécuter ffprobe
    result = subprocess.run(
        [ffprobe_path, "-v", "error", "-show_streams", "-print_format", "json", input_file],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    # Vérifiez s'il y a des erreurs
    if result.returncode != 0:
        raise RuntimeError(f"Erreur lors de l'exécution de ffprobe : {result.stderr}")

    # Parsez la sortie JSON
    probe_data = json.loads(result.stdout)

    # Extraire les informations de bitrate
    for stream in probe_data['streams']:
        if 'bit_rate' in stream:
            print(f"Stream {stream['index']} - Codec: {stream['codec_name']} - Bitrate: {int(stream['bit_rate']) / 1000} kbps")

except Exception as e:
    print(f"Une erreur est survenue : {e}")
    
##############################################################################
#                                GET INFO ON VIDEO                           #
##############################################################################

# Chemin explicite vers l'exécutable ffmpeg
ffmpeg_path = r"C:\Users\cnco\Downloads\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe"  # Remplacez par le chemin correct

# Input and output file paths
input_file = "House of Dragons Ep1.mkv"
output_file = "House of Dragons Ep1_compressed.mkv"

# Vérifiez que le fichier d'entrée existe
if not os.path.exists(input_file):
    raise FileNotFoundError(f"Le fichier spécifié est introuvable : {input_file}")


# Parameters for cutting and compressing
start_time = "00:00:05"  # Start time (HH:MM:SS)
duration = "01:04:30"    # Duration (HH:MM:SS)
video_bitrate = "1000k"  # Video bitrate for compression
audio_bitrate = "128k"   # Audio bitrate for compression

try:
    # Utilisation de ffmpeg avec découpage et compression
    (
        ffmpeg
        .input(input_file, ss=start_time, t=duration)  # Découpe la vidéo
        .output(output_file, vcodec='libx264', acodec='aac', video_bitrate=video_bitrate, audio_bitrate=audio_bitrate)
        .run(cmd=ffmpeg_path, overwrite_output=True)  # Spécifie le chemin
    )
    print(f"Fichier de sortie enregistré sous : {output_file}")
except ffmpeg.Error as e:
    print("Une erreur est survenue :", e.stderr.decode())


