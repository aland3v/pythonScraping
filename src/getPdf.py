from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import os

def request_get(url):
    """
    Realisa una solicitud 'GET' en la url proporcinada, si se realiza con exito retorna el contenido
    y se ocurre algun error retorna 'None'  
    Parametro 'url' direccion del sitio web
    return: 'requests.get.content' 
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def is_good_response(resp):
    """
    Returna 'True' si parametro 'resp' tinen como respuesta 200 (peticion exitosa de la solicitud get)
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)

def log_error(e):
    """
    Imprime los errores  al realizar la solicitud 'GET'
    """
    print(e)


def array_url_pdf(url):
    """
    Obtiene todos los enlaces .pdf y los almacena en un Array
    return: array enlaces_pdf
    """
    raw_html=request_get(url)
    html=BeautifulSoup(raw_html,"html.parser")
    enlaces_pdf=[]
    for link in html.find_all('a'):
        print(link.get('href'))
        # TODO adicionar a la lista solamente los enlaces con terminación .pdf
        enlaces_pdf.append(link.get('href'))
    
    return enlaces_pdf

# TODO implementar un metodo para que descargue la lista 
# de enlacdes devuelta por el metodo array_url_pdf(url)

array_url_pdf('https://www.economiayfinanzas.gob.bo/')