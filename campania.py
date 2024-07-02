# Importar las clases necesarias
from error import LargoExcedidoError, SubTipoInvalidoError
from anuncio import Video, Social, Display
from datetime import date


class Campania():
    def __init__(self, nombre: str, fecha_inicio: date, fecha_termino: date, anuncios: list) -> None:
        self.__nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        self.__anuncios = [self.__obtener_instancia_anuncio(anuncio) for anuncio in anuncios]

    # Método para obtener la instancia del tipo correcto de anuncio
    def __obtener_instancia_anuncio(self, anuncio: dict):
        tipo_anuncio = anuncio.get("tipo", "").lower()
        ancho = anuncio.get("ancho", 0)
        alto = anuncio.get("alto", 0)
        url_archivo = anuncio.get("url_archivo", "")
        url_clic = anuncio.get("url_clic", "")
        sub_tipo = anuncio.get("sub_tipo", "")
        duracion = anuncio.get("duracion", 0)

        if tipo_anuncio == "video":
            return Video(ancho, alto, url_archivo, url_clic, sub_tipo, duracion)
        elif tipo_anuncio == "social":
            return Social(ancho, alto, url_archivo, url_clic, sub_tipo)
        else:
            return Display(ancho, alto, url_archivo, url_clic, sub_tipo)

    # Método de propiedad para acceder al nombre de la campania
    @property
    def nombre(self) -> str:
        return self.__nombre

    # Método setter para el nombre de la campania
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        if len(nombre) > 250: # Verifica que el nombre no supere los 250 caracteres
            raise LargoExcedidoError("El nombre de la campaña excede los 250 carácteres.")
        self.__nombre = nombre
    

    # Método de propiedad para acceder a la fecha de inicio
    @property
    def fecha_inicio(self) -> date:
        return self.__fecha_inicio
    
    # Método setter para la fecha de inicio
    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio: date) -> None:
        self.__fecha_inicio = fecha_inicio

    # Método de propiedad para acceder a la fecha de término
    @property
    def fecha_termino(self) -> date:
        return self.__fecha_termino

    # Método setter para la fecha de término
    @fecha_termino.setter
    def fecha_termino(self, fecha_termino: date) -> None:
        self.__fecha_termino = fecha_termino

    # Método de propiedad para acceder a la lista de anuncios
    @property
    def anuncios(self) -> list:
        return self.__anuncios

    # Método para obtener una representación en cadena de la campania
    def __str__(self):
        cant_video = len(list(filter(lambda x: isinstance(x, Video), self.anuncios)))
        cant_display = len(list(filter(lambda x: isinstance(x, Display), self.anuncios)))
        cant_social = len(list(filter(lambda x: isinstance(x, Social), self.anuncios)))

        return (f"Nombre de la Campania: {self.__nombre}\n"
                f"Anuncios: {cant_video} Video, {cant_display} Display, {cant_social} Social")