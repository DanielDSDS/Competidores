#Man ejo de informacion y formatos de data
from datetime import time

class DataHandler:
  """
  Clase DataHandler 

  Se encarga de la manipulación de datos, formato de datos y clasificar competidores
  """

  def __init__(self):
    pass
    
  """
  format_competitors() 

  Crea una listsa de instancias de competidores, es utilizado al leer el archivo
  """
  def format_competitors(self, lines, Competitor, Competitors):
    competitor_list = Competitors() 

    for competitor_text in lines:
      competitor = competitor_text.replace("\n", "").split(',')
      competitor_list.append_competitor(Competitor(competitor[0],competitor[1],competitor[2],competitor[3],competitor[4],competitor[5],competitor[6],competitor[7],competitor[8],competitor[9]))

    return competitor_list 
  
  """
  print_table() 

  Se encarga de darle un titulo y formato de tabla a la lista de competidores que 
  se le pase a esta como argumento
  """
  def print_table(self, list_title, competitors):
    format_text = "{:<10} {:<15} {:<15} {:<15} {:<15} {:<10} {:<10} {:<10} {:<10} {:<10}"

    print("\n" + list_title + "\n")
    print(format_text.format(*list(['cedula', '1º apellido', '2º apellido', 'nombre', 'I. 2º nombre', 'genero', 'edad', 'horas', 'minutos', 'segundos'])) + "\n")

    for competitor in competitors:
      print(format_text.format(*list(competitor.values())))

  """
  get_competitors_age_group() 

  Se encarga de agrupar los grupos etarios de la lista de competidores
    que se pase como argumentos
  """
  def get_competitors_age_group(self, competitors):
    juniors = []
    seniors = []
    masters = []

    for competitor in competitors:
      if(competitor.age_group == 'junior'):
        juniors.append(competitor)
      elif(competitor.age_group == 'senior'):
        seniors.append(competitor)
      elif(competitor.age_group == 'master'):
        masters.append(competitor)

    return juniors, seniors, masters
 
  """
  get_competitors_gender_group() 

  Se encarga de agrupar los grupos de genero de la lista de competidores
    que se pase como argumentos
  """
  def get_competitors_gender_group(self, competitors):
    female = []
    male = []

    for competitor in competitors:
      if(competitor.get_gender() == 'F'):
        female.append(competitor)
      elif(competitor.get_gender() == 'M'):
        male.append(competitor)

    return male, female 

  """
  get_winner() 

  Devuelve el ganador de la lista de competidores pasada como argumento,
  obteniendo el minimo tiempo de los competidores
  """
  def get_winner(self, competitors):
    return min(
      competitors,
      key = lambda c: time(
        int(c['hours']), int(c['minutes']), int(c['seconds'])
      )
    )

