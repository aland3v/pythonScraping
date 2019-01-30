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

def array_img_src(url):
    """
    Obtiene todos los enlaces(src) de  la imagenes de la URL proporcionada y la almacena en un Array
    return: array_de_imagenes_src
    """
    raw_html=request_get(url)
    html=BeautifulSoup(raw_html,"html.parser")
    src_img=[]
    for img in html.select('img'):
        #print(img['src'])
        src_img.append(img['src'])
    return src_img

def descargar_imagenes(url,ruta=''):
    """
    Descarga las imagenes de una URL proporcionada
    """
    if ruta=='':
        os.mkdir("ImagenesDescargadas")

    list_img_src=array_img_src(url)
    for i in list_img_src:
        if ruta=='':
            
            nom_img=os.path.join(os.getcwd(),"ImagenesDescargadas",i.split("/")[len(i.split("/"))-1])
            print(os.getcwd())    
        else:
            nom_img=ruta+i.split("/")[len(i.split("/"))-1]
        
        imagen = get(i).content
        with open(nom_img, 'wb') as handler:
	        handler.write(imagen)

    
array_img_src("http://blog.educacionit.com/")
descargar_imagenes("http://blog.educacionit.com/")
