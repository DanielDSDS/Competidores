
class Competitors:
  """
  Clase Competitors 

  Clase que almacena el grupo de competidores cargados en el sistema
  """

  def __init__(self):
    self.competitor_list = [] 

  def append_competitor(self, competitor):
    self.competitor_list.append(competitor)
    return 0 

  def get_competitors(self):
    return self.competitor_list


  """
  get_competitors_data() 

  retorna las instancias de competidores almacenadas como diccionarios,
  en vez de objetos
  """
  def get_competitors_data(self):
    competitors = []
    for competitor in self.competitor_list:
      competitors.append(competitor.get_data())
    return competitors 