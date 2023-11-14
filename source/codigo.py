import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import re

# Configuración de Selenium y el navegador Chrome
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Ejecutar el navegador en modo silencioso
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3") # Configurar el encabezado HTTP "User-Agent" en la configuración del navegador Chrome controlado por Selenium
driver = webdriver.Chrome(options=options)

# BBC home page
root_url = 'https://www.bbc.com/news'

# Acceder a la página principal
driver.get(root_url)
time.sleep(5)  # Esperar a que el contenido se cargue

# Realizar "infinite scroll" para cargar más noticias
for _ in range(5):  # Número de iteraciones limitado a 5 
    # Ejecutar el script de JavaScript para hacer scroll hasta el final de la página
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Esperar a que se cargue más contenido

# Enlaces de todas las noticias (limitado a los primeros 10 ya que hay infinitos links)
article_links = [a.get_attribute('href') for a in driver.find_elements(By.CSS_SELECTOR, 'div.gs-c-promo a')[:10]]

# Listas para almacenar los datos
titles = []
links = []
images = []
dates = []

# Conjunto para almacenar enlaces ya visitados
visited_links = set()

def find_bbc_article(url):
    '''
    Esta función toma un enlace de artículo como entrada, accede a la página del artículo y 
    extrae el título, la imagen y la fecha de publicación del artículo.
    '''
    print(url)
    # Acceder a la página del artículo
    driver.get(url)
    time.sleep(5)  # Esperar a que el contenido se cargue

    # Encontrar la descripción del artículo
    title = driver.title

    # Encontrar la imagen del artículo
    try:
        img_element = driver.find_element(By.CSS_SELECTOR, 'meta[property="og:image"]')
        img_url = img_element.get_attribute('content')
    except:
        img_url = "No Image"

    # Encontrar el tiempo de publicación del artículo
    try:
        time_element = driver.find_element(By.CLASS_NAME, 'date')
        # Utilizar expresiones regulares para quitar el primer conjunto de caracteres antes de 'h', 'm', o 's'
        article_time = re.sub(r'^\d+[hms]\s*', '', time_element.text.strip())
    except: 
        article_time = "No Date or Live Stream"

    return title, img_url, article_time

def discover_links(url):
    '''
    Esta función encuentra enlaces adicionales dentro de una noticia específica. 
    Se limita a los primeros 10 enlaces para evitar un número excesivo de exploraciones.
    '''
    driver.get(url)
    time.sleep(5)
    # Encontrar enlaces adicionales dentro de las noticias (limitado a los primeros 10)
    additional_links = [a.get_attribute('href') for a in driver.find_elements(By.CSS_SELECTOR, 'div.gs-c-promo a')[:10]]
    return additional_links

# Recorrer todos los enlaces de las noticias y obtener los datos
for i, article_url in enumerate(article_links):
    try:
        if article_url not in visited_links:
            title, img_url, article_time = find_bbc_article(article_url)

            # Agregar los datos a las listas
            titles.append(title)
            links.append(article_url)
            images.append(img_url)
            dates.append(article_time)
            # Descubrir enlaces adicionales dentro de la noticia
            additional_links = discover_links(article_url)
            # Agregar los enlaces adicionales a la lista principal (limitado a los primeros 10)
            if i < 10:
                article_links.extend(additional_links)
            # Agregar el enlace actual al conjunto de enlaces visitados
            visited_links.add(article_url)
    except Exception as e:
        print(f"Error al procesar el artículo {article_url}: {e}")

# Verifica nuevamente que las listas tengan la misma longitud antes de crear el DataFrame
if len(titles) == len(links) == len(dates) == len(images):
    # Crea un DataFrame de pandas con los datos
    news_df = pd.DataFrame({'Title': titles, 'Link': links, 'Date': dates, 'Image': images})

    # Guarda el DataFrame en un archivo CSV 
    news_df.to_csv('bbc_news_dataset.csv', index=False)

    # Cierra el navegador
    driver.quit()
    
    print('Dataset creado y guardado.')
else:
    print('Error: Las listas de títulos y enlaces tienen longitudes diferentes.')
