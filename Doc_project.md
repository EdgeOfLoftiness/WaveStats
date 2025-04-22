#  Proyecto de Captura y Análisis de Daño en Wuthering Waves

##  Objetivo General
Crear una aplicación que permita capturar en tiempo real los daños infligidos por los personajes en el juego **Wuthering Waves**, procesando la información visual mediante modelos de detección entrenados con YOLO, y mostrando estadísticas de daño por segundo (DPS), número de golpes, etc., usando una interfaz integrable con Overwolf.

---

##  Tecnologías
- **Overwolf API**: Integración con el juego, instalación y alojamiento de la app.
- **ElectronJS**: Desarrollo de la interfaz de usuario de escritorio.
- **JavaScript**: Lógica de la interfaz y comunicación con Python.
- **Python**: Procesamiento de imagen y ejecución del modelo.
- **YOLO**: Detección de números flotantes en pantalla (versión ligera y pesada por definir).

---

##  Requisitos Iniciales
- Resolución recomendada: **1920x1080** (relación 16:9).
- Configuración gráfica estable.
- GPU mínima: equivalente a **RX 6500 XT** o superior.
- FPS objetivo: 60, con captura de **8 a 15 imágenes por segundo** para procesamiento.

---

##  Flujo General

1. **Captura de Imagen**: Capturas constantes (8–15 FPS) usando Overwolf.
2. **Preprocesamiento**: Envío de imagen a Python.
3. **Detección**: El modelo YOLO detecta los números de daño flotante.
4. **Filtro de Duplicados**:
   - Comprobación de valores detectados recientemente.
   - Evaluación de tiempo, distancia y movimiento 3D.
   - Permite duplicados válidos (hits simultáneos).
5. **Postprocesamiento**: Agrupación por jugador, tiempo, tipo de daño, etc.
6. **Visualización**: Estadísticas mostradas en la UI con Electron.

---

##  Funcionamiento Local y Futuro Online

- **Fase actual**: Aplicación corre localmente al instalarse.
- **Fase futura**: Lectura de datos enviada a un servidor para guardar y comparar estadísticas entre usuarios.

---

##  Entrenamiento con YOLO + Inferencia con ONNX

Este proyecto utiliza un enfoque dividido en dos etapas principales: **entrenamiento** con YOLO (basado en PyTorch) y **ejecución/inferencia** con ONNX Runtime. Esta separación permite máxima flexibilidad y compatibilidad, especialmente en entornos con GPU AMD o sin GPU dedicada.

---

###  Etapa 1: Entrenamiento con YOLO

YOLO se utiliza para entrenar un modelo que pueda detectar con precisión los números y efectos visuales que aparecen en pantalla durante el combate en Wuthering Waves.

- Se recomienda entrenar en un entorno compatible con PyTorch (CPU o GPU).
- Se pueden usar scripts de extracción de fotogramas desde video (`extract_frames.py`) para preparar datasets.
- El resultado del entrenamiento es un archivo `.pt` (modelo PyTorch entrenado).

```bash```
yolo task=detect mode=train model=yolov8n.yaml data=data.yaml epochs=50 imgsz=640

---

##  Consideraciones
- Dataset entrenado con capturas y videos del juego.
- Modelo dividido en dos versiones:
  - **Ligera**: mejor rendimiento.
  - **Precisa**: mejor detección.
- Se incluirá un **disclaimer** de configuración recomendada para minimizar errores.

---

##  Futuro del Proyecto
- API en la nube para subir resultados por usuario.
- Sistema de perfiles, estadísticas acumuladas, builds, etc.
- Rankings y análisis avanzado.

---

##  Pendientes
- Selección de versión final de YOLO (v5, v7, v8...).
- Implementar tracking 3D ligero para evitar duplicados por movimiento de cámara.
- Sistema de configuración para adaptarse a diferentes PCs sin comprometer el juego.
