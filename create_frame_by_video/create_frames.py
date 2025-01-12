import cv2
import numpy as np
from pyzbar.pyzbar import decode
import glob
import os

def extract_frames(video_path, output_folder):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imwrite(f"{output_folder}/frame_{frame_count:04d}.png", frame)
        frame_count += 1
    cap.release()
    cv2.destroyAllWindows()
    
extract_frames("Remise de prix aux lauréats du HackerLab 2024.mp4", "frames")
