from abc import ABC, abstractmethod
from error import SubTipoInvalidoError



class Anuncio(ABC):
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        self.__ancho = ancho if ancho > 0 else 1
        self.__alto = alto if alto > 0 else 1
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo

    @property
    def ancho(self) -> int:
        return self.__ancho

    # Método setter para el ancho
    @ancho.setter
    def ancho(self, ancho: int) -> None:
        if ancho > 0:
            self.__ancho = ancho
        else:
            self.__ancho = 1
    

    # Método de propiedad para acceder al alto
    @property
    def alto(self) -> int:
        return self.__alto
    # Método setter para el alto
    @alto.setter
    def alto(self, alto: int) -> None:
        if alto > 0:
            self.__alto = alto
        else:
            self.__alto = 1




    @property
    def url_archivo(self) -> str:
        return self.__url_archivo

    @url_archivo.setter
    def url_archivo(self, url_archivo: str) -> None:
        self.__url_archivo = url_archivo

    @property
    def url_clic(self) -> str:
        return self.__url_clic

    @url_clic.setter
    def url_clic(self, url_clic: str) -> None:
        self.__url_clic = url_clic

    @property
    def sub_tipo(self) -> str:
        return self.__sub_tipo

    # Método setter para el sub_tipo
    @sub_tipo.setter
    def sub_tipo(self, sub_tipo: str) -> None:
        if (isinstance(self, Video) and sub_tipo not in Video.SUB_TIPOS or
            isinstance(self, Display) and sub_tipo not in Display.SUB_TIPOS or
            isinstance(self, Social) and sub_tipo not in Social.SUB_TIPOS):
            raise SubTipoInvalidoError("El sub_tipo indicado no está permitido para este formato")
        else:
            self.__sub_tipo = sub_tipo

    @staticmethod
    def mostrar_formatos() -> None:  # Método estático para mostrar los formatos disponibles
        print("FORMATO VIDEO:")
        print("==============")
        for v in Video.SUB_TIPOS:
            print(f"- {v}")

        print("FORMATO DISPLAY:")
        print("==============")
        for d in Display.SUB_TIPOS:
            print(f"- {d}")

        print("FORMATO SOCIAL:")
        print("==============")
        for s in Social.SUB_TIPOS:
            print(f"- {s}")

    @abstractmethod
    def comprimir_anuncio(self) -> None:  # Método abstracto para comprimir los anuncio
        pass

    @abstractmethod
    def redimensionar_anuncio(self) -> None:  # Método abstracto para redimensionar los anuncio
        pass


class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")
        
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str, duracion: int) -> None:
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)
        self.duracion = duracion
        
    def comprimir_anuncio(self) -> None:
        print(f"Comprimiendo el anuncio de video: {self.url_archivo}")
        
    def redimensionar_anuncio(self) -> None:
        print(f"Redimensionando el anuncio de video: {self.url_archivo}")

class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")
        
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)
        
    def comprimir_anuncio(self) -> None:
        print(f"Comprimiendo el anuncio de display: {self.url_archivo}")
        
    def redimensionar_anuncio(self) -> None:
        print(f"Redimensionando el anuncio de display: {self.url_archivo}")

class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")
        
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)
        
    def comprimir_anuncio(self) -> None:
        print(f"Comprimiendo el anuncio de redes sociales: {self.url_archivo}")
    
    def redimensionar_anuncio(self) -> None:
        print(f"Redimensionando el anuncio de redes sociales: {self.url_archivo}")
