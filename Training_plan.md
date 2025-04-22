# Plan de Entrenamiento del Modelo YOLO para Análisis de Daño

Este documento detalla el enfoque técnico y cronograma aproximado para entrenar el modelo personalizado de detección de números en imágenes del juego Wuthering Waves.

## Fase 0: Preparación de datos

- Captura de gameplay en resolución 1920x1080 a 30 FPS para facilitar la extracción de imágenes sin pérdida de calidad.
- Conversión de videos a imágenes individuales utilizando script automatizado.
- Inclusión de imágenes tanto con números como sin números para balancear la detección y reducir falsos positivos.

## Fase 1: Detección básica de números (Semanas 1–2)

- Entrenamiento inicial para que el modelo reconozca correctamente todos los dígitos del 0 al 9 en diversas situaciones.
- Se utilizará una versión ligera de YOLO (YOLOv8n o YOLOv8s).
- Corrección manual del etiquetado en caso de errores visuales.

## Fase 2: Agrupación de dígitos (Semanas 2–4)

- Desarrollo de lógica para detectar cuándo los dígitos forman un número completo.
- Implementación de agrupación por proximidad, tamaño relativo y secuencia.
- Posible etiquetado adicional de números compuestos.

## Fase 3: Reducción de duplicados y seguimiento (Mes 2)

- Establecimiento de una lógica para detectar si un número es una instancia repetida del anterior debido al movimiento de cámara o animación prolongada.
- Consideración del uso de trackeo heurístico por distancia en píxeles y tiempo entre fotogramas.
- Pruebas con imágenes con múltiples golpes simultáneos y números superpuestos.

## Modo de trabajo

- Captura y procesamiento de imágenes durante la semana.
- Entrenamiento continuo del modelo durante la noche y fines de semana.
- Revisión de resultados semanal antes de avanzar a la siguiente fase.

## Herramientas

- YOLOv8 para entrenamiento personalizado.
- Python para el procesamiento de datos, entrenamiento y scripts de etiquetado.
- ElectronJS para interfaz de escritorio.
- Overwolf para integración con el juego.
- ONNX para conversión y despliegue del modelo en entornos productivos de bajo consumo.

## Consideraciones finales

- El modelo será entrenado en hardware de consumo general (GPU AMD o CPU en su defecto).
- Se aplicará validación continua y dataset curado manualmente.
- El objetivo es tener una versión funcional de prueba al finalizar el segundo mes de desarrollo.
