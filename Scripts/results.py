import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:/Code/WaveStats/runs/detect/yolo_numeros_v13/results.csv")

plt.plot(df["epoch"], df["metrics/mAP50(B)"], label="mAP@0.5")
plt.plot(df["epoch"], df["metrics/precision(B)"], label="Precision")
plt.plot(df["epoch"], df["metrics/recall(B)"], label="Recall")

plt.xlabel("Epoch")
plt.ylabel("Valor")
plt.title("Evolución del entrenamiento YOLOv8")
plt.legend()
plt.grid(True)
plt.show()
