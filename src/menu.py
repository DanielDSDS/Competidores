# Main menu for action options
import os 
import sys
from services.file_handler import FileHandler
from controllers.data_handler import DataHandler
from exceptions.exception_handler import InvalidFileFormat,  MissingFileSelection

class Menu:
  
  """
  Clase Menu

  Junta las demas clases del proyecto para mostrar la data solicitada
  a su vez aportando navegacion

  constructor() 

  Inicializa las acciones de cada opcion y el layout de los posibles menus
  """
  def __init__(self):
    self.competitor_list = [] 
    self.menu = 0
    self.options = {
      "0": self.salir,
      "1": self.goto_file,
      "2": self.goto_actions,
    }
    self.actions_options = {
      "0": self.go_back,
      "1": self.list_all,
      "2": self.competitors_amount,
      "3": self.competitors_by_age,
      "4": self.competitors_by_gender,
      "5": self.winners_by_age,
      "6": self.winners_by_gender,
      "7": self.winners_by_agengender,
      "8": self.general_winner,
      "9": self.age_histogram,
    }
    self.file_options = {
      "0": self.go_back,
      "1": self.load_file,
    }

    #print para el menu
  def display_menu(self):
    if self.menu == 0:
      self.cls()
      print("""
        ------Estadisticas de Competidores------

        1. Archivo 
        2. Acciones 
        0. Salir
      """)
    elif self.menu == 1:
      self.cls()
      print("""
        -------------- Acciones ---------------

        1. Listar todos los competidores 
        2. Cantidad total de competidores
        3. Cantidad de competidores por grupo etario 
        4. Cantidad de competidores por genero
        5. Ganadores por grupo
        6. Ganadores por sexo 
        7. Ganadores por grupo etario y sexo
        8. Ganador general
        9. Histograma de partitcipantes por grupo etario
        0. Volver
      """)
    elif self.menu == 2: 
      self.cls()
      print("""
        -------------- Archivo -----------------

        1. Cargar Archivo 
        0. Volver
      """)
    else:
      return 0

  #print para acciones
  def display_action_menu(self):
    self.menu = 1 

  #print para el menu
  def display_file_menu(self):
    self.menu = 2

  #correr y mostrar menu
  def run(self):
    while True:
      self.display_menu()
      if self.menu != 3:
        choice = input("Ingresar una opcion: ")

      if self.menu == 0:
        action = self.options.get(choice)
      elif self.menu == 1:
        action = self.actions_options.get(choice)
      elif self.menu == 2:
        action = self.file_options.get(choice)
      
      if action:
        action()
      else:
        print("{0} no es una opcion valida".format(choice))

  #limpiar pantalla
  def cls(self):
    os.system('cls' if os.name=='nt' else 'clear')

  #limpiado de pantalla y navegacion a menu de acciones 
  def goto_actions(self):
    self.cls()
    self.display_action_menu() 

  #limpiado de pantalla y navegacion a menu de archivos 
  def goto_file(self):
    self.cls()
    self.display_file_menu() 

  #salida del sistema 
  def salir(self):
    sys.exit(0)

  def go_back(self):
    self.menu = 0

  """
  list_all() 

  Listado de todos los competidores que participaron
  """
  def list_all(self):
    self.cls()
    while True:
      try:
        if len(self.competitor_list.get_competitors()) == 0:
          raise MissingFileSelection 
        DataHandler().print_table('Lista de Competidores', self.competitor_list.get_competitors_data())
      except (MissingFileSelection) as e:
        print(e)
      input("Presiona cualquier boton para volver al menu principal...")
      self.menu = 0
      return 

  """
  competitors_amount() 

  Retorna la cantidad de competidores participantes
  """
  def competitors_amount(self):
    self.cls()
    while True:
      try:
        if len(self.competitor_list.get_competitors()) == 0:
          raise MissingFileSelection 
        print("\n Cantidad total de competidores\n")
        print(
          f"Compitieron {len(self.competitor_list.get_competitors_data())} personas"
        )
      except (MissingFileSelection) as e:
        print(e)
      input("Presiona cualquier boton para volver al menu principal...")
      self.menu = 0
      return 

  """
  competitors_by_age() 

  Retorna la cantidad de participantes clasificados por grupo etario
  """
  def competitors_by_age(self):
    self.cls()
    while True:
      try:
        if len(self.competitor_list.get_competitors()) == 0:
          raise MissingFileSelection 
        format_text = "{:<10}" * 3
        juniors, seniors, masters = DataHandler().get_competitors_age_group(self.competitor_list.get_competitors())

        print("\n Cantidad de participantes por grupo etario \n")
        print(format_text.format("Juniors", "Seniors", "Masters") + "\n")
        print(format_text.format(len(juniors), len(seniors), len(masters)))
      except (MissingFileSelection) as e:
        print(e)
      input("Presiona cualquier boton para volver al menu principal...")
      self.menu = 0
      return 


  """
  competitors_by_gender() 

  Retorna la cantidad de participantes clasificados por grupo de genero 
  """
  def competitors_by_gender(self):
    self.cls()
    while True:
      try:
        if len(self.competitor_list.get_competitors()) == 0:
          raise MissingFileSelection 
        format_text = "{:<10}" * 3
        male, female = DataHandler().get_competitors_gender_group(self.competitor_list.get_competitors())

        print("\n Cantidad de participantes por grupo etario \n")
        print(
          f"Hay {len(male)} participantes hombres y {len(female)} participantes mujeres"
        )
      except (MissingFileSelection) as e:
        print(e)
      input("Presiona cualquier boton para volver al menu principal...")
      self.menu = 0
      return 


  """
  winners_by_age() 

  Retorna una tabla con los datos de los ganadores clasificados por grupo etario
  """
  def winners_by_age(self):
    self.cls()
    while True:
      try:
        if len(self.competitor_list.get_competitors()) == 0:
          raise MissingFileSelection 
        remappedJuniors = [] 
        remappedSeniors = [] 
        remappedMasters = [] 
        juniors, seniors, masters = DataHandler().get_competitors_age_group(self.competitor_list.get_competitors())
        for junior in juniors:
          remappedJuniors.append(junior.get_data())
        for senior in seniors:
          remappedSeniors.append(senior.get_data())
        for master in masters:
          remappedMasters.append(master.get_data())
        winners_by_age = [DataHandler().get_winner(remappedJuniors), DataHandler().get_winner(remappedSeniors),DataHandler().get_winner(remappedMasters)]
        DataHandler().print_table('Lista de Ganadores por Edad', winners_by_age)

      except (MissingFileSelection) as e:
        print(e)
      input("Presiona cualquier boton para volver al menu principal...")
      self.menu = 0
      return 

  """
  winners_by_gender() 

  Retorna una tabla con los datos de los ganadores clasificados por grupo de genero 
  """
  def winners_by_gender(self):
    self.cls()
    while True:
      try:
        if len(self.competitor_list.get_competitors()) == 0:
          raise MissingFileSelection 
        remappedMales = [] 
        remappedFemales = [] 
        male, female = DataHandler().get_competitors_gender_group(self.competitor_list.get_competitors())
        for m in male:
          remappedMales.append(m.get_data())
        for f in female:
          remappedFemales.append(f.get_data())

        by_gender = [
          DataHandler().get_winner(remappedMales),
          DataHandler().get_winner(remappedFemales),
        ]

        DataHandler().print_table('Lista de Ganadores por Genero', by_gender)
      except (MissingFileSelection) as e:
        print(e)
      input("Presiona cualquier boton para volver al menu principal...")
      self.menu = 0
      return 


  """
  winners_by_agengender() 

  Retorna una tabla con los datos de los ganadores clasificados por grupo de genero y edad 
  """
  def winners_by_agengender(self):
    self.cls()
    while True:
      try:
        if len(self.competitor_list.get_competitors()) == 0:
          raise MissingFileSelection 
        juniors, seniors, masters = DataHandler().get_competitors_age_group(self.competitor_list.get_competitors())
        by_gender_age = map(
          utils.get_winner,
            list(
              DataHandler().get_competitors_gender_group(juniors) +
              DataHandler().get_competitors_gender_group(seniors) +
              DataHandler().get_competitors_gender_group(masters) 
            ),
        )
        DataHandler().print_table('Lista de Ganadores por Grupos de Genero y Edad', by_gender)
      except (MissingFileSelection) as e:
        print(e)
      input("Presiona cualquier boton para volver al menu principal...")
      self.menu = 0
      return

  def general_winner(self):
    self.cls()
    while True:
      try:
        if len(self.competitor_list.get_competitors()) == 0:
          raise MissingFileSelection 
        winner = DataHandler().get_winner(self.competitor_list.get_competitors_data())
        print("\n Ganador General \n")
        print(
          f"El ganador general es {winner['name']} {winner['last_name']} con un tiempo de {winner['hours']} horas {winner['minutes']} minutos {winner['seconds']} segundos \n"
        )
      except (MissingFileSelection) as e:
        print(e)
      input("Presiona cualquier boton para volver al menu principal...")
      self.menu = 0
      return

  """
  age_histogram() 

  Retorn histograma con la agrupacion de participantes clasificados por grupo etario  
  """
  def age_histogram(self):
    self.cls()
    while True:
      try:
        if len(self.competitor_list.get_competitors()) == 0:
          raise MissingFileSelection 
        juniors, seniors, masters = DataHandler().get_competitors_age_group(self.competitor_list.get_competitors())

        print("\n Histograma de participantes por grupo etario\n")
        print(f"Juniors ({len(juniors)}): {'*' * int(len(juniors) / 2)}")
        print(f"Seniors ({len(seniors)}): {'*' * int(len(seniors) / 2)}")
        print(f"Masters ({len(masters)}): {'*' * int(len(masters) / 2)}")
      
      except (MissingFileSelection) as e:
        print(e)

      input("Presiona cualquier boton para volver al menu principal...")
      self.menu = 0
      return

  def load_file(self):
    self.cls()
    while True:
      try:
        print("\n Lineamientos: \n")
        print("* El archivo debe estar ubicado en la carpeta 'resources' del proyecto")
        print("* El archivo debe estar en formato '.txt'")
        print("* Incluya el nombre del archivo sin la extension .txt'")
        print("\n")
        file_name = input("Ingresa el nombre del archivo de competidores: ")
        self.competitor_list = FileHandler(file_name).generate_competitors_list(DataHandler)

      except FileNotFoundError:
        print('El archivo indicado no existe en "resources" ')

      print("\n")
      input("Presiona cualquier boton para volver al menu principal...")
      self.menu = 0
      return