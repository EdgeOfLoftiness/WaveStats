# Reconocimiento de Números de Daño en Wuthering Waves

Este proyecto tiene como objetivo desarrollar una aplicación de escritorio capaz de capturar, procesar y analizar los números de daño generados en pantalla durante las sesiones de juego en Wuthering Waves, utilizando modelos personalizados de detección de objetos basados en YOLO y tecnologías como Overwolf, ElectronJS, y Python.

La aplicación ofrecerá a los usuarios un análisis automatizado de los valores de daño registrados durante el combate, entregando métricas en tiempo real o post-combate, según configuración. El modelo de visión computacional será entrenado utilizando imágenes extraídas de sesiones reales del juego, y se optimizará tanto para precisión como para rendimiento.

## Características principales

- Captura de pantalla en tiempo real (restringido a resoluciones como 1920x1080, 16:9).
- Detección precisa de números de daño individuales y agrupados.
- Agrupación de dígitos para formar valores completos.
- Filtrado de duplicados por movimiento de cámara o animaciones.
- Modo de ejecución liviano mediante modelo exportado a ONNX.
- Interfaz embebida mediante Overwolf para facilitar acceso desde el juego.
- Aplicación multiplataforma construida con ElectronJS y JS.

## Requisitos técnicos

- GPU recomendada: AMD 6500 XT, RTX 2050 o superior.
- Resolución recomendada para uso: 1920x1080.
- Requiere conexión a internet únicamente para descarga inicial (la app correrá localmente).
- Overwolf instalado para la interfaz integrada en juego.

## Licencia y uso

El modelo y su implementación se desarrollarán bajo una licencia compatible con uso privado y futuro uso comercial. ONNX y YOLOv8 permiten distribución siempre que se cumpla con sus respectivas licencias.
