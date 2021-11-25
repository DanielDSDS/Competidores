# Main menu for action options
import os 
import sys

class Menu:
  
  def __init__(self):
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
      "8": self.general_winners,
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

  def cls(self):
    os.system('cls' if os.name=='nt' else 'clear')

  def goto_actions(self):
    self.cls()
    self.display_action_menu() 

  def goto_file(self):
    self.cls()
    self.display_file_menu() 

  def salir(self):
    sys.exit(0)

  def go_back(self):
    self.menu = 0

  def list_all(self):
    self.menu = 3 
    self.cls()
    print('listar todos')
    return False 

  def competitors_amount(self):
    print('cantidad de competidores')

  def  competitors_by_age(self):
    print('cantidad de competidores por edad')

  def competitors_by_gender(self):
    print('cantidad de ganadores por genero')

  def winners_by_age(self):
    print('ganadores por edad')

  def winners_by_gender(self):
    print('ganadores por genero')

  def winners_by_agengender(self):
    print('ganadores por edad y genero')

  def general_winners(self):
    print('ganadores generales')

  def age_histogram(self):
    print('histograma de edades')

  def load_file(self):
    print('Cargar archivo')
