# Web Scraping BBC News

Este script de web scraping en Python utiliza la biblioteca Selenium para extraer información de noticias de la página principal de BBC News en inglés, mediante la identificación de enlaces y la navegación autónoma.

# Integrantes:
Judith Urbina Córdoba y
Cristina Grau Vílchez

# Archivos que componen el Repositorio:

1. **README.md:** Este archivo proporciona detalles sobre la ejecución del código y contiene el DOI de Zenodo para referencia. Aquí se explican los pasos necesarios para configurar y ejecutar el script.

2. **codigo.py:** Este archivo contiene el código en Python implementado para extraer datos de la página principal de BBC News mediante web scraping utilizando la biblioteca Selenium.

3. **requirements.txt:** En este archivo se encuentran las librerías necesarias para ejecutar el código. Pueden ser instaladas utilizando el comando `pip install -r requirements.txt`.

4. **/dataset/bbc_news_dataset.csv:** Este archivo CSV, ubicado dentro de la carpeta "dataset", contiene el conjunto de datos resultante, con información detallada sobre títulos, enlaces, fechas e imágenes de las noticias extraídas.

# Descripción de uso del código:
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

# DOI de Zenodo del dataset generado:
```bash
10.5281/zenodo.10124551
```
