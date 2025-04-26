from ultralytics import YOLO

model = YOLO("runs/detect/yolo_numeros_v13/weights/best.pt")
results = model("D:\Code\WaveStats\Datasets\Extracted_frames", save=True,save_txt=True)
