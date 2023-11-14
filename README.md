# Web Scraping BBC News

Este script de web scraping en Python utiliza la biblioteca Selenium para extraer información de noticias de la página principal de BBC News en inglés, mediante la identificación de enlaces y la navegación autónoma.

## 1. Instalación:

Instala las librerías necesarias ejecutando los siguientes comandos:

```bash
pip install selenium
pip install pandas
```

## 2. Configuración:

Descarga ChromeDriver, un ejecutable necesario para la automatización con Selenium, desde el sitio oficial de Chromium (https://sites.google.com/chromium.org/driver/).

## 3. Ejecución:

Dirígete a la carpeta correspondiente y ejecuta el código en el terminal:

```bash
python codigo.py
```

El código generará y guardará automáticamente el conjunto de datos.

## Visualización del Conjunto de Datos:

Abre el archivo `bbc_news_dataset.csv` para visualizar el conjunto de datos creado. Este archivo contiene información detallada sobre los títulos, enlaces, fechas e imágenes de las noticias extraídas.
