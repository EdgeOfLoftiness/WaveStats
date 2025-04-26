from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="D:/Code/WaveStats/Datasets/data.yaml",
    epochs=150,
    imgsz=1280,
    batch=16,
    name="yolo_numeros_v1",
    device="0",
    patience=20,
    save_period=10,
    cache=True,
    val=True,
    exist_ok=True,
)
