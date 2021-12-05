# Clase utilizada para la lectura y manejo de archivos  
from io import open
from .competitor import Competitor
from .competitors import Competitors

class FileHandler: 

  """
  Clase FileHandler 

  Se encarga de la carga de archivos y el parsing de la data obtenida
  """
  def __init__(self, file_name):
    self.file_name = file_name 

  """
  generate_competitors_list 
  
  Se encarga de obtener la ruta del archivo, separarlo en lineas
  y convertir esas lineas en una lista de competidores 
  """
  def generate_competitors_list(self, DataHandler):
    try:
      competitor_file = open(f"resources/{self.file_name}.txt", 'r') 

      lines = competitor_file.readlines()
      competitor_file.close()

      if(len(lines) > 0):
        competitors_list = DataHandler().format_competitors(lines, Competitor, Competitors)

        return competitors_list 
    except FileNotFoundError:
      print('El archivo indicado no existe en "resources" ')

