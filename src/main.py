import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError
import whois # Obtener info de sitios web


def download_page(url):
    """Jugando con el modulo urllib"""
    print('Downloading:', url)
    try:
        html = urllib.request.urlopen(url).read()
    except (URLError, HTTPError, ContentTooShortError) as error:
        print('Download error: ', error.reason)
        html = None
    return html


def data_web(dominio):
    """Jugando un poco: Obteniendo un poco
       de información util de un sitio web"""
    return whois.whois(dominio)


def main():
    url = input("Ingrese url de pagina a descargar> ")
    print (download_page(url))

    dom = input("Dominio(ej: google.com)> ")
    print(data_web(dom))

main()