class InvalidFileFormat(Exception):
    """
      Excepción de carga de archivo segun formato
    """

    def __init__(self):
        super().__init__(
            "El formato del archivo seleccionado no es válido. Solo se permiten archivos 'txt'"
        )


class MissingFileSelection(Exception):
    """
    Excepción causada por la elección de una acción cuando no se ha cargado un archivo
    """

    def __init__(self):

      super().__init__(
        f"Para la realización de acciones debe cargar un archivo primero"
      )
