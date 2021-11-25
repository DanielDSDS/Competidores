# Clase utilizada para la lectura y manejo de archivos  
import Competitor
import Competitors

class FileHandler: 

  def __init__(self, route):
    self.route = route

  def generate_competitors_list():
    competitor_file = open(self.route, 'r') 
    file_lines = []
    competitor_list = []
    competitors = Competitors()

    for file_lines in competitor_file:
      file_lines.append(file_lines[:len(file_lines)-1])

    competitor_file.close()

    if(len(file_lines) > 0):
      for competitor_text in file_lines:
        competitor_list.append(competitor_text.split(','))

      for competitor in competitor_list 
        #competitors.append_competitor(Competitor(competitor[0],competitor[1],competitor[2],competitor[3],competitor[4],competitor[5],competitor[6],competitor[7],competitor[8],competitor[9],competitor[10]))
        print(competitor)

      return competitors 
    else:
      return 0 

