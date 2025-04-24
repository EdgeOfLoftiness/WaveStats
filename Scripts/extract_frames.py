import cv2
import os

video_path = input("Ruta del video: ").strip()
output_folder = "D:\Code\WaveStats\Datasets\Extracted_frames".strip()
fps_interval = int(input("Imagenes por segundo: ").strip())

def extract_frames(video_path, output_folder, fps_interval=2):
    os.makedirs(output_folder, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"No se pudo abrir el video: {video_path}")
        return

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_interval = max(1, fps // fps_interval)
    frame_count = 0
    saved_count = 0

    video_name = os.path.splitext(os.path.basename(video_path))[0]

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_interval == 0:
            filename = os.path.join(output_folder, f"{video_name}_frame{frame_count:05d}.jpg")
            cv2.imwrite(filename, frame)
            saved_count += 1

        frame_count += 1

    cap.release()
    print(f"Total de imágenes guardadas: {saved_count}")

extract_frames(video_path, output_folder, fps_interval)
